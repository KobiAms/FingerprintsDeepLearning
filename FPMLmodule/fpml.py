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
        self.history = None
    
    def create(self, optimizer, learningRate, loss, metrics):
        model = models.Sequential()
        if self.inputLayer:
            model.add(self.inputLayer.create())
        model.add(self.backbone.create())
        model.add(self.classifier.create())
        model.build((None, *self.inputDim))
        model.compile(optimizer=optimizer(learning_rate=learningRate),loss=loss,metrics=[metrics])
        self.model = model
        return model
    
    def getModel(self):
        if not self.model:
            print('model not created. please call create()')
            return None
        return self.model
    
    def getHistory(self):
        if not self.history:
            print('model not trained. please call fit()')
            return None
        return self.history
        
    def fit(self, trainSet, validation_data, epochs, verbose):
        if not self.model:
            print('model not created. please call create()')
            return None
        history = self.model.fit(trainSet, validation_data=validation_data, epochs=epochs, verbose=verbose)
        if self.history:
            self.history = [*self.history, history]
        else:
            self.history = [history]
        return history
    
    def save(self, path):
        if not self.model:
            print('model not created. please call create()')
        else:
            self.model.save(path)
    
     