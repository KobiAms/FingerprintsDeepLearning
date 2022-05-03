from datasets import SOCOFingGender
from FPMLmodule.backbones import ResNet50
from FPMLmodule.classifiers import ResNetClassifier
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

dsConfig = {
    'batchSize': batch_size, 
    'parallelTune': AUTOTUNE, 
    'split': split_ratio, 
    'inputDim': img_dim, 
    'seed': seed, 
    'shuffle': shuffle
    }

weights = "./weights/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5"

# Model Config
learning_rate = 0.001
epochs_find_best = 10
epochs_best = 100

genderClassNames=['F','M']

train_set, test_set, val_set = SOCOFingGender(**dict(dsConfig, sampling=SOCOFingGender.UNDER_SAMPLING)).create()
rn50 = ResNet50(img_dim, weights=weights, trainable=False)
rnc = ResNetClassifier(2, "softmax")

model = FPML(rn50, rnc, "", img_dim).create("adam", learning_rate, 'binary_crossentropy', 'accuracy')
model_history = model.fit(train_set, validation_data=val_set, epochs=10)

# {"model" : model, "history": model_history}