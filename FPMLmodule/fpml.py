from .backbones.backbone import FPBackbone
from .inputlayers.inputlayer import FPInputLayer
from .classifiers.classifier import FPClassifier
from tensorflow.keras import models


DEFAULT_CONFIG = {}

class FPML:
    
    def __init__(self, backbone, classifier, inputDim, config=None, inputLayer=None) -> None:
        
        if inputLayer and not issubclass(type(inputLayer), FPInputLayer):
            raise SystemError('inputLayer type error')
        if not issubclass(type(backbone), FPBackbone):
            raise SystemError('backbone type error')
        if not issubclass(type(classifier), FPClassifier):
            raise SystemError('classifier type error')
        
        self.inputLayer = inputLayer
        self.backbone = backbone
        self.classifier = classifier
        self.config = config
        self.inputDim = inputDim
        self.model = None
    
    def create(self, optimizer, learningRate, loss, metrics):
        model = models.Sequential()
        if self.inputLayer:
            model.add(self.inputLayer.create())
        model.add(self.backbone.create())
        model.add(self.classifier.create())
        model.build((None, *self.inputDim))
        model.compile(optimizer=optimizer(learning_rate=learningRate),loss=loss,metrics=[metrics])
        return model
        
    # def train(self, trainSet, valSet, epochs):
    #     history = self.model.fit(trainSet, validation_data=valSet, epochs=epochs)
    #     return history
    
     