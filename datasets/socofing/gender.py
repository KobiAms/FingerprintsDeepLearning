import os
import tensorflow as tf
from datasets.dataset import FPDataset 

class SOCOFingGender(FPDataset):

    def __init__(self, path='./data/socofing', subDS=['train', 'test', 'validation'], inputDim=(180, 180, 3), seed=9):
        FPDataset.__init__(self, 'SOCOFingGender', path, subDS=subDS, imgFormat='BMP', inputDim=inputDim, classNames=['F', 'M'],seed=seed)
    
    def getLabel(self, pathFile):
        # Convert the path to a list of path components
        fileName = tf.strings.split(pathFile, os.path.sep)[-1]
        className = tf.strings.split(fileName, '_')[2]  
        # The second to last is the class-directory
        one_hot = className == self.classNames
        # Integer encode the label
        # return tf.argmax(one_hot)
        return tf.cast(one_hot, dtype=tf.int8, name=None)


    