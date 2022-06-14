from .backbone import FPBackbone
import tensorflow as tf


class Xception(FPBackbone):
    def __init__(self, inputDim=(224, 224, 3), weights=None, trainable=True, name="Xception-Backbone") -> None:
        FPBackbone.__init__(self,
                            name=name,
                            backbone=tf.keras.applications.xception.Xception,
                            inputDim=inputDim, weights=weights,
                            trainable=trainable
                            )
