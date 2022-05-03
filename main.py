from FPMLmodule.inputlayers import FPILgray2rgb
from FPMLmodule.backbones import ResNet50
from FPMLmodule.classifiers import ResNetClassifier

from datasets import SOCOFingGender
from FPMLmodule.fpml import FPML

import tensorflow as tf


# Global Config
seed=9
img_dim = (120, 120, 3)
img_height, img_width, img_channels = img_dim
batch_size = 32

# Dataset configuration
AUTOTUNE = tf.data.AUTOTUNE
split_ratio = [0.7, 0.15, 0.15]
shuffle=True

dsConfig = {'batchSize': batch_size, 'parallelTune': AUTOTUNE, 'split': split_ratio, 'inputDim': img_dim, 'seed': seed, 'shuffle': shuffle}
SOCOGender = SOCOFingGender(**dict(dsConfig, sampling=SOCOFingGender.UNDER_SAMPLING))


# genderDS = SOCOGender.create()

print("Hello Fingerprints Module")


# g2rgb = FPILgray2rgb((96, 103), (180, 180, 3))
# rnbb = ResNet50()
# rnc = ResNetClassifier(2, "softmax")

# fpml = FPML(g2rgb, rnbb, rnc, None)

# print(g2rgb.getName())
# print(rn50.getName())