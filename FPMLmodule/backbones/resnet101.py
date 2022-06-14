from .backbone import FPBackbone
import tensorflow as tf


class ResNet101(FPBackbone):
    def __init__(self, inputDim=(224, 224, 3), weights=None, trainable=True, name="ResNet101-Backbone") -> None:
        FPBackbone.__init__(self,
                            name=name,
                            backbone=tf.keras.applications.resnet.ResNet101,
                            inputDim=inputDim, weights=weights,
                            trainable=trainable
                            )
