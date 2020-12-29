# Just some funny note (but important)

1. The batch Normalization is different between **Pytorch** and **Tensorflow**: $momentum_{pytorch}=1-momentum_{tensorflow}\Rightarrow$, so if we want to pre-produce a model, we should research the original weights was created by Tf or torch to modified the hyperparameter momentum in batch norm to adapt with what we want (or it will be really bad).
2. The Conv2dStaticSamePadding and  MaxPool2dStaticSamePadding between them is different, please come back and dig deeper in [this link](https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch) when you have more time 
