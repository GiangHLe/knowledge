# Average Precision

In classification problem, we have precision and recall metrics to evaluate model performance, the same thing with object detection problem.

$Precision= \frac{TP}{TP+FP}$

$Recall = \frac{TP}{TP+FN}$

In object detection, they care more about the precision rate. Therefore, the different here is how we assign which one is $True$ $Positive$ or $False$ $Positive$.

* ##### Note: The previous word present for the actual, and later for predicted (True Negative means Positive class in actual, and model predict it is negative).

First, we need to know about Intersection over Union (IoU), it's quite easy to understand if we look at the picture

![image](.\\..\\image\\ObjectDetectionEvaluate1.png)

**True Positive:** 
* IoU > IoU_Threshold
* Confidence_score > confidence_Threshold 
* The model predict the correct label

**False Positive:**
* IoU < IoU_Threshold
* Confidence_score > confidence_Threshold 
* The model predict the correct label

**False Negative:**
* IoU > IoU_Threshold
* Confidence_score > confidence_Threshold
* The model predict the wrong label 

With those definations above, we can calculate the precision of each class with the stable IoU.

Nowadays, the competition usually have three kind of AP which is $AP, AP^{50}, AP^{75}$ which $50$ and $75$ mean the IoU score to decide an object is $TP$ or not ($0.5$ and $0.75$). $AP$ is the little different, it is range from $0.5$ to $0.95$ with each step is $0.05$ that means $10$ threshold.

$\rightarrow$ It will be $10$ $Precision$ value for those threshold and we take the average, then it is called $Average$ $Precision$ also known as $AP$.

$\rightarrow$ The $Mean$ $Average$ $Precision$ means the average of those $AP$ points with different labels.

###Conclusion:

* $AP$ is the $Mean$ $Average$ $Precision$ in short term which is the mean from various of IoU Threshold value.
* $AP^{50}$ is the average $Precision$ value of different classes with threshold $75\%$
* $AP^{75}$ is the same with $AP^{50}$ but with threshold $50\%$ 
 
