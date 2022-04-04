import os
import tensorflow as tf
from datasets.dataset import FPDataset 

class SOCOFingSubjects(FPDataset):

    def __init__(self, path='./data/socofing', subDS=['train', 'test', 'validation'], inputDim=(180, 180, 3), seed=9):
        FPDataset.__init__(self, 'SOCOFingSubjects', path, subDS=subDS, imgFormat='BMP', inputDim=inputDim, seed=seed)
    
    def getLabel(self, pathFile):
        # Convert the path to a list of path components
        fileName = tf.strings.split(pathFile, os.path.sep)[-1]
        className = tf.strings.split(fileName, '_')[0]  
        return className

