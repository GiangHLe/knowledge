# Progressive GANs (PGANs)

GANs, as we know, interesting but really hard to control, especially with the generator model. Even Ian Goodfellows admited that he was lucky when chose the hyperparameters for traditional GANs. 

Progressive GANs introduces a new method to training GANs, and other algorithms which help GANs more stable.

1. A new Generator
   Step by step increase
2. New layer in Discriminator
   * They **incresing variation** of **Generator** by using [MiniBatch Standard Deviation](MinibatchStandardDeviation.md)
3. New normalization
   Normally, both D and G networks have a raise the parameters value which is unhealthy for both models. To control/ solve this covariate shift problem, the batch normalization is usually used. However, the author saw that is not GANs problem, so they introduce some new normalize without learnable parameters.

   * [Equalized Learning Rate](equalizedLR.md)
   * [Pixelwise feature vetor Normalization](PixelNorm.md) in **Generator**  
4. New training method
   Actually, it is not so new, the VGG (in Batchnorm funfact part) already did it in past to avoid the vanishing gradient.   

