# Likelihood

**"Likelihood"**: We maybe hear about this a lot, actually, everywhere, at least with me. In every book or every lectures that I learned, they mentioned and assumed that we already know what is it. 

Well, it is hard to say, the Likelihood is conditional probability in some case. In statistic, with the let see the definition of likelihood first (or the formula):

$$ \mathcal{L}(\theta \mid x_1,\dots,x_n) = \prod_{i=1}^n f_\theta(x_i) $$

where $\theta$ is the parameters of the model (function) $f$ which has input $x_i$.

Now let take a look on Bayesian Theorem:

$$ P(a \mid b) = \frac{P(b \mid a) P(a)}{P(b)} $$

Where we called $P(b \mid a)$ is the conditional probability of b given a, or likelihood of an event $a$ based on the occurrence of a previous event $b$. So what make likelihood is not probability? Remember that $b$ is the random variable

$\Rightarrow$ The integral of $P(b\mid a)$ over all b posible outcome should be 1.

In the other hand, $\theta$ is parameters of model $f$ so the integral of all $\theta$ do not necessarily equal 1.

From here, I, myself have a conclusion, a conditional probability if a likelihood but the likelihood is not necessarily to be an probability.

#### Machine Learning (ML)

Likelihood is a very important definition in machine learning, it is the baseline for all machine learning (even deep learning) model.

Normally, data in ML is discrete variable, and the process is stochastic (a random process) with outcome $Y$ from the set of parameter $\theta$. Because of the stochastic process so we often do not know $\theta$, so we need to observe $X,Y$, then maximize $P(Y=y\mid \theta)= \mathcal{L}(\theta\mid Y=y)$ ~ This definition only true if we do not know parameters $\theta$

I will not discuss further in continuous case, but you can read about it in references.

**Reference**
* [Likelihood and Conditional](https://stats.stackexchange.com/questions/249031/relation-between-likelihood-conditional-probability-and-failure-rate)
* [Likelihood and Conditional 2](https://stats.stackexchange.com/questions/2641/what-is-the-difference-between-likelihood-and-probability)
* [Likelihood and Conditional 3](https://stats.stackexchange.com/questions/224037/wikipedia-entry-on-likelihood-seems-ambiguous)