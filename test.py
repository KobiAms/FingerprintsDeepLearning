import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.optimizers import Adam

from datasets import SOCOFingGender
from FPMLmodule.backbones import ResNet50
from FPMLmodule.classifiers import ResNetClassifier
from FPMLmodule.fpml import FPML 


# Global Config
seed=9
img_dim = (96, 103, 3)
img_height, img_width, img_channels = img_dim
batch_size = 32

# Dataset configuration
AUTOTUNE = tf.data.AUTOTUNE
split_ratio = [0.7, 0.15, 0.15]
shuffle=True
weights = "./weights/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5"

# Train config
learning_rate = 0.001

dsConfig = {
    'batchSize': batch_size, 
    'parallelTune': AUTOTUNE, 
    'split': split_ratio, 
    'inputDim': img_dim, 
    'seed': seed, 
    'shuffle': shuffle
    }

SOCOGender = SOCOFingGender(**dict(dsConfig, sampling=SOCOFingGender.UNDER_SAMPLING))

train_ds, test_ds, val_ds = SOCOGender.create()


rn50 = ResNet50(img_dim, weights=weights, trainable=False)
rnc = ResNetClassifier(2, "softmax")

fpml = FPML(rn50, rnc, "", img_dim)

model = fpml.create(Adam, learning_rate, 'binary_crossentropy', 'accuracy')

model_history = model.fit(train_ds, validation_data=val_ds, epochs=10)

