# Test time Augmentation

As we know, the Augmentation play a regularization role in the training phase, it guarantee that each inference time, the model will look at different image. 

However, the Augmentation can also use in test time, the method is quite similar to cross validation. With each image in test, we apply augmentation to generate $M$ images then predict on those images. The mean probability from them (example with classification) will be the final result.

We have this phenomenon because the error maybe extends by one sample, but for average multiple images, it can be reduced.