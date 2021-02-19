# [2nd place] Solution Overview
--Ian Pan's idea--

The note for the idea of second solution in this competition.

**Batch size**

Use multi-GPU and make sure it can fit enough size for one batch to get the best result by using batch normalization. Base batch size is 64, if the GPU memory is not enough, reduce batch size to 32 and set the gradient accumulation by 2.

**Back Bone**

Test on EfficientNet, SE-ResNext, ResNest, BiT-Resnet -> EfficientNet is the best.
$\rightarrow$ Smaller model with bigger image is worse (run by [this repo](https://github.com/rwightman/pytorch-image-models))
$\Rightarrow$ Best is EfficientNetB6 (noisy student pre-trained) - 512x512, and EfficientNetB7 - 640x640.

**Upsampling**

The author also used the combination dataset (2019 and 2020) competition which has much larger the number of melanomas images. To make sure that the melanomas from 2019 did not overwhelm the 2020, he upsampling the number of melanomas in 2020 dataset 7 times (to be equal with number of melanomas in 2019 dataset).

**Training**

AdamW, cosine annealing with warm restarts scheduler with init learning rate is 3e-4.

3 snapshots, 2 epochs per each for EfficientNetB6 and 3 per each for EfficientNetB7 $\Rightarrow$ then take the best of the three(only validated on 2020 data) -> each model was selected by this way until enough 5 for 5-fold cross validation (CV)

At first using the metadata which is embeded to be a 32-D vector then concatenated to the final feature vector before the last FC (simple use mean/mode imputation to replace the missing place in csv). $\Rightarrow$ later remove the metadata to get the prize without context data (but he got 2nd rank, didn't know why).

For data, the author used [Chris Deotte’s triple stratified data splits](https://www.kaggle.com/c/siim-isic-melanoma-classification/discussion/165526) - an expert notebook guy, he sumarized, devided fold and resize image for the community (both TFRecord and JPEG format).

**Augmentation**

Used RandAugment with N = 3

Used square cropping during training and inference:

* Training: if image is square $\rightarrow$ ignore, else crop the random square area. Example: $768\times512 \Rightarrow 512\times512$.
* Test/Inference: Use the same strategy with training but take random 10 time $\Rightarrow$ 10 samples per each image then apply [TTA](./../DeepLearning/../../DeepLearning/TTA.md) to calculated the final score for each sample.

**Pseudo Labeling**

Extend 2 class to 3 class to help the model flexible with its tasks by using the data and information from 2019 data (have more labels and more details than 2020 data)