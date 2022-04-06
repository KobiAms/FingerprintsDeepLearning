import os
from datasets.dataset import FPDataset 
import tensorflow as tf
import numpy as np

class SOCOfing(FPDataset):

    def __init__(
        self,  
        path='./data/SOCOFing/Real', 
        name='SOCOFing', 
        inputDim=(180, 180, 3), 
        **kargs
        ):
        FPDataset.__init__(self, name=name, path=path, imgFormat='BMP', inputDim=inputDim, **kargs)       

    def getFile(self, pathFile):
        # Load the raw data from the file as a string
        img = tf.io.read_file(pathFile)
        # Convert the compressed string to a 3D uint8 tensor
        img = tf.io.decode_bmp(img, channels=3)
        # Resize the image to the desired size
        img = tf.image.resize(img, self.inputDim[0:2])
        return tf.cast(img, dtype=tf.uint8, name=None)
    
    
    def samplesByRatio(self, nbSamples, ratio):
        nbSubjects = nbSamples/10
        ratio = np.array(ratio)
        splits = nbSubjects*ratio//1
        splitSum = splits.sum()
        if splitSum < nbSubjects:
            splits[0]+=(nbSubjects-splitSum)
        splits*=10
        return splits
    

    def createDatasets(self, splitsRatio=None, shuffle=False):
        PATH = '{}{}/*.{}'
        path = PATH.format(os.getcwd(), self.path[1:],self.imgFormat)
        ds = tf.data.Dataset.list_files(path, shuffle=False)
        nbSamples = len(ds)
        if splitsRatio:
            splitsAcc = self.samplesByRatio(nbSamples, splitsRatio)
            tok = 0
            datasets = []
            for a in splitsAcc:
                dsf = ds.take(tok+a).skip(tok)
                tok+=a
                if shuffle:
                    dsf  = dsf.shuffle(buffer_size=len(dsf), seed=self.seed)
                dsf = dsf.map(self.proccessPath, num_parallel_calls=tf.data.AUTOTUNE)
                datasets.append(dsf)   
        else:
            if shuffle:
                ds = ds.shuffle(buffer_size=nbSamples*2, seed=self.seed)
            datasets = ds.map(self.proccessPath, num_parallel_calls=tf.data.AUTOTUNE)
        return datasets
