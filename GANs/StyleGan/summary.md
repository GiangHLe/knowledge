# Style Gan

Evaluated by the same author with Progressive GAN, inherit the stucture of both Generator and Discriminator (even the hyper-parameters). Style Gan introduced a bunch of new things to improve the generator only.

**Note:** StyleGAN only modifies the Generator and Noise input.

Normally, the Generator take input from the noise vector from latent space, but in Style GAN, they generate noise tensor multiple time, modify, learning and push it to model by:
* [Noise Mapping](./noiseMapping.md)
* [Adaptive Instance Normalization](./AdaIN.md)
* [Stochastic Variation](./StochasticVariation.md)

**Noted:** StyleGAN generator begin with the constant tensor for all images, this method also leads to a lot of problem which was discussed in [Constant Input](./constantInput.md)

Then, try to control the Fidelity/Diversity by Mixing Regularization and truncate trick:
* [Style Mixing](./StyleMixing.md)

**Reference**
* [Style GAN paper](https://arxiv.org/abs/1812.04948)
* [Coursera lecture](https://www.coursera.org/learn/build-better-generative-adversarial-networks-gans/home/week/3)
* [StyleGAN Pytorch implement](https://github.com/rosinality/style-based-gan-pytorch)