# GANs common Problem

### 1. Mode collapse

The target of Generator is to generate the data have same distribution with real dataset, when this problem happen, it means the Generator's parameters is collasped where it stuck in the same point. As we know the loss come from the result of Discriminator which lead to the gradient also come from there $\Rightarrow$ The gradient of the discriminator may point in similar directiions for many similar points.

The reason of this is because the discriminator only process each image as once, so there are no correlation between the gradient of different image which also leads to no variant of the output from generator. We also know that the update of generate will make the discriminator loss increase and vice versa which mean there gradient is opposite $\Rightarrow$ The parameters will stuck at this point forever.

So the solution for this term should be to let discriminator look at batch of images per executed time.

**References:** [Improved Techniques for training GANs](https://arxiv.org/abs/1606.03498)

### 2. Non-convergence

As describe above, it is no convergence point in GANs loss function, 

### 3. Diminished gradient

### 4. Highly sensitive to the hyperparameter selection