# Batch normalization 

This article only talk about the "internal covariate shift" (ICS) problem, other furthur information about BatchNorm please find in the notebook.

***Internal covariate shift (ICS)*** 
In neural networks, the output of the first layer feeds into the second layer, the output of the second layer feeds into the third, and so on. **ICS** is a phenomenon when a distribution of input to a layer changes (shift). Deep learning model have many layers, and for a small change in the first layer lead to the significant change at the last layer, and because of the activate function (for $sigmoid$, $x$ should be in $[-2.5,2.5]$, or ReLu, it should be $\ge 0$), the vanishing problem will be raised. 

It is defined like this, with activation $i$ at time $t$, the ICS will be the difference $||G_{t,i}-G_{t,i}^{'}||_2$, where:

$G_{t,i}= \nabla_{W_i^{(t)}}\frak{{L}}(W_1^{(t)},...,W_k^{(t)};x^{(t)},y^{(t)})$

$G_{t,i}^{'}= \nabla_{W_i^{(t)}}\frak{{L}}(W_1^{(t+1)},...,W_{i-1}^{(t+1)}, W_{i}^{(t)}, W_{i+1}^{(t)},...,W_k^{(t)};x^{(t)},y^{(t)})$

$x^{(t)},y^{(t)}$ is the input-label pairs used to train the network at time $t$
$G_{t,i}$ is the gradient of the model before optimized
$G_{t,i}^{'}$ is the gradient of model after optimized to layer $i$

![image](.\\image\\BatchNorm1.png)

As we can see, with BatchNorm:
* the loss and the gradient value are much more stable, more smooth.  
* It show that BatchNorm help the network increase the correlation between $G_{t,i}$ and $G_{t,i}^{'}$ which means reduce their distance $||G_{t,i}-G_{t,i}^{'}||_2 \rightarrow$ reducing ICS.
* By normalize the value of feature maps after each CNNs layers, its variance will be more stable $\rightarrow$ the gradient value will be more fluency.
* By normalize each layer, we set it back to the distribution as input (normaly whited) $\rightarrow$ avoid vanishing gradient


## Fun fact

Batchnorm was published in 2015, after that we have GoogleNet and VGG were two state-of-the-art model in ImageNet ranking, because of the vanishing/exploring problem, they all had a trick to train a deep model.

For GoogleNet, the reason they stack those CNN together to increase the value of gradient in backpropagation

For VGG, they train a shallow model first (8 layers) to get the high performance then add more layers and keep training, this method also was implemented by YOLO's author as a very interesting way.    

**Reference**
* [Original Batchnorm paper](https://arxiv.org/abs/1502.03167)
* [A explaination why Batchnorm work](https://arxiv.org/abs/1805.11604)
* [Visualize batchnorm effective](https://rohanvarma.me/Batch-Norm/)
* [Batch normalization explained (Medium community)](https://towardsdatascience.com/batch-normalization-the-greatest-breakthrough-in-deep-learning-77e64909d81d)