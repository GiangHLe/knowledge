# Maximum a Posteriori (MAP)

The idea should come from an example, if we toss a coin 5 time and get 1 head result, follow Maximum Likelihood, the probability to get the head is $\frac{1}{5}$. And we get conclusion that coss has $20\%$ is head, done...

Just joking, this is what we call overfitting in machine learning, yes, it also happens to human, when we get the conclusion from a small set of data. The MLE function is not wrong, but it is not correct with the small data, we need some more stronger evidences.

Maximum a Posteriori solve this problem by assuming that we know the prior of parameter $\theta$. Opposite with MLE, MAP formula define as maximize the likelihood of $\theta$ given a set $X$.

$$ \theta = \displaystyle\argmax_\theta p(\theta\mid x_1, ..., x_N) [1]$$

**Fact:** $p(\theta\mid x_1,...,x_N)$ is also known as "posteriori probability" of $\theta$ which show the reason of the name

It is very hard to solve $[1]$ formula since $\theta$ is the parameter of the stochastic process, we can do it by combine the **Bayesian Theorem** and the **MLE**.

$$ \theta = \displaystyle\argmax_\theta P(\theta\mid x_1,...,x_N) = \displaystyle\argmax_\theta \Bigg[ \frac{\overbrace{P(x_1,...,x_N\mid \theta)}^{Likelihood}\overbrace{P(\theta)}^{prior}}{\underbrace{P(x_1,...,x_N)}_{evidence}} \Bigg][2]$$

From the [MLE article](./MLE.md), we know that $X=\{x_1,...,x_N\}$ is a set of independent data points which can consider is the constant number, so we can convert the equation as

$$ \theta = \displaystyle\argmax_\theta P(\theta\mid x_1,...,x_N) = \displaystyle\argmax_\theta P(\theta)\prod^N_{n=1}P(x_n)$$

Therefore, we can see that the main different between MAP and MLE is the extension $P(\theta)$, so how can it help the model prevent the overfitting? Let take the logarit of it.

$$ \theta = \displaystyle\argmax_\theta \log (P(\theta)\prod^N_{n=1}P(x_n)) = \displaystyle\argmax_\theta \Bigg[ \sum_{n=1}^N \log(P(x_n)) + \log (P(\theta)) \Bigg] $$

Look familiar now? Does the word "regularization" remind you of something?

**Reference**
* [Vietnamese blog MLE](https://machinelearningcoban.com/2017/07/17/mlemap/#-maximum-likelihood-estimation)