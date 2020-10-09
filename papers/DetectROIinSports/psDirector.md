# PsDirector

Following those steps:
1. Extract soccer field
2. Extract motion module
3. Attractive ROI with fixed size was created depend on result from step 1 and 2.
4. Detect player on in the ROI only
5. Apply the attacking direction inference module
6. Get the final resullt

**Go in details**

### Soccer field determination
Convert image to HSI color space, then find the histogram of each channel (H,S,I). Based on that, we can segment the soccer field.

The result can't be trust with one frame only, so we should calculated the field on 10 frames then adjust the result is the union as pixel level of them.

***Note***: we should apply morphological operations to fill small holes or reduce noise in result.

### Motion Extraction and Attractive ROI Positioning

Take 2 image subtract between each 5 frame then the motion image will show the different between them. They didn't mention about it, but I think it is some think like this:

```python
import numpy as np
# pseudo code
subtraction = np.abs(k_plus_five_frame - k_frame)
motion_mask = subtraction > threshold
```

Then **AND** it with the mask from the first task (because we only care about the object in soccer field). Use that image, we will have

$\begin{cases}
    i_w = \alpha_w \times |i-\frac{w}{2}|\\
    j_h = \alpha_h \times |j-h|
\end{cases}$

Where:
* $\alpha_w$ and $\alpha_w$ are the hardware parameters, we will get it after setting the camera.
* $w,h$ are the weight and the height of the panoramic picture.
* $i,j$ is the postion of pixel on image, related to the equation below

$\begin{cases}
    \displaystyle\max_y = \displaystyle\sum_{j=y}^{y+boxH}\displaystyle\sum_{i=0}^{w}(i_w+j_h)sgn(I(i,j))\\
    \displaystyle\max_x = \displaystyle\sum_{i=x}^{x+boxH}\displaystyle\sum_{j=y}^{y+boxW}(i_w+j_h)sgn(I(i,j))
\end{cases}$

Where:
* $I$ is the result from **AND** operation, and $I(i,j)$ is the pixel value (in binary, I guess) of that image at position $(i,j)$.
* $boxH,boxW$ is the fixed weight and height of the attractive ROI.

It is easy to understand that we should find a postion $(x,y)$ where the box $(x,y,boxW,boxH)$ will contain as much movement objects as possible.

### Detect player and other

Call $R_1=(x_1,y_1,x_2,y_2)$ is Attractive ROI.

Use YOLOv3 on the Attractive ROI above then find new ROI (Called $R_2$) by formula

Call $p_i$ is detection result of $i$th players and there are $m$ players in Attractive ROI $\rightarrow p_i=(x_i,y_i,w_i,h_i)$ where $i = 1,2,3,...,m$

$\begin{cases}
x_{min}= min(x_i-\frac{w_i}{2})\\
x_{max}= max(x_i+\frac{w_i}{2})\\
y_{min}= min(y_i-\frac{h_i}{2})\\
y_{max}= max(y_i+\frac{h_i}{2})
\end{cases}$

$\rightarrow R_2=(x_{min},y_{min},x_{max},y_{max})$

Then use YOLOv3 again on new ROI. Normally, the result now will be more accurated because it is focus on new smaller ROI.

Calculate mean centers of all player $(x_{mean}, y_{mean})$, with:

$x_{mean} = \frac{1}{m}\displaystyle\sum_{i=1}^m x_i$
$y_{mean} = \frac{1}{m}\displaystyle\sum_{i=1}^m y_i$
$\rightarrow p_{mean} = (x_{mean},y_{mean})$
$\rightarrow Area(R_2) \le Area(R_1)$

Then we compute distance from each player to center point. (The author didn't mention about distance metrics so I assume it was norm 2 or Euclidean distance)

$d_i=||p_i-p_{mean}||$ with $i=1,2,3,..., n$ where $n$ is number of objects in R2.

Then rank them with descending order, choose $T_p$ players nearest to the $p_{mean}$ to generate new view ($R_3$) what they called **basic view**. Normally, $T_p = max(m-4,4)$ 

$\rightarrow R_3 = (x_{bl},y_{bt},x_{br},y_{bb})$
$\rightarrow Area(R_3) \le Area(R_2)$

Human tend to have smaller view when players garthers and bigger when they splits out $\rightarrow$ we need to enlarge the size of basic view. They measure it by the standard deviation of the obtained distances

$std = \sqrt{\frac{\sum_{i=1}^m ((x_i-x)^2+(y_i-y)^2)}{m}} > T_d= (\frac{2}{3} \sqrt{(\frac{w_b}{2})^2+(\frac{h_b}{2})^2})$

With $h_b = y_{bb} - y_{bt}$ and $w_b = x_{br} - x_{bl}$

The ROI will stop enlarging when $std = T_d$ or when ROI's Area will be equal to $R_2$. However, to avoid splitting on players, they still plus $0.01 \times w$ and $0.03 \times h$ to the $x$ and $y$ of the ROI.

**Note**: 
1. From third goal, they will enlarge the view to cover whole situation.
2. When the view near to the corners, they will enlarge the view.

Again, we don't know how much they extend the ROI size.

### Attacking Direction Inference

To easy to understand, this step will create a real ROI that we can see.

They accept for the delay in this step with time delay is $t = 4s$. At $k$th frame, call $R_k$ is the ROI from **detect player and other** and $R_{k+r \times t}$ is the ROI of the frame after $t$ seconds with $r$ is FPS.

Then they try to measure the direction of the real ROI by:

$\begin{cases}
    \sum_{i \in H}sgn(q^i-q^k) \ge T \text{ direction go right/up}\\
    \sum_{i \in H}sgn(q^i-q^k) \le T \text{ direction go left/down}\\
    \text{others is none direction}
\end{cases}$

Where $q\in [x,y]$, and $H=$```range(k,k+r*t,5)``` (stepsize = 5 in part motion extraction), $T = 2$

The real ROI for viewer will be realease follow this formula:

$\LARGE R_{k+i}=\frac{(r\times t - i)\times R_K+i\times R_{k+r\times t}}{r \times t}$

With this formula, the first frame will be $R_k$ and last frame is $R_{k+r\times t}$, during $t$ seconds, the ROI will slowly move and scale the size from $R_k$ to $R_{k+r\times t}$.


**Wrong Note:**
* No measure distance for last part with $q^i - q^k$
  Not sure how to calculate that metrics (what if x is greater and y is lower), recommend:
$\begin{cases}
    \sum_{i \in H}sgn(x^i-x^k) \ge T \text{ direction go right}\\
    \sum_{i \in H}sgn(x^i-x^k) \le T \text{ direction go left}\\
    \sum_{i \in H}sgn(y^i-y^k) \ge T \text{ direction go down}\\
    \sum_{i \in H}sgn(y^i-y^k) \le T \text{ direction go up}\\
\end{cases}$

    Even not sure about their coordinate, maybe it's normal coordinate, not image coordinate. (bigger y is higher). 
* No parameter for enlarge task
  In Object detection and rescale attractive ROI, they mention about how to increase the size ROI when $std = T_d$ but they didn't say how much ROI should be dilated.
* Maybe wrong in first task
  The equation, yeah?
* No explain fo $T_d$ threshold
  Don't know where it come from
* Maybe wrong in last task
  Let assume t = 4. 
  At first, they said the result will be delay for 4s, so I thought it is a real-time solution. However, the author said in the last of that sentence that they splitted the video to many short clips of 4 seconds $\rightarrow$ not real-time then concate them to get the final result. 
* No code, no result video
* Introduce 54 panoramic videos with resolution 3840*800, each video is 2 hours long but didn't release anything
* In Motion Extraction and Attractive ROI measurance part, recommend the equation should be like
  
$\begin{cases}
    \displaystyle\max_y = \displaystyle\sum_{j=y}^{y+boxH}\displaystyle\sum_{i=0}^{w}(i_w+j_h)sgn(I(i,j))\\
    \displaystyle\max_x = \displaystyle\sum_{i=x}^{x+boxW}\displaystyle\sum_{j=y}^{y+boxH}(i_w+j_h)sgn(I(i,j))
\end{cases}$