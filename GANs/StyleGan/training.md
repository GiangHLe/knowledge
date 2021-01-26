# Training

Tero Karass is my favourite author from now on, he provided all the hyper-parameters and training strategies. Besides that, he explained clearly why he selected those things (except StyleGAN2). This article will store all the necessary information to training StyleGAN.

StyleGAN used some information with ProGAN:

* Discriminator architecture
* Adam optimization (same beta parameters)
* Exponential moving average of the generator
* Activation Leaky ReLU with $\alpha = 0.2$
* [Equalized learning rate](./../ProGan/equalizedLR.md) for all layers $\Rightarrow$ weight parameters for all kind of layer (convolution, dense/fc) is initilized using gaussian $N(0,1)$, bias initilized with zero value
* ***REMOVE*** pixelwise feature vector normalization.

And other signature things:

* Mirror augmentation (Flip X) for CelebA-HG and FFHQ but not LSUN.
* The downsampling and upsampling replace from the nearest-neighbor method to bilinear method.
* Implement Progressive process but start at resolution $8^2$ (constant at $4^2$)
* Noise scaling factor is initialized to zero
* Bias style $y_s$ and the constant tensor $4\times 4 \times 512$ are initialized to one.
* Loss function WGAN-GP

For FFHQ dataset:

* Switch from WGAN-GP to non-saturating loss with $T_1$ regularization using $\gamma = 10$
* Increase training time from 12M to 25M images.
* Set learning rate to 0.002 instead of 0.003 for two resolution $512^2$ and $1024^2$ elad to better stability.