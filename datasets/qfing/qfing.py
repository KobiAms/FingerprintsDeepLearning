import os
from datasets.dataset import FPDataset 
import tensorflow as tf
import numpy as np

class QFing(FPDataset):

    def __init__(
        self,  
        path='./data/QFing', 
        name='QFing',
        classNames=[
                '0',
                '1',
                '2',
                '3',
                '4',
            ],
        inputDim=(1024, 700, 3), 
        **kargs
        ):
        FPDataset.__init__(self, name=name, path=path, inputDim=inputDim, classNames=classNames, **kargs)       

    def getFile(self, pathFile):
        # Load the raw data from the file as a string
        img = tf.io.read_file(pathFile)
        # Convert the compressed string to a 3D uint8 tensor
        img = tf.io.decode_jpeg(img, channels=3)
        # Resize the image to the desired size
        img = tf.image.resize(img, self.inputDim[0:2])
        return tf.cast(img, dtype=tf.uint8, name=None)
    
    def getLabel(self, pathFile):
        # Convert the path to a list of path components
        className = tf.strings.split(pathFile, os.path.sep)[-2]
        # The second to last is the class-directory
        one_hot = className == self.classNames
        # Integer encode the label
        return tf.cast(one_hot, dtype=tf.int8, name=None)
    
    # calculates the actual sizes of splitted datasets by ratio, divide by 10 to force different subjects in each dataset
    def samplesByRatio(self, nbSamples, ratio):
        ratio = np.array(ratio)
        splits = nbSamples*ratio//1
        splitSum = splits.sum()
        if splitSum < nbSamples:
            splits[0]+=(nbSamples-splitSum)
        return splits
    
    def splitDatasetByRatio(self, ds, splitsRatio):
        nbSamples = len(ds)
        dsSizes = self.samplesByRatio(nbSamples, splitsRatio)
        tok = 0
        datasetsSplitted = []
        for size in dsSizes:
            datasetsSplitted.append(ds.take(tok+size).skip(tok)) 
            tok+=size
        return datasetsSplitted
    

    def create(self):
        PATH = '{}{}/*/*.jpg'
        path = PATH.format(os.getcwd(), self.path[1:])
        dsf = tf.data.Dataset.list_files(path, shuffle=True)
        if self.split:
            dsf = self.splitDatasetByRatio(dsf, self.split)
        for i, ds in enumerate(dsf):
            if self.shuffle:
                shuffleBS = len(dsf[i])
            else:
                shuffleBS = 1
            dsf[i] = dsf[i].map(self.proccessPath)
            dsf[i] = self.configureForPerformance(dsf[i], self.batchSize, shuffleBS)
        return dsf
                
