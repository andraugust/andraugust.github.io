---
layout: default
---

# Notes on "Image Style Transfer Using Convolutional Neural Networks" (Gatys et al, CVPR 2016)

["Image Style Transfer Using Convolutional Neural Networks"](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)

- __Architecture__ Features from VGG19 (16 conv, 5 pool). "Normalize" network weights.  No fully connected layers.  Use avg pool instead of max pool.

- __Content Transfer__ 1) Input an image to CNN, 2) Measure the output at layer $l$, 3) Input a random noise image to the CNN, 4) Apply gradient descent to the noise image such that the output at $l$ matches that of the original image.

Let $X^l_i$ be the outputs from the original image and $X~^l_i$ be the outputs from the constructed image, then the content loss is given by

$J_{content}^l = \sum_{i}{(X^l_i - X~^l_i)^2}$

- __Style representation__  Style is represented by the covariance between channels in a convolutional output.  If a convolutional output has shape NxMxK, then each channel is flattened and arrange into a matrix of shape (N*M)xK.  This matrix is used to compute covariance in the usual way: G = FF^T.

- [picture of style reconstruction from fig. 1]

- __Style Transfer__ Style is transferred just like content is, but instead of matching $X_l$ to $X_l~$, we match $G_l$ to $G_l~$.  The style objective is

$J_{style}^l = \sum{G^l_i - G~^l_i}^2$

Note that G is really 2 dimensional, so technically this should be a double sum, but we're comparing element-wise so we can ignore the complex notation of two sums. If you like, imagine G gets flattened prior to summing, so now we only need one index.

- __Putting it all together__  The final objective is

$J = \sum_{l}{\alpha*J_{content}^l + J_{style}^l}$

Where $\alpha$ is a parameter controlling how much or how little the content is emphasized relative to the style.

- __Heuristics__ The authors point out that it isn't necessary to initialize the generated image to random noise.  Instead, the content image could be the initialization.  In this case there will be one unique generate image (assuming there's a fixed random seed on the objective solver), whereas using a random initialization allows for possibly different generated images to be found.
