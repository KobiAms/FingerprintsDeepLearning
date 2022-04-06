import os
import tensorflow as tf

class FPDataset:

    def __init__(self, name, path, imgFormat, inputDim, classNames=None, seed=9):
        self.name = name        
        self.path = path        
        self.imgFormat = imgFormat                
        self.inputDim = inputDim        
        self.seed = seed        
        self.classNames = classNames        

    def getLabel(self):
        raise NotImplementedError

    def createDatasets(self):
        raise NotImplementedError
    
    def getFile(self, pathFile):
        raise NotImplementedError

    def proccessPath(self, pathFile):
        label = self.getLabel(pathFile)
        file = self.getFile(pathFile)
        return file, label

