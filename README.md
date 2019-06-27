# Tensorflow Tutorials

All my files for *Creative Applications of Deep Learning with Tensorflow*, an online course on [Kadenze][kadenze].

## Overview

The Kadenze course "creative applications of deep learning in TensorFlow" is a great MOOC to learn the TensorFlow framework and manipulate fascinating neural network architectures, which has been a great opportunity to develop my burgeoning creative skills.

The following manifold has been generated during the course with the dataset of my choice ([latent space][fastforward-vae]):

![Galaxy Zoo manifold][galaxy-manifold]

The Galaxy Zoo dataset is not expressive enough, so the visual and artistic impact is not as good as expected. Nevertheless, you can perfectly observe relevant variations of galaxy shape, sharpness, orientation, existence of stars in the field, etc.

For the project, I came to play around with generative hand writing (see below for full credits on inspiration and external code use). After a training on human hand writing, the code is able to generate a kind of [ansemic writing][wikipedia-asemic]:

![Generative hand writing][glyphs-rnn]

## Installation and setup

On OS X, download the Anaconda [installation script][continuum-download] for Python 3.5 and follow the Continuum instructions. Then, install TensorFlow:

````
$ conda create -n tensorflow python=3.5
$ source activate tensorflow
(tensorflow)$ conda install ipykernel
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc1-py3-none-any.whl
(tensorflow)$ pip install --upgrade --ignore-installed $TF_BINARY_URL
````

## Contribution

Contributions are not accepted for this project.

## Credits and license

+ the main credits go to [Parag Mital][pkmital] and [Kadenze][kadenze], all materials are distributed under the Apache license v2.0 and the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license
+ the assignments come from the [CADL GitHub repository][github-cadl], you can find in this repository amazing code, like a ready-to-use VAE/GAN net (strong computing power will be required to train it by yourself)
+ the course heavily relies on the [CelebFaces Attributes Dataset][mmlab-celeba]

[fastforward-vae]: http://blog.fastforwardlabs.com/post/148842796218/introducing-variational-autoencoders-in-prose-and
[wikipedia-asemic]: https://en.wikipedia.org/wiki/Asemic_writing
[cadl-install]: https://github.com/pkmital/CADL#what-is-notebook
[continuum-download]: https://www.continuum.io/downloads#_macosx
[pkmital]: https://github.com/pkmital
[kadenze]: https://www.kadenze.com/
[github-cadl]: https://github.com/pkmital/CADL

[galaxy-manifold]: /assets/img/manifold-galaxy.png "Galaxy Zoo manifold"
[glyphs-rnn]: /assets/img/glyphs-rnn.png "Generative hand writing"
