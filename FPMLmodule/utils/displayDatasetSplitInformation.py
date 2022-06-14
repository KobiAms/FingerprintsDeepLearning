import matplotlib.pyplot as plt
import numpy as np
import csv
from FPMLmodule.utils import displayDsSplit, datasetDistribution, displayGroupedBar

def displayDatasetSplitInformation(datasets, classNames=None, savePath=None, labels=['Train', 'Test', 'Validation']):
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    displayDsSplit(datasets)
    dist = np.array([datasetDistribution(ds) for ds in datasets])
    if savePath:
        f = open(savePath+'DatasetSplitInformation.csv', 'w')
        writer = csv.writer(f)
        if classNames:
            writer.writerow(['',*classNames,'SUM'])
        for dsName, dsDist in zip(labels, dist):
            row = [dsName, *dsDist, np.sum(dsDist)]
            writer.writerow(row)
        writer.writerow(['SUM', *np.sum(dist, axis=0), np.sum(dist)])
        f.close()
    plt.subplot(1, 2, 2)
    displayGroupedBar(dist.T, labels=labels, classes=classNames)
    if savePath:
        plt.savefig(savePath+'DatasetSplitInformation.png', bbox_inches='tight')
        plt.close()
    plt.show()