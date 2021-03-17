# Selecting class weights for imbalanced dataset

Because of imbalanced problem, in my experience, many famous framework (Tensorflow, Pytorch, etc) add the options `class_weights` into their loss function module. Normally, assume that we are working on the supervised multi-class classification problem, it will be implement like this:

$$loss(x|y=class)=weight(class)\times criterion(x,y)$$

where:

* `weight` is the scale factor of that class.
* `criterion` is the selected loss function: Cross-Entropy, Mean-Square-Error, etc.
* `class` is the correct class of that x

This article will show how can we select the hyper-parameter `class_weights`, we will need a lot of assumption:

* Assume that we are dealing with a binary classification problem, it should be true with the case with multi-labels.
* $loss_{neg},loss_{pos}$ are the approximate loss for negative and positive samples in order, assume that they are all the same.
* $N$ and $P$ are the number of positive and negative samples, respectively.

With any loss function we have:

$$
L = \frac{1}{N+P} (N\times loss_{neg} + P\times loss_{pos}) \\ 
\Leftrightarrow L = 0.5\times loss_{neg} + 0.5 \times loss_{pos}
$$

The `class_weights` should be select in this way:

$$w_n = \frac{1}{N} \frac{N+P}{2}$$ $$w_p = \frac{1}{P} \frac{N+P}{2}$$

with $w_n, w_p$ are the weight of negative and postitive samples, respectively.

$$\Rightarrow L = \frac{1}{N+P} \Bigg( N\times \frac{1}{N} \frac{N+P}{2}\times loss_{neg} + P\times \frac{1}{P} \frac{N+P}{2}\times loss_{pos} \Bigg)$$ $$\Leftrightarrow L = 0.5\times loss_{neg} + 0.5 \times loss_{pos}$$

Easy to see that the loss value still be unchanged. However, in the training process, it will boost the gradient is computed by **the lower density label** $\Rightarrow$ model can learn in similar speed to adapt with two class even the number of samples is much more different.