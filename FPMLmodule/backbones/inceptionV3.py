from .backbone import FPBackbone
import tensorflow as tf


class InceptionV3(FPBackbone):
    def __init__(self, inputDim=(224, 224, 3), weights=None, trainable=True, name="InceptionV3-Backbone") -> None:
        FPBackbone.__init__(self,
                            name=name,
                            backbone=tf.keras.applications.inception_v3.InceptionV3,
                            inputDim=inputDim, weights=weights,
                            trainable=trainable
                            )
