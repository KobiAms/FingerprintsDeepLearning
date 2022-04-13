from .backbones.backbone import FPBackbone
from .inputlayers.inputlayer import FPInputLayer
from .classifiers.classifier import FPClassifier
from tensorflow.keras import models


DEFAULT_CONFIG = {}

class FPML:
    
    def __init__(self, backbone, classfier, config, inputDim, inputLayer=None) -> None:
        
        if inputLayer and not issubclass(type(inputLayer), FPInputLayer):
            raise SystemError('inputLayer type error')
        if not issubclass(type(backbone), FPBackbone):
            raise SystemError('backbone type error')
        if not issubclass(type(classfier), FPClassifier):
            raise SystemError('classfier type error')
        
        self.inputLayer = inputLayer
        self.backbone = backbone
        self.classfier = classfier
        self.config = config
        self.inputDim = inputDim
        self.model = None
    
    def createModel(self, optimizer, learningRate, loss, metrics):
        model = models.Sequential()
        if self.inputLayer:
            model.add(self.inputLayer.createInputLayer())
        model.add(self.backbone.createBackbone())
        model.add(self.classfier.createClassifier())
        model.build((None, *self.inputDim))
        model.compile(optimizer=optimizer(learning_rate=learningRate),loss=loss,metrics=[metrics])
        return model
        
    # def train(self, trainSet, valSet, epochs):
    #     history = self.model.fit(trainSet, validation_data=valSet, epochs=epochs)
    #     return history
    
     