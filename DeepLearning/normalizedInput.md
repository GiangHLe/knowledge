# Normalized Input Image

Nowadays, they verified that normalized the input layer was much better than keep it as original (the scale number will be very large). 

There are many kinds of normalizationm, in this articles just assume that the normalization will be the same with [Albumentations](https://albumentations.ai/docs/):

$x=\frac{x-mean(x)}{std(x)+\epsilon}$

Assume that the input image pixels will bring the value in range $[0,255]$, the code for normalize will look like this

```python
def normalize(img, mean = (0.485, 0.456, 0.406), std = (0.229, 0.224, 0.225), max_pixel_value=255.0):
    mean = np.array(mean, dtype=np.float32)
    mean *= max_pixel_value

    std = np.array(std, dtype=np.float32)
    std *= max_pixel_value

    denominator = np.reciprocal(std, dtype=np.float32)

    img = img.astype(np.float32)
    img -= mean
    img *= denominator
    return img
```

The default **mean** and **std** was calculated from ImageNet dataset, to make the model is more adaptive (overfit) with the own dataset, replace them with training set **mean** and **std** of the dataset. (Please make sure that the dataset is big enough).

The dataset should big enough to divide to 70/30 for training and dev set, and the dev set size should be $10,000$ examples according to [Machine Learning Yearning](https://www.dbooks.org/machine-learning-yearning-1501/) of [Andrew Ng](https://www.andrewng.org/).

**Note:** Albumentations is the very famous augmentation tool for computer vision problems, their paper was published on [ISPRS](https://www.scimagojr.com/journalsearch.php?q=21100427639&tip=sid&clean=0) - a Q1 journal.