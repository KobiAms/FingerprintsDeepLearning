import os
from random import seed
import tensorflow as tf
import numpy as np
from .socofing import SOCOfing

class SOCOFingGender(SOCOfing):

    def __init__(self, **kargs):
        SOCOfing.__init__(
            self, 
            name='SOCOfingGender', 
            classNames=['F', 'M'],
            **kargs
            )
    
    def getLabel(self, pathFile):
        # Convert the path to a list of path components
        fileName = tf.strings.split(pathFile, os.path.sep)[-1]
        className = tf.strings.split(fileName, '_')[2]  
        # The second to last is the class-directory
        one_hot = className == self.classNames
        # Integer encode the label
        return tf.cast(one_hot, dtype=tf.int8, name=None)
        
    
    def createDatasets(self, splitsRatio=None, overSampling=False, shuffle=False):
        
        PATH = '{}{}/*__{}_*.{}'
        pathF = PATH.format(os.getcwd(), self.path[1:], 'F',self.imgFormat)
        pathM = PATH.format(os.getcwd(), self.path[1:], 'M',self.imgFormat)
        dsF = tf.data.Dataset.list_files(pathF, shuffle=False)
        dsM = tf.data.Dataset.list_files(pathM, shuffle=False)
        nbSamples = min(len(dsF), len(dsM))
        
        if overSampling:
            nbRepeat = np.ceil(len(dsM)/len(dsF))
            dsF = dsF.repeat(nbRepeat)
            dsF = dsF.take(len(dsM))
            nbSamples = len(dsF)
        
        if splitsRatio:
            splitsAcc = self.samplesByRatio(nbSamples, splitsRatio)
            tok = 0
            datasets = []
            for a in splitsAcc:
                dsf = dsF.take(tok+a).skip(tok)
                dsm = dsM.take(tok+a).skip(tok)
                tok+=a
                ds = dsf.concatenate(dsm)
                if shuffle:
                    ds = ds.shuffle(buffer_size=len(ds)*2, seed=self.seed)
                ds = ds.map(self.proccessPath, num_parallel_calls=tf.data.AUTOTUNE)
                datasets.append(ds)   
        else:
            ds = dsF.concatenate(dsM.take(nbSamples))
            if shuffle:
                ds = ds.shuffle(buffer_size=nbSamples*2, seed=self.seed)
            datasets = ds.map(self.proccessPath, num_parallel_calls=tf.data.AUTOTUNE)
        return datasets


    