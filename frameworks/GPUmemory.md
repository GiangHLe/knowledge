# Why the memory of GPU increase dramatically while training the deep learning model?

Have you ever wondered why just a few hundred MB parameters, that model consumes nearly 20 times that while training?

To make the answer simpler, just one word: **Input**.

For more details, let get back to the simplest equation:

$y=wx+b$ with $x,y$ are input and output, $w,b$ are parameters 

The gradiend of it should be:

$\Large\frac{\delta y}{\delta w} = x$

$\Large\frac{\delta y}{\delta b} = 1$

Therefore, to calculate the gradient for a node, we need to keep the input to that node.

Next the backpropagation depend on the chain rule, so we need to keep all the gradient values of learnable parameters. 

**Note:** ReLu is the save-memory-time activative, because it is simple $\rightarrow$ fast and easy to get gradient (just need to save the signed map which is much lighter tensor compare with others) $\rightarrow$ efficient memory.

In conclusion, the main reason for the increasing memory in GPU is the GPU have to consume the whole graph of model with each node is parameters, input and its gradient.

**Note:** The chart for memory consuming of GPU should have the sine shape (increase after input and release all after optimization), but normally, we will see it raise and stay in the same status until the end of the last epoch (even in valuated phase). It keep the memory to avoid the [memory fragmentation](./MemoryFragmentation.md).

### Solutions

To deal with that, Pytorch raise some solutions, but I am not sure is it good in reality or not.

#### 1. Gradient checkpointing

The idea is quite simple, you don't need to handle the input of each model, just need to save few checkpoints before each nodes and compute the input when the gradient come there.

**Advantages:** still keep the same accuracy, reduce a lot of memory in GPU $\rightarrow$ feel free to increase batch size.

**Disavantages:** Long time training, because we need to load and calculate the input again at each node.

#### 2. Automatic mixed precision

Change the type of variables, for example if one number is 4 bytes required, now you just need 2.

**Advantages:** the training speed still the same, but the memory reduce twice $\rightarrow$ again, increase your batch size.

**Disavantages:** the training model will be hard to convergence, even never, so some technical was applied as a solution for that (loss scaling, master weight copy, casting to FP32 for some layers…) but the performance is still lower than the original ways.

**Reference**
* [SICARA articles](https://www.sicara.ai/blog/2019-28-10-deep-learning-memory-usage-and-pytorch-optimization-tricks).