
import os
import tensorflow as tf
from .nistsdb300a import NISTSDB300a

class NISTSDB300aFingers(NISTSDB300a):

    def __init__(self, **kargs):
        NISTSDB300a.__init__(
            self, 
            name='SOCOfingFingers',
            classNames=[
                '01',
                '02',
                '03',
                '04',
                '05',
                '06',
                '07',
                '08',
                '09',
                '10'
            ], 
            **kargs
            )
    
    def getLabel(self, pathFile):
        # Convert the path to a list of path components
        fileName = tf.strings.split(pathFile, os.path.sep)[-1]
        label = tf.strings.split(fileName, '_')[3]
        className = tf.strings.regex_replace(label, '.png', '')
        # The second to last is the class-directory
        one_hot = className == self.classNames
        # Integer encode the label
        return tf.cast(one_hot, dtype=tf.int8, name=None)