from .classifier import FPClassifier
from tensorflow.keras import layers, models

class MobileNetClassifier(FPClassifier):
    
    def __init__(self, nbClasses, activation) -> None:
        super().__init__("MobileNet-Classifier", nbClasses=nbClasses, activation=activation)
        
    def createClassifier(self):
        model = models.Sequential(name=self.name)
        model.add(layers.Flatten())
        model.add(layers.Dense(512, activation='relu'))
        model.add(layers.Dropout(0.4))
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dropout(0.3))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dropout(0.2))
        model.add(layers.Dense(self.nbClasses, activation=self.activation))
        return model