import numpy as np
from matplotlib import pyplot as plt

def displayDatasetSplit(dataset, splitNames=['train', 'test ', 'validation']):
    
    lens = []
    for part in dataset:
        tempLen = 0
        for _, labels in part.as_numpy_iterator():
            tempLen+=len(labels)
        lens.append(tempLen)
    
    print(lens)
    lens = np.array(lens)
    plt.figure(figsize=(7,7), facecolor='white')
    plt.pie(lens, labels = splitNames[:len(dataset)], autopct=lambda x: "{}".format(int(np.round(x*lens.sum()/100))))
    plt.show()