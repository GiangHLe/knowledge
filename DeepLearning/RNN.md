# Recurrent Neural Networks

Normally, a model will have one input and output. However, there are some tasks that one input at current time is not enough information, even with human, we have to combine the decisions to get the final once, and there is a method to do that in Machine Learning. 

The Recurrent Neural Networks (RNNs) is usually used in the Natural Language Processing (NLP) problem, but we will only focus on computer vision problem, so this article will only contain the image based example.

![drawing](.\\..\\image\\RNN1.png)

The image show that instead of using the last layer to create the probability such as sigmoid or softmax, we change it to RNN block, and set the vector from FC as input.

The image present for the one to many problem (input the image and let the model describe that image), so it will have many outputs (words in this case)