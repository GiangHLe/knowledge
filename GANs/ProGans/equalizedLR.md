# Equalized learning rate

The author initilize the weight by normal distribution $N\thicksim(0,1)$ for all layers. 

After each time those layers parameters are called (each forward steps), they scale it with the [He's initializer constant](./../DeepLearning/weightInit.md) (the scale factor is the std of Normal distribution of Kaiming)  

```python
def forward(self, x, equalized):
    # generate He constant depend on the size of tensor W
    size = self.module.weight.size()
    fan_in = prod(size[1:])
    weight = math.sqrt(2.0 / fan_in)

    '''
    forward the module with the previous layer (x)
    A module example:

    import torch.nn as nn
    module = nn.Conv2d(nChannelsPrevious, nChannels, kernelSize, padding=padding, bias=bias) 
    '''
    x = self.module(x)

    if equalized:
        x *= self.weight
    return x
```
<!-- The modern initilization such as He or Xavior will makes some parameters need longer time to be convergence. Because of the different from its position to global minima, we will need different learning rate in different layers to get the global minima for all layers.  -->

With this method, the distance from $W_i$ with $i= 1,2,3,...,n$ and n is number of layers to its convergence value will be the same, so we just need to find a suitable learning rate to adapt all.



