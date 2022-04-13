
class FPClassifier:
    def __init__(self, name, nbClasses, activation) -> None:
        self.name = name
        self.nbClasses = nbClasses
        self.activation = activation
        
    def createClassifier(self):
        raise NotImplementedError