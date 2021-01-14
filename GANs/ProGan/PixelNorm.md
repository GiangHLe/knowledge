# Pixel normalization

<span style="font-size:30pt;"><center>$\Large b_{x,y} = \frac{a_{x,y}}{\sqrt{\frac{1}{C}\sum_{j=0}^{C}a_{x,y}^j+\epsilon}}$</center></span>

With:
Consider $a$ is input tensor and $b$ is output tensor.
$a_{x,y}$ is the value at position x,y of tensor $a$, same with $b$ tensor.
$C$ is the number of channels of tensor.
$\epsilon$ is the small number to prevent the $0$ division.

As formula, PixelNorm is a method that scale each vector at $(x,y)$ position with its mean value $\rightarrow$ this is no trainable weights.

This method was used instead of batchnorm, with GANs this help the signal magnitudes (value of feature maps) more stable by normalized all feature. The author confirmed that this method does not harm the generator's result a lots (try on most datasets) but it help to control the convergence very effectively.

**Noted**: This layer only appears in generative models, and because it's non learnable layer so the number of learnable parameters still be the same.

[Back to the main page](summary.md)
