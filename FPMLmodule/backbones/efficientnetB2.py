from .backbone import FPBackbone
import tensorflow as tf


class EfficientNetB2(FPBackbone):
    def __init__(self, inputDim=(224, 224, 3), weights=None, trainable=True) -> None:
        FPBackbone.__init__(self,
                            name="EfficientNetB2-Backbone",
                            backbone=tf.keras.applications.efficientnet.EfficientNetB2,
                            inputDim=inputDim, weights=weights,
                            trainable=trainable
                            )
