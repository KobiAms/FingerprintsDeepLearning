from .backbone import FPBackbone
import tensorflow as tf


class EncoderV1(FPBackbone):
    def __init__(self, inputDim, weights=None, trainable=True) -> None:
        FPBackbone.__init__(self, 
                            name="Encoder-Backbone", 
                            backbone=tf.keras.applications.ResNet50, 
                            inputDim=inputDim, weights=weights, 
                            trainable=trainable
                            )
        