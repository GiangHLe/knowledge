# Accumulation gradient

Similar to the title, the main idea of this idea is the sum of the gradient, the question is when we do that?

Normally, to make a deep learning model better, we need to increase the resolution of the image fed to the model, or the size of model (more layer, each layer is deeper). Unfortunately, all of those options rise the number of parameters which leads to an increase in GPU memory, for example, EfficientNet B7 need nearly 10GB per image with input size 600x600 (the size use by the author). It will not suitable for some people who do not have the condition for large Memory capacity in their private PC or rent the server.

So this accumulation gradient for when we cannot feed a large batch size into our GPU at once but still able to get the same performance in optimization step. Let play around with the mathematics to demonstrate how it works. 

Please move to [code part if you only need implement](#code-implement-pytorch-only)

#### Math explaination

Assume that we have a Mean-Squared-Error loss, and the last layer will be a Dense layer without any activate function, our formula will become:

$$
f(x)=W^Tx+b\\L=\frac{1}{2m}\displaystyle\sum_{i=1}^m (y_i-f(x_i))^2
$$ 

Now we need to find the derivative of $L$ follow $W$:

$$
\frac{\delta L}{\delta W}= \frac{1}{2m} \sum_{i=1}^m \frac{\delta}{\delta W} (y_i-f(x_i))^2\\
=\frac{1}{2m} \sum_{i=1}^m 2(y_i-f(x_i))\frac{\delta}{\delta W} (y_i-f(x_i))\\
=\frac{1}{m} \sum_{i=1}^m (y_i-f(x_i))\frac{\delta}{\delta W}f(x_i)\\
=\frac{1}{m} \sum_{i=1}^m (y_i-f(x_i))x_i^T
$$

We can easily see that the gradient also the accumulate of the gradient of each $x_i$, it is maybe different with other loss functions but it will be true with the common once such as MSE or Cross Entropy. 

In some situations, we have to take batch size equal 1 because of memory problem, and if we update the parameter with each samples, the model will be unstable and $W$ will be optimized to adapt with one direction per sample only. With the formula above, our solution is to sum all the gradient together then divide by $m$.

#### Code implement (Pytorch only)

It is very easy to implement with Pytorch when we understand well about `loss.backward()`, `optim.step()`, `optim.zero_grad()`, and the way how can they generate the computation graph in Pytorch. Maybe I am wrong in this step, please check the discussion on Pytorch forum in the [references](#reference) for more information. Further, those step and knowleadge should be implement for dynamic graph only (for more details, take a look in [this articles](./../frameworks/Graph.md)), so I am not sure the same idea can implement on Tensorflow or not, even Tensorflow 2.0 and above.

```python
model = RandomModel() # model generate, generate the graph
model.cuda()
optimizer = torch.optim.adam(model.parameters(), lr = 1e-3) # optimizer generate
criterion = torch.nn.MSELoss() # loss generate

for data in DataLoader():
    optimizer.zero_grad() # release all the gradient values out of the graph
    x = data['image'].cuda() 
    y = data['label'].cuda()
    output = model(x) # fill values to the graph, this inference will hold the cache for backward step, the GPU memory increase
    loss = criterion(output, y)
    loss.backward() # fill the gradient to the graph, release the input value
    optimizer.step() # update all parameter, this step should consume the same 
```

Now, we know that our memory problem come from `loss.backward()`, we just need to modify it 

```python
real_batch = 64
optim.zero_grad()
for i,data in enumerate(DataLoader()):
    x = data['image'].cuda()
    y = data['label'].cuda()
    output = model(x)
    loss = criterion(output, y)
    loss.backward()
    if i % real_batch == 0:
        optimizer.step() # update after take gradient of 64 samples
        optimizer.zero_grad()
```

Remember that for $n_{th}$ times call `loss.backward()`, the final result will be sum of gradient, not average, so to devide for the number of samples, my solution right now is divide the learning rate for the batch size in SGD case only, take a look back to math formula of other optimizer, we can see that they do the various thing with gradient before update so scale the learning rate maybe not a good idea (still wait for the answer on Forum)

```python
lr /= real_batch # 64 in the example above
optimizer = torch.optim.adam(model.parameters(), lr = lr)
```

#### Note:

I get the answer for the question above, even there is no mathematics proof, but the author reached the second rank in the huge competition on Kaggle so I think I can trust him, the correct code should be:

```python
real_batch = 64
optim.zero_grad()
for i,data in enumerate(DataLoader()):
    x = data['image'].cuda()
    y = data['label'].cuda()
    output = model(x)
    loss = criterion(output, y)
    (loss/real_batch).backward() # here, it take the average
    if i % real_batch == 0:
        optimizer.step() # update after take gradient of 64 samples
        optimizer.zero_grad()
```

**Another note**

All the code snippets in this article use batch size equal 1 in the DataLoader.

#### **References**
* [Article on medium](https://towardsdatascience.com/what-is-gradient-accumulation-in-deep-learning-ec034122cfa#:~:text=Gradient%20accumulation%20means%20running%20a,to%20compute%20the%20variable%20updates.)
* [Pytorch discussion](https://discuss.pytorch.org/t/why-do-we-need-to-set-the-gradients-manually-to-zero-in-pytorch/4903/81)