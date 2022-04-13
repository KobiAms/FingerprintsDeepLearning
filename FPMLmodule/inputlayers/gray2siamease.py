from .inputlayer import FPInputLayer

NAME='inputLayer-gray2siamease'

class FPILgray2siamease(FPInputLayer):
    
    def __init__(self, inputDim, outputDim):
        FPInputLayer.__init__(self, name=NAME, inputDim=inputDim, outputDim=outputDim)
        