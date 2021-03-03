# Precision, Recall and $F_\beta$ Score

As the title, this article will be about three different types of score which present for the way they evaluate the classification problem in machine learning which named Precision, Recall and $F_\beta$.

For classification problem, we maybe feel familiar with the accuracy. However, in some case, accuracy is not the best metric to evaluate, for example, imbalance dataset. With imbalance data, your model can easily get high accuracy just by bias the higher density label. Those score above will solve this problem.

Let start with the definition of True Positive(TP), False Positive(FP), True Negative(TN), False Negative(FN).

<center>
<img src="./image/PRF1_1.png" width="600">
<figcaption>
Fig 1. Visualize all the combination of True/False Positive/Negative.
</figcaption>
</center>

At first, this idea was implemented for the binary problem only, so if we call 1 class is positive (the lower densitiy label), the other will be negative. However, with multiple classes problem, the new solution will be compute the four values {TP, FP, TN, FN} for each class (consider that class is positive and others are negative) then compute it in different way (continue at the last part).

From Figure 1, we can understand that from the name, for example "False Negative", the first word represent for correct or wrong and the later shows the label of that sample. 

Now, move on with Precision and Recall formula:

$$Precision = \frac{TP}{TP+FP}$$

$$Recall = \frac{TP}{TP +FN}$$

Take a look on the formula, we can see the Precision is the ratio between **the number of sample predicted as correct label** and **all samples that our network predict as correct label** 
$\rightarrow$ show the accuracy of the positive sample that the network think it is correct.
$\Rightarrow$ easy to see that the weakness of Precision is the number of TP points, model just need to make sure about 1 TP point to get Precision = 1.

Next, Recall represents for the ratio between **the number of sample predicted as correct label** and **all the correct label from the dataset** 
$\rightarrow$ show the accuracy of the correct positive sample from all the positive label that should be correct.
$\Rightarrow$ similarity to Precision, the weakness of Recall is the number of wrong positive (FP) points, so if all the sample is predicted as positive, we will get recall = 1.

A good model will have the balance between Precision and Recall, from some example above, we can not guarantee that a model is good with high Precision or Recall only. Therefore, **$F_\beta$** is used as the balance metric with the formula is *harmonic mean* of Precision and Recall.

$$F_\beta=(1+\beta^2)\frac{precision\times recall}{\beta^2\times precision + recall}$$

At $\beta = 1$, the metric will try to balance those scores, $\beta > 1$ will bias Recall. In the other hand, $\beta < 1$ shows that Precision is more important.

**Reference**
* [Harmonic mean](https://www.mathsisfun.com/numbers/harmonic-mean.html)
* [Precision Recall and F beta](https://machinelearningcoban.com/2017/08/31/evaluation/#-accuracy)






















A classification model purpose is to maximise the $P(y|X)\rightarrow$ predict the correct label for each input distribution. To do that, we need to $\max P(y=i|X)$ with $i={1,2,...,n}$ where $n$ is the number of class in dataset. 


Therefore, the accuracy sometime is not enough to evaluate the performance of classification model, e.g: a dog image return the $P(y="dog"|X) = 0.6$ and $P(y="dog"|X) = 0.9$ return the same accuracy.

