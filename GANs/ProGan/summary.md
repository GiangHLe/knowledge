# Progressive GANs (PGANs)

GANs, as we know, interesting but really hard to control, especially with the generator model. Even Ian Goodfellows admited that he was lucky when chose the hyperparameters for traditional GANs. 

Progressive GANs introduces a new method to training GANs, and other algorithms which help GANs more stable.

1. [Progressive Process.](./Progressive.md)
2. New layer in Discriminator
   * They **incresing variation** of **Generator** by using [MiniBatch Standard Deviation](MinibatchStandardDeviation.md)
3. New normalization
   Normally, both D and G networks have a raise the parameters value which is unhealthy for both models. To solve this covariate shift problem, the batch normalization is usually used. However, the author saw that with GANs, they need different method to solve the problem, so they introduce some new normalizer without learnable parameters, simpler, but more efficient.

   * [Equalized Learning Rate](equalizedLR.md)
   * [Pixelwise feature vetor Normalization](PixelNorm.md) in **Generator**  
