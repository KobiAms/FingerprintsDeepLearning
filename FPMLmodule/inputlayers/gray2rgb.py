
from .inputlayer import FPInputLayer

NAME='inputLayer-gray2rgb'

class FPILgray2rgb(FPInputLayer):
    
    def __init__(self, inputDim, outputDim):
        FPInputLayer.__init__(self, name=NAME, inputDim=inputDim, outputDim=outputDim)
