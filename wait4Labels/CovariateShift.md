# Covariate Shift

Covariate Shift or Internal Covariate Shift is one of the greatest problem of deep leanring model. In reality, the main effect of batch normalization is to reduce the effect of this phenomenon. This article will explain what is it?

Its definition relate to the datashift problem. For example, we train a model to predict a cat with the all-black cat training set, then in the test set there are all color cats. In more mathematics way, we can say the data distribution of training set and test set are different



**References:** 

* [Covariate Shift Medium](https://towardsdatascience.com/understanding-dataset-shift-f2a5a262a766#:~:text=Covariate%20shift%20is%20the%20change,spatial%2C%20or%20less%20obvious.%20%E2%80%94)
* [Why does batch norm work? Deep learning coursera](https://www.youtube.com/watch?v=nUUqwaxLnWs&ab_channel=Deeplearning.ai)