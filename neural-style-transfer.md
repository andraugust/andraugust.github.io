---
layout: default
---

# Notes on Neural Style Transfer

## Background
In the paper [Image Style Transfer Using Convolutional Neural Networks](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf), published by Gatys et al for CVPR 2016, the authors define a neural method for transforming the style of an image so it matches the style of another image.

(im dog) + (im van gogh) = (style transfer)

Neural networks, in particular convolutional ones, have been shown to extract texture information at both hi and low spatial scales.  The photos below, borrowed from the [keras blog](https://blog.keras.io/category/demo.html), show the images that maximally activate filters in an ImageNet trained VGG16.  Note that shallow layers respond to high frequency texture while deep layers respond to low frequency texture.

![im](neural-style-transfer/keras1.png)
![im](neural-style-transfer/keras2.png)
![im](neural-style-transfer/keras3.png)

Given the ability to respond to texture like this, and the correspondence between texture and style, the authors of the paper ask if convolutional output can be used to achieve style transfer. They show that the answer is yes. Here's how they do it.

Let $$X$$ be a $$N \times M \times K$$ matrix containing the output of a convolutional layer in a VGG type network.  $$N$$ and $$M$$ are the spatial shapes determined by the width and height of the input image, $$K$$ is the channel shape determined by the number of conv filters in the layer.  Now treat each channel like a $$NM \times K$$ vector and take the inner product between each pair of channel vectors to form the so-called _style matrix_

$$G = \frac{1}{NM} X^TX$$

We've normalized by spatial shape because we don't want the input shape to influence the magnitude of entries in $$G$$.

We'll compute $$G$$ for the source image and $$\tilde{G}$$ for the destination image, then we'll do gradient descent on the destination image until $$G \approx \tilde{G}$$.  In particular, we'll minimize

$$frac{1}{K^2}\sum_{ij}{(G_{ij} - \tilde{G}_{ij})^2}$$

with respect to the input image.

But why this definition of style matrix?  The authors don't provide an answer, and a look around the internet suggests no clear consensus.  I like to think it's because of this: if instead of making the $$G$$s match, we tried to directly make the conv output match, then we'd find ourselves constructing an image that's pixel-for-pixel equal to the source image.  This suggests that maybe we should try instead to reconstruct the _relationship_ between conv outputs, instead of the exact values.  Dot products are a good candidate for measuring relationship because they calculate the angle between two vectors, so if we try to reconstruct all of the angles between conv vectors then maybe we'll reconstruct the style of the source image and still maintain the content of the destination image.  Of course the real explanation for why $$G$$ is defined this way is that __it works__, so we'll stick with it and do some experiments of our own.

## Implementation

I'm going to use `keras` to implement the transfer.


- __Heuristics__ The authors point out that it isn't necessary to initialize the generated image to random noise.  Instead, the content image could be the initialization.  In this case there will be one unique generate image (assuming there's a fixed random seed on the objective solver), whereas using a random initialization allows for possibly different generated images to be found.
