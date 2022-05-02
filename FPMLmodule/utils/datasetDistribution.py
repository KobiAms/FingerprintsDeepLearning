import numpy as np

def datasetDistribution(dataset):
    batchDistribution = []
    for _, labels in dataset:
        batchDistribution.append(labels.numpy().sum(axis=0))
    return np.array(batchDistribution).sum(axis=0)