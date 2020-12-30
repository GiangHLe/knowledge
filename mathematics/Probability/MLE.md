# Maximum Likelihood Estimation (MLE)

***Note: Because it is my note, not a blog or a community forum, this article is mainly translated from the reference and add some of my knowledge, very welcome if you want to discuss about mathematics but please do not question why I just translated the article already there*** 

Should read [Likelihood article](./Likelihood.md) first.

Basically, the event with higher probability will have more chance to happen than the other. 

Assume we have a function $f$ with parameter $\theta$ describe the distribution of a set of data points $X = \{x_1,x_2,...,x_N\}$, we will want to have the maximum probability for each data point follow $f_\theta$ or $\theta = \displaystyle\max_\theta P(x_1,...,x_N\mid \theta) [1]$ where $P(x_1,...,x_N)$ is the probability that event $x_1, ...,x_N$ appear in the same time.

As we discuss in [Likelihood article](./Likelihood.md), in real life problem, we can only observe the data points then find the $\theta$ then comeback to predict the **unseen** data points. 

Normally, it is really hard to solve equation $[1]$, we continue to assume that all data points in $X$ are independent $\Leftrightarrow P(A,B)=P(A)P(B)$, the conditional probability follows all the rule of probability so we have

$$ P(x_1,...,x_N\mid \theta) \approx \displaystyle\prod_{n=1}^N P(x_n \mid \theta)$$$$\Rightarrow \theta = \displaystyle\max_\theta\prod_{n=1}^N P(x_n\mid \theta)$$

We know that $0 \le P(x_i \mid \theta) \le 1 \Rightarrow \displaystyle\lim_{n\rightarrow \infty} P(x_1,...,x_N \mid \theta) = 0$. It is hard to find the  optimal of product, so we can convert it to summation by get logarit (also know as **Log-likelihood**), we can do that because:

* $\log$ of a production equal sum of each element
* $\log$ is an increasing function which mean the highest value still have highest $\log$ value and vice versa.

Our function will become:

$$\theta = \displaystyle\max_\theta\sum_{n=1}^N \log(P(x_n\mid \theta)) $$

The reference has some very clear examples.

**Reference**
* [Vietnamese blog MLE](https://machinelearningcoban.com/2017/07/17/mlemap/#-maximum-likelihood-estimation)
