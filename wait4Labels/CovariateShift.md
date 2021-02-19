# Covariate Shift

Covariate Shift or Internal Covariate Shift is one of the greatest problem of deep leanring model. In reality, the main effect of batch normalization is to reduce the effect of this phenomenon. This article will explain what is it?

Its definition relate to the datashift problem. For example, we train a model to predict a cat with the all-black cat training set, then in the test set there are all color cats. In more mathematics way, we can say the data distribution of training set and test set are different. For more details, this can shows the important in the way we divide training and validation set (both of them should have same distribution).

<center>
<img src = "./image/CovariateShift1.png" width = '500'>
<figcaption>
Figure 1. The discord of all hidden layer without batch normalization.
</ficaption>
</center>

The covariate shift happens in each layer of deep learning that why they are called **internal**. Take example in Fig 1, look at second hidden layer (h2), it is computed from first hidden layer(h1) and connect to next layer(h3). Since we know those parameters are learnable, so whenever the weight matrix is updated to transform from h2 to h3, it rely on the result from h1 which is also trained to adapt with the input. 

Interal Covariate Shift is the phenomenon where the distribution of each hidden layer in deep learning model become noisy and hard to connect each other that leads to the reason why we have to careful init the weight and set very low learning rate before batch norm appeared.

**References:** 

* [Covariate Shift Medium](https://towardsdatascience.com/understanding-dataset-shift-f2a5a262a766#:~:text=Covariate%20shift%20is%20the%20change,spatial%2C%20or%20less%20obvious.%20%E2%80%94)
* [Why does batch norm work? Deep learning coursera](https://www.youtube.com/watch?v=nUUqwaxLnWs&ab_channel=Deeplearning.ai)