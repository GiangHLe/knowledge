# Minibatch Standard Deviation

Assume that we have a tensor $N \times C \times H \times W$, the pytorch code assume that the mini-batch size is 4.

### Step 1:
Split $N$ samples batch to $N/4$ minibatch
Output: $N/4 \times 4 \times C \times H \times W$
### Step 2:
Compute the std of that tensor follow the number of minibatch
Output: $N/4 \times 1 \times C \times H \times W$
### Step 3:
Flatten
Output: $N/4 \times (C \times H \times W)$
### Step 4:
Compute average with each batch of those std
Output: $N/4 \times 1$
### Step 5:
Expand the result to the original size
Output: $N \times 1 \times H \times W$
### Step 6:
Concate the new feature map to the original feature map
Output: $N \times (C+1) \times H \times W$

This step help the generator model return the more variation results. As we maybe know, in traditional GANs, the result from generator has tend to create the similar image even the different input, it's called **mode collapse** problem. By divide to mini-batch, the author hope that this will make the generator richer and learn more from data.

This layer can be placed anywhere in model but the author find out that it is the best right after the last down-scaling layer (in this case, $(8 \times 8) \rightarrow (4 \times 4)$)

[Back to the main page](main.md)