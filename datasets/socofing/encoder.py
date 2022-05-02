import os
import tensorflow as tf
from .socofing import SOCOfing

class SOCOFingEncoder(SOCOfing):

    def __init__(self, **kwargs):
        SOCOfing.__init__(
            self, 
            name='SOCOFingEncoder', 
            **kwargs
            )
    
    def getLabel(self, pathFile):
        img = tf.io.read_file(pathFile)
        # Convert the compressed string to a 3D uint8 tensor
        img = tf.io.decode_bmp(img, channels=3)
        # Resize the image to the desired size
        img = tf.image.resize(img, self.inputDim[0:2])
        return tf.cast(img, dtype=tf.uint8, name=None)

