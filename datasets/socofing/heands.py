import os
import tensorflow as tf
from .socofing import SOCOfing

class SOCOFingHeands(SOCOfing):

    def __init__(self, **kargs):
        SOCOfing.__init__(
            self, 
            name='SOCOfingHeands',
            classNames=[
                'Right',
                'Left'
            ], 
            **kargs
            )
    
    def getLabel(self, pathFile):
        # Convert the path to a list of path components
        fileName = tf.strings.split(pathFile, os.path.sep)[-1]
        className = tf.strings.regex_replace(fileName, '[0-9]+__[F,M]_', '')
        className = tf.strings.regex_replace(className, '_[a-z]+_finger.BMP', '')
        # The second to last is the class-directory
        one_hot = className == self.classNames
        # Integer encode the label
        return tf.cast(one_hot, dtype=tf.int8, name=None)