# Side

This is the temporary note, I still don't know where to classify those knowledge

### Low/High pass filter

The low and high pass filter maybe have the different definition in orther field of signal processing, this article only confirm their effects in image processing. 

<center>
<img src="./filters1.png" alt="yolo" width="650">
<figcaption>
Fig 1. Average filter with kernel size is (1,2)
</figcaption>
</center>

Low pass filter is the type of kernel which make the gap between each pixel in image is smaller. For example, Figure 1 show the effect of average filter to signal, we can see each gap of two signal is reduced (replaced by the average value). Therefore, the purpose of low pass filter usually to make the image smoother $\rightarrow$ Blur, Average, etc filter $\rightarrow$ reduce noise.

High pass filter is vice versa, make the gap bigger and usually use to help the image look sharper. (Until this time, I still don't remember any high pass filter kernel example)