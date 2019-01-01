---
layout: default
---

# Notes on "Image Style Transfer Using Convolutional Neural Networks" (Gatys et al, CVPR 2016)

- Features from VGG19 (16 conv, 5 pool)
- "Normalize" network weights
- No fully connected layers
- Use avg pool instead of max pool
- 1) Input an image to CNN, 2) Measure the output at layer l, 3) Input a random noise image to the CNN, 4) Apply gradient descent to the input such that the output at l matches that of the original image.  Call this process _content reconstruction_.
- [picture of content reconstruction from fig. 1]
- Style representation.  Style is represented by the covariance of channels in a convolutional output.  Each channel is flattened and treated like a vector, then the collection of vectors is used to compute a covariance as usual: G = FF^T.
- Style reconstruction. Style can be reconstructed in exactly the same way as content, however this time the objective function is defined in terms of style error.
- [picture of style reconstruction from fig. 1]

If layer l consists of feature maps indexed by k, then the
