import numpy as np
from matplotlib import pyplot as plt

def displayGroupedBar(data, yLabel='Number of examples', title='Datasets Distribution', labels=None, classes=None):
    if not classes:
        classes = np.arange(data.shape[0])    
    n = len(data)
    _X = np.arange(data.shape[1])
    width=0.8
    for i in range(n):
        plt.bar(_X - width/2. + i/float(n)*width, data[i], width=width/float(n))
    if labels:  
        plt.xticks(_X-width/(data.shape[0]*2), labels)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend(classes)  