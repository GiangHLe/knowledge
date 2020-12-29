# Weight initilization

The weight initilize for deep learning depend on the activation and the size of the model (network).

***Note***: 

1. The code to calculated the parameters of weight initilization formula

```python
# shape is the shape of tensor W, if dense layer, 
# shape is (layer_i nodes, layer_i+1 nodes), 
# else if cnn, shape is (num_blocks, c_input,h_kernel,w_kernel)
n_j = shape[0] if len(shape) == 2 else np.prod(shape[1:])
n_jPlus = shape[1] if len(shape) == 2 else shape[0]
```

2. Normally, the input image is [normalized](./normalizedInput.md) to help the model more stable 

### For saturable nonlinearities (tanh, sigmoid, etc)
If the weight value is too small, the output from activate function will be step by step come to $0$ then it will means nothing. 

Else if the weight value is too big, the output from activate function will be saturate as 1 in case tanh and sigmoid $\rightarrow$ vanishing gradient.

$\rightarrow$ Start with uniform distribution in this range will help the model learn faster by make the gradient value be more stable and avoid vanishing/exploring gradient.

Use Xavier initilization, with formula:

$W \thicksim U[-\frac{\sqrt{6}}{\sqrt{n_j+n_{j+1}}}, \frac{\sqrt{6}}{\sqrt{n_j+n_{j+1}}}]$

$U$ is uniform distribution
$n_j$ and $n_{j+1}$ was defined above


### For ReLu family (ReLu, Leaky ReLu)

If we use normal distirbution for initilizes the parameters, we will get $50\%$ of weights equal to zero after ReLu. 

Therefore, He introduce new ReLu called PReLu and one way to optimize the initilization with that activation is:

$W \thicksim N[0, \frac{\sqrt{2}}{\sqrt{n_j}}]$ with $N$ is normal distribution.

$PReLU$

$f(y_i)=\begin{cases}
    y_i &\text{if  } y_i>0 \\
    a_iy_i &\text{if  } y_i\leq0
\end{cases}$

where $a_i$ is learnable parameter, 
**Reference**
* [Glorot init paper](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf)
* [Kaiming He paper](https://arxiv.org/pdf/1502.01852.pdf)
* [Keras code impliment](https://github.com/keras-team/keras/blob/998efc04eefa0c14057c1fa87cab71df5b24bf7e/keras/initializations.py)
* [Albumentations paper](https://arxiv.org/abs/1809.06839)