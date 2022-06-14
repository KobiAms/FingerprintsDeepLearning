from .backbone import FPBackbone
import tensorflow as tf


class MobileNet(FPBackbone):
    def __init__(self, inputDim=(224, 224, 3), weights=None, trainable=True, name="MobileNetV2-Backbone") -> None:
        FPBackbone.__init__(self,
                            name=name, 
                            backbone=tf.keras.applications.MobileNetV2, 
                            inputDim=inputDim, weights=weights, 
                            trainable=trainable
                            )
        
        
        
    