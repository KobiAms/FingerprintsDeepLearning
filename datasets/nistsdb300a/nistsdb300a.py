import os
from datasets.dataset import FPDataset 
import tensorflow as tf
import numpy as np


class NISTSDB300a(FPDataset):

    def __init__(
        self,  
        path='./data/NISTSDB300a/500/png/roll', 
        name='NISTSDB300a', 
        inputDim=(500, 500, 3), 
        **kargs
        ):
        FPDataset.__init__(self, name=name, path=path, inputDim=inputDim, **kargs)

    def getFile(self, pathFile):
        # Load the raw data from the file as a string
        img = tf.io.read_file(pathFile)
        # Convert the compressed string to a 3D uint8 tensor
        img = tf.io.decode_png(img, channels=3)
        # Resize the image to the desired size
        img = tf.image.resize(img, self.inputDim[0:2])
        return tf.cast(img, dtype=tf.uint8, name=None)
    
    # calculates the actual sizes of splitted datasets by ratio, divide by 10 to force different subjects in each dataset
    def samplesByRatio(self, nbSamples, ratio):
        nbSubjects = nbSamples/10
        ratio = np.array(ratio)
        splits = nbSubjects*ratio//1
        splitSum = splits.sum()
        if splitSum < nbSubjects:
            splits[0]+=(nbSubjects-splitSum)
        splits*=10
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
        PATH = '{}{}/*.png'
        path = PATH.format(os.getcwd(), self.path[1:])
        dsf = tf.data.Dataset.list_files(path, shuffle=False)
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