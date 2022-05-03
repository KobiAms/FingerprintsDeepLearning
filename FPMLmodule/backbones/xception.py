from .backbone import FPBackbone
import tensorflow as tf


class Xception(FPBackbone):
    def __init__(self, inputDim=(224, 224, 3), weights=None, trainable=True) -> None:
        FPBackbone.__init__(self,
                            name="Xception-Backbone",
                            backbone=tf.keras.applications.xception.Xception,
                            inputDim=inputDim, weights=weights,
                            trainable=trainable
                            )
