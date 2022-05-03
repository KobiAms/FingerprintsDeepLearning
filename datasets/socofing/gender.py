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
    
    
    def create(self):
        # create datasets to hold images path for male and female
        PATH = '{}{}/*__{}_*.BMP'
        pathFemale = PATH.format(os.getcwd(), self.path[1:], 'F')
        pathMale = PATH.format(os.getcwd(), self.path[1:], 'M')
        dsFemale = tf.data.Dataset.list_files(pathFemale, shuffle=False)
        dsMale = tf.data.Dataset.list_files(pathMale, shuffle=False)
        
        if self.split:
            dsFemale = self.splitDatasetByRatio(dsFemale, self.split)
            dsMale = self.splitDatasetByRatio(dsMale, self.split)
        
        datasets = []
        for dsf, dsm in zip(dsFemale, dsMale):
            if self.sampling != SOCOfing.NOT_SAMPLING:
                dsf, dsm = self.makeSampling(dsf, dsm)
            dsb = dsf.concatenate(dsm)
            if self.shuffle:
                shuffleBS = len(dsb)
            else:
                shuffleBS =1
            dsb = dsb.map(self.proccessPath)
            dsb = self.configureForPerformance(dsb, self.batchSize, shuffleBS)
            datasets.append(dsb)
        return datasets
        


    