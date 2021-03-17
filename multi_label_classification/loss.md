# Loss function for multi-label classification task

The loss function for multi-label is nearly similar with the loss from single label, until now, I can find 3 famous loss function for this task

### 1. Binary Cross Entropy with Sigmoid activation

Because of multiple label per ground truth, this method to apply sigmoid activation on output then treat each of them as the binary cross entropy then take the normalize to get final loss value.

$$Loss = \frac{1}{m\times n} \sum_{i=0}^{n} \sum_{j=0}^{m}l_{i,j}(x_{i,j},y_{i,j})$$

$$l_{i,j} = [y_{i,j}\log\sigma(x_{i,j})+ (1-y_{i,j})(1-\log\sigma(x_{i,j}))]$$

Where:

* n is batch_size
* m is number of class per sample
* $l_{i,j}$ is loss value at sample $i$ class $j$
* $\sigma$ is sigmoid function

We can easy implement with Pytorch by using `nn.BCELoss()` and `nn.Sigmoid()` but on Pytorch document (second reference), they said `nn.BCEWithLogitsLoss()` is more better in some way. Besides that, it allow us to sepecify `pos_weight` variable via [this discussion](https://discuss.pytorch.org/t/why-multilabelmarginloss-take-torch-long-has-arguments/28970/6).

```python
# ptrblck's dummy example from: https://discuss.pytorch.org/t/multi-label-classification-in-pytorch/905/45
model = nn.Linear(20, 5) # predict logits for 5 classes
x = torch.randn(1, 20)
y = torch.tensor([[1., 0., 1., 0., 0.]]) # get classA and classC as active

criterion = nn.BCEWithLogitsLoss()
optimizer = optim.SGD(model.parameters(), lr=1e-1)

for epoch in range(20):
    optimizer.zero_grad()
    output = model(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()
    print('Loss: {:.3f}'.format(loss.item()))
```

### 2. Multilabel margin loss

The idea come from the multi-classification hinge loss (svm margin-based loss) 

$$Loss = \frac{1}{n\times m} \sum_{i}^n\sum^m_j\max(0,1-(x_{i,j=y_{i,j}}-x_{i,j\ne y_{i,j}}))$$

The formula was take from Pytorch's document (third reference), I can not find any document clearly explain about that formula so I will explain follow my assumption. 

Follow [cs231n document](https://cs231n.github.io/linear-classify/), hinge loss with each sample has form:

$$L_i = \sum_{j\ne y_i}\max (0, s_j - s_{y_i} + \Delta)$$

where $s_j$ and $s_{y_i}$ are the score predict from model, the formula expect the score of correct class will be higher than other a $\Delta$ to prevent overfitting problem.

Back to our equation, with the expectation output from our model in probability form (~[0.,1.]), the term `1-(something)` play as the regularization to prevent overfitting. Because this is the multi-label classification problem so we need to use sigmoid to convert the output to probability form. 

Pytorch implement

```python
'''
This code from Pytorch document (third reference)
Function MultiLabelMarginLoss require:
    + x is the output from ourmodel, each element should be in probability form
    + y is the target labels, x and y should have the same shape, at each sample, it should be a vector with same length will all vector, and the negative label should be presented as -1
'''
loss = nn.MultiLabelMarginLoss()
x = torch.FloatTensor([[0.1, 0.2, 0.4, 0.8]])
y = torch.LongTensor([[3, 0, -1, -1]])
loss(x, y)
```

**Reference**
* [Pytorch forum discussion](https://discuss.pytorch.org/t/multi-label-classification-in-pytorch/905/)
* [BCE with Logic - Pytorch document](https://pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html)
* [Multilabel margin loss - Pytorch document](https://pytorch.org/docs/stable/generated/torch.nn.MultiLabelMarginLoss.html)
* [Multilabel with soft margin loss- Pytorch document](https://pytorch.org/docs/stable/generated/torch.nn.MultiLabelSoftMarginLoss.html)
