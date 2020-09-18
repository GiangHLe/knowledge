# Batch normalization 

This article only talk about the "internal covariate shift" (ICS) problem, other furthur information about BatchNorm please find in the notebook.

***Internal covariate shift (ICS)*** 
In neural networks, the output of the first layer feeds into the second layer, the output of the second layer feeds into the third, and so on. **ICS** is a phenomenon when a distribution of input to a layer changes (shift). Deep learning model have many layers, and for a small change in the first layer lead to the significant change at the last layer, and because of the activate function (for <img src="http://www.sciweavers.org/tex2img.php?eq=sigmoid&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="sigmoid" width="72" height="19" /,<img src="http://www.sciweavers.org/tex2img.php?eq=%20x&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" x" width="15" height="12" /> should be in <img src="http://www.sciweavers.org/tex2img.php?eq=%5B-2.5%2C2.5%5D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="[-2.5,2.5]" width="96" height="18" />, or ReLu, it should be <img src="http://www.sciweavers.org/tex2img.php?eq=%5Cge%200&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\ge 0" width="31" height="17" />), the vanishing problem will be raised. 

It is defined like this, with activation $i$ at time $t$, the ICS will be the difference, <img src="http://www.sciweavers.org/tex2img.php?eq=%7C%7CG_%7Bt%2Ci%7D-G_%7Bt%2Ci%7D%5E%7B%27%7D%7C%7C_2&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="||G_{t,i}-G_{t,i}^{'}||_2" width="106" height="29" />where:

<!-- $G_{t,i}= \nabla_{W_i^{(t)}}\frak{{L}}(W_1^{(t)},...,W_k^{(t)};x^{(t)},y^{(t)})$

$G_{t,i}^{'}= \nabla_{W_i^{(t)}}\frak{{L}}(W_1^{(t+1)},...,W_{i-1}^{(t+1)}, W_{i}^{(t)}, W_{i+1}^{(t)},...,W_k^{(t)};x^{(t)},y^{(t)})$ -->

<img src="http://www.sciweavers.org/tex2img.php?eq=G_%7Bt%2Ci%7D%3D%20%5Cnabla_%7BW_i%5E%7B%28t%29%7D%7D%5Cfrak%7B%7BL%7D%7D%28W_1%5E%7B%28t%29%7D%2C...%2CW_k%5E%7B%28t%29%7D%3Bx%5E%7B%28t%29%7D%2Cy%5E%7B%28t%29%7D%29%0A%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="G_{t,i}= \nabla_{W_i^{(t)}}\frak{{L}}(W_1^{(t)},...,W_k^{(t)};x^{(t)},y^{(t)})" width="289" height="35" />

<img src="http://www.sciweavers.org/tex2img.php?eq=G_%7Bt%2Ci%7D%5E%7B%27%7D%3D%20%5Cnabla_%7BW_i%5E%7B%28t%29%7D%7D%5Cfrak%7B%7BL%7D%7D%28W_1%5E%7B%28t%2B1%29%7D%2C...%2CW_%7Bi-1%7D%5E%7B%28t%2B1%29%7D%2C%20W_%7Bi%7D%5E%7B%28t%29%7D%2C%20W_%7Bi%2B1%7D%5E%7B%28t%29%7D%2C...%2CW_k%5E%7B%28t%29%7D%3Bx%5E%7B%28t%29%7D%2Cy%5E%7B%28t%29%7D%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="G_{t,i}^{'}= \nabla_{W_i^{(t)}}\frak{{L}}(W_1^{(t+1)},...,W_{i-1}^{(t+1)}, W_{i}^{(t)}, W_{i+1}^{(t)},...,W_k^{(t)};x^{(t)},y^{(t)})" width="485" height="35" />



<img src="http://www.sciweavers.org/tex2img.php?eq=%24x%5E%7B%28t%29%7D%2Cy%5E%7B%28t%29%7D%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$x^{(t)},y^{(t)}$" width="64" height="22" /> is the input-label pairs used to train the network at time <img src="http://www.sciweavers.org/tex2img.php?eq=t&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0" align="center" border="0" alt="t" width="12" height="14" />
<img src="http://www.sciweavers.org/tex2img.php?eq=G_%7Bt%2Ci%7D&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0" align="center" border="0" alt="G_{t,i}" width="32" height="19" /> is the gradient of the model before optimized
<img src="http://www.sciweavers.org/tex2img.php?eq=G_%7Bt%2Ci%7D%5E%7B%27%7D&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0" align="center" border="0" alt="G_{t,i}^{'}" width="32" height="29" /> is the gradient of model after optimized to layer <img src="http://www.sciweavers.org/tex2img.php?eq=i&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0" align="center" border="0" alt="i" width="11" height="15" />

<center><img src="./../image/BatchNorm1.png" alt="BatchNorm Chart" width="500"/><figcaption>Fig 1. The comparasion between Original VGG and VGG with BatchNorm </figcaption></center>



As we can see, with BatchNorm:

* the loss and the gradient value are much more stable, more smooth.  
* It show that BatchNorm help the network increase the correlation between <img src="http://www.sciweavers.org/tex2img.php?eq=%24G_%7Bt%2Ci%7D%24%20&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0" align="center" border="0" alt="$G_{t,i}$ " width="32" height="18" /> and <img src="http://www.sciweavers.org/tex2img.php?eq=G_%7Bt%2Ci%7D%5E%7B%27%7D&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0" align="center" border="0" alt="G_{t,i}^{'}" width="32" height="29" /> which means reduce their distance <img src="http://www.sciweavers.org/tex2img.php?eq=%24%7C%7CG_%7Bt%2Ci%7D-G_%7Bt%2Ci%7D%5E%7B%27%7D%7C%7C_2%20%5Crightarrow%24&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0" align="center" border="0" alt="$||G_{t,i}-G_{t,i}^{'}||_2 \rightarrow$" width="129" height="29" /> reducing ICS.
* By normalize the value of feature maps after each CNNs layers, its variance will be more stable <img src="http://www.sciweavers.org/tex2img.php?eq=%5Crightarrow&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0" align="center" border="0" alt="\rightarrow" width="19" height="8" />the gradient value will be more fluency.
* By normalize each layer, we set it back to the distribution as input (normaly whited) <img src="http://www.sciweavers.org/tex2img.php?eq=%5Crightarrow&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0" align="center" border="0" alt="\rightarrow" width="19" height="8" />avoid vanishing gradient

**Reference**

* [Original Batchnorm paper](https://arxiv.org/abs/1502.03167)
* [A explaination why Batchnorm work](https://arxiv.org/abs/1805.11604)
* [Visualize batchnorm effective](https://rohanvarma.me/Batch-Norm/)
* [Batch normalization explained (Medium community)](https://towardsdatascience.com/batch-normalization-the-greatest-breakthrough-in-deep-learning-77e64909d81d)