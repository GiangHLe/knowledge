# Style Gan

Evaluated by the same author with Progressive GAN, inherit the stucture of both Generator and Discriminator (even the hyper-parameters). Style Gan introduced a bunch of new things to improve the generator only.

**Note:** StyleGAN only modifies the Generator and Noise input.

Normally, the Generator take input from the noise vector from latent space. However, StyleGAN start with the one inited tensor, then scale and shift by intermediate noise (which was modified from gaussian noise by learnable parameters), they generate noise tensor multiple time, learning and push it to model by:

* [Noise Mapping](./noiseMapping.md)
* [Adaptive Instance Normalization](./AdaIN.md)
* [Stochastic Variation](./StochasticVariation.md)

**Noted:** StyleGAN generator begin wi
th the constant tensor for all images, this method also leads to a lot of problem which was discussed in [Constant Input](./constantInput.md)

Then, try to control the Fidelity/Diversity by Mixing Regularization and truncate trick:

* [Style Mixing](./StyleMixing.md)

To evaluate the input of Generator, normally, they will need an encoder to transform the image back to noise. However, StyleGAN input in special way so they introduce two new way to verify the benifit of intermediate noise:

* [Perceptual path length](./PerceptualPathLength.md)
* [Linear separability](./LinearSeparability.md)

However, StyleGan also has some problems in [StyleGan problems](problems.md)

**Reference**
* [Style GAN paper](https://arxiv.org/abs/1812.04948)
* [Coursera lecture](https://www.coursera.org/learn/build-better-generative-adversarial-networks-gans/home/week/3)
* [Github link: StyleGAN Pytorch implement](https://github.com/rosinality/style-based-gan-pytorch)
* [Mirror augment](http://datahacker.rs/deep-learning-data-augmentation/)
* [Style GAN weakness](https://github.com/tensorfork/tensorfork/issues/21)