

class FPBackbone:
    
    def __init__(self, name, backbone=None, inputDim=None, weights=None, trainable=True) -> None:
        self.name = name
        self.backbone = backbone
        self.inputDim = inputDim
        self.weights = weights
        self.trainable = trainable
        
    def createBackbone(self, pooling="max"):
        backbone = self.backbone(include_top=False, input_shape=self.inputDim, pooling=pooling, weights=self.weights)
        if not self.trainable:
            for layer in backbone.layers:
                layer.trainable=False
        return backbone