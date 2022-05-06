import matplotlib.pyplot as plt
import numpy as np
from FPMLmodule.utils import displayDsSplit, datasetDistribution, displayGroupedBar

def displayDatasetSplitInformation(datasets, classNames=None):
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    displayDsSplit(datasets)
    dist = np.array([datasetDistribution(ds) for ds in datasets]).T
    plt.subplot(1, 2, 2)
    displayGroupedBar(dist, labels=['Train', 'Test', 'Validation'], classes=classNames)
    plt.show()