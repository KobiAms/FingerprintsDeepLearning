import os
import tensorflow as tf
from .nistsdb302b import NISTSDB302b


class NISTSDB302bFingers(NISTSDB302b):

    def __init__(self, **kargs):
        NISTSDB302b.__init__(
            self, 
            name='NISTSDB302bFingers',
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
        label = tf.strings.split(fileName, '_')[-1]
        className = tf.strings.regex_replace(label, '.png', '')
        # The second to last is the class-directory
        one_hot = className == self.classNames
        # Integer encode the label
        return tf.cast(one_hot, dtype=tf.int8, name=None)