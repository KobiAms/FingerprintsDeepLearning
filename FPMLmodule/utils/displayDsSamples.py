import numpy as np
from matplotlib import pyplot as plt

def displayDatasetSamples(dataset, title='', shape=(1, 1), classNames=None):
  plt.figure(figsize=(8,10))
  plt.suptitle(title)
  rows, cols = shape
  numOfImages = rows*cols
  
  i=1
  for image, label in dataset:
    for image, label in zip(image, label):
      plt.subplot(rows, cols, i)
      plt.axis('off')
      plt.imshow(image, cmap='gray')
      parseLabel = label
      if classNames:
        parseLabel = classNames[np.argmax(parseLabel)]
      plt.title(parseLabel, fontsize=16)
      if i==numOfImages:
        break
      i+=1
  plt.tight_layout()
  plt.subplots_adjust(wspace=0.1, hspace=0.1)
  plt.show()