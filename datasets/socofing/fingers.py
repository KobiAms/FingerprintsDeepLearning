import os
import tensorflow as tf
from datasets.dataset import FPDataset

class SOCOFingFingers(FPDataset):

    def __init__(self, path='./data/socofing', subDS=['train', 'test', 'validation'], inputDim=(180, 180, 3), seed=9):
        classNames=[
            'Right_thumb',
            'Right_index',
            'Right_middle',
            'Right_ring',
            'Right_little',
            'Left_thumb',
            'Left_index',
            'Left_middle',
            'Left_ring',
            'Left_little'
        ]
        FPDataset.__init__(self, 'SOCOFingFingers', path, subDS=subDS, imgFormat='BMP', inputDim=inputDim, classNames=classNames, seed=seed)
    
    def getLabel(self, pathFile):
        # Convert the path to a list of path components
        fileName = tf.strings.split(pathFile, os.path.sep)[-1]
        className = tf.strings.regex_replace(fileName, '[0-9]+__[F,M]_', '')
        className = tf.strings.regex_replace(className, '_finger.BMP', '')
        # The second to last is the class-directory
        one_hot = className == self.classNames
        # Integer encode the label
        return tf.cast(one_hot, dtype=tf.int8, name=None)