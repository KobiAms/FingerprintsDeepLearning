from .classifier import FPClassifier
from tensorflow.keras import layers, models

class ResNetClassifier(FPClassifier):
    
    def __init__(self, nbClasses, activation) -> None:
        super().__init__("ResNet-Classifier", nbClasses=nbClasses, activation=activation)
        
    def create(self):
        model = models.Sequential(name=self.name)
        model.add(layers.Flatten())
        model.add(layers.Dense(self.nbClasses, activation=self.activation))
        return model