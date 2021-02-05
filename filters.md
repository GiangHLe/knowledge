# Side

This is the temporary note, I still don't know where to classify those knowledge

### Low/High pass filter

The low and high pass filter maybe have the different definition in orther field of signal processing, this article only confirm their effects in image processing. 

<center>
<img src="./filters1.png" alt="yolo" width="650">
<figcaption>
Fig 1. Average filter with kernel size is (1,2)
</figcaption>
</center>

Low pass filter is the type of kernel which make the gap between each pixel in image is smaller. For example, Figure 1 show the effect of average filter to signal, we can see each gap of two signal is reduced (replaced by the average value). Therefore, the purpose of low pass filter usually to make the image smoother $\rightarrow$ Blur, Average, etc filter $\rightarrow$ reduce noise.

High pass filter is vice versa, make the gap bigger and usually use to help the image look sharper. (Until this time, I still don't remember any high pass filter kernel example)

### Infimum and Supremum

Let start with the Infimum, it is easier for us to understand the definition if we distinguish **minimum** and **infimum** through the example:

Let say we have a set $S=x\in(0,1)=\{x|0<x<1\}$

Minimum can be define as the lowest value in a set which we can see that not exist here 
$\Rightarrow min\{x|0<x<1\} = \empty$

From [Wikipedia](https://en.wikipedia.org/wiki/Infimum_and_supremum), the infimum of a set S is defined as the greatest number that is less than or equal to all elements of S.
$\Rightarrow\displaystyle\inf\{x|0<x<1\}=0$

* It is a fact that every non empty set (bounded below) of real numbers has an infimum. But, as we saw, not every real set has a minimum.
* In some case, infimum and minimum can be the same in some case. Example: for set $S = \{1,2,3,4,5\}$
$\Rightarrow \min\{S\}=\inf\{S\}=1$ and $\max\{S\}=\sup\{S\}=5$

Same definition for supremum but I haven't come up with any good examples yet.