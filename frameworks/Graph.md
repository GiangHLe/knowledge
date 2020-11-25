# Graph

Graph in deep learning framework divide by two kinds:

* Static Graph: Build the graph once time, then we can use it without the code.
  * Advantages: 
    * Faster
    * More safer
  * Disavantages:
    * Lack of flexibility
  * Example: Tensorflow, Theano.
* Static Graph: The graph is built parallel with executing the code, so always need source code to run.
  * Advantages:
    * Flexibility
  * Disavantages:
    * Maybe slower
  * Example: Pytorch

We can image as **C** and **Python**. Nowadays, all frameworks tend to change to Dynamic graph, because of the raising of dynamic models such as [Recurrent networks](./../DeepLearning/RNN.md), Recursive networks or Modular networks.

Take Recurrent networks with NLP problem as an example, the model will have more Recurrent node if the sentence is longer and vice versa.

Therefore, to adapt with this, from version 2.0, Tensorflow start to build the graph with dynamic stucture.
