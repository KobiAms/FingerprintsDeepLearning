import os
import tensorflow as tf
import numpy as np

class FPDataset:
    
    [NOT_SAMPLING, OVER_SAMPLING, UNDER_SAMPLING] = range(3)

    def __init__(self, name, path, inputDim, sampling=NOT_SAMPLING, split=None, batchSize=1, parallelTune=tf.data.AUTOTUNE, classNames=None, seed=9, shuffle=False):
        self.name = name        
        self.path = path        
        self.inputDim = inputDim        
        self.sampling = sampling        
        self.split = split        
        self.batchSize = batchSize        
        self.parallelTune = parallelTune        
        self.classNames = classNames        
        self.seed = seed        
        self.shuffle = shuffle        

    def getLabel(self):
        raise NotImplementedError

    def getFile(self, pathFile):
        raise NotImplementedError
    
    def proccessPath(self, pathFile):
        label = self.getLabel(pathFile)
        file = self.getFile(pathFile)
        return file, label
    
    def configureForPerformance(self, ds, batchSize, shuffleBS=1):
        ds = ds.cache()
        ds = ds.shuffle(buffer_size=shuffleBS)
        ds = ds.batch(batchSize)
        ds = ds.prefetch(buffer_size=self.parallelTune)
        return ds
    
    def create(self):
        raise NotImplementedError
    
    def makeSampling(self, dsBigger, dsSmaller):
        dsBiggerLen = len(dsBigger)
        dsSmallerLen = len(dsSmaller)
        swapped = False
        # replace bigger and smaller if needed
        if dsBiggerLen < dsSmallerLen:
            swapped = True
            tmp = dsBigger 
            dsBigger = dsSmaller
            dsSmaller = tmp
            tmp = dsBiggerLen
            dsBiggerLen = dsSmallerLen
            dsSmallerLen = tmp
        # repeat smaller for over sampling
        if self.sampling == self.OVER_SAMPLING:
            nbRepeat = np.ceil(dsBiggerLen/dsSmallerLen)
            dsSmaller = dsSmaller.repeat(nbRepeat)
            dsSmaller = dsSmaller.take(dsBiggerLen)
        # cut bigger for under sampling
        elif self.sampling == self.UNDER_SAMPLING:
            dsBigger = dsBigger.take(dsSmallerLen)
        
        if swapped:
            return dsSmaller, dsBigger
        return dsBigger, dsSmaller


