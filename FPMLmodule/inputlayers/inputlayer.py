

class FPInputLayer:
    def __init__(self, name, activation) -> None:
        self.name = name
        self.activation = activation
        
    def create(self):
        raise NotImplementedError
    
