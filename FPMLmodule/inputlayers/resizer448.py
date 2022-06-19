import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models


from .inputlayer import FPInputLayer


class Resizer448(FPInputLayer):
    
    def __init__(self):
        FPInputLayer.__init__(self, name='Resizer')


    def create(self):
        model = models.Sequential(name=self.name)
        model.add(layers.Flatten())
        model.add(layers.Dense(4096, activation='relu'))
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(4096, activation='relu'))
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(self.nbClasses, activation=self.activation))
        return model