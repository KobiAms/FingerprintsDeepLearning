from .backbone import FPBackbone
import tensorflow as tf


class ResNet50(FPBackbone):
    def __init__(self, inputDim=(224, 224, 3), weights=None, trainable=True, name="ResNet50-Backbone") -> None:
        FPBackbone.__init__(self, 
                            name=name, 
                            backbone=tf.keras.applications.ResNet50, 
                            inputDim=inputDim, weights=weights, 
                            trainable=trainable
                            )
        
        
        
    