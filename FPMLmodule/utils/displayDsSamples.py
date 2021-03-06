import numpy as np
from matplotlib import pyplot as plt

def displayDatasetSamples(dataset, title='', shape=(1, 1), classNames=None, savePath=None):
  plt.figure(figsize=(10,2))
  plt.suptitle(title)
  rows, cols = shape
  numOfImages = rows*cols
  
  i=1
  for image, label in dataset:
    for image, label in zip(image, label):
      plt.subplot(rows, cols, i)
      plt.axis('off')
      plt.imshow(image, cmap='gray')
      
      if classNames:
        parseLabel = classNames[np.argmax(label)]
      else:
        parseLabel = label.numpy().decode('utf-8')
      plt.title(parseLabel, fontsize=16)
      if i==numOfImages:
        break
      i+=1
  plt.tight_layout()
  plt.subplots_adjust(wspace=0.1, hspace=0.1)
  if savePath:
    plt.savefig(savePath+'DatasetSamples.png', bbox_inches='tight')
    plt.close()
  else:   
    plt.show()