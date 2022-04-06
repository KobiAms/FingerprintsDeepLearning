from datasets.socofing import SOCOFingGender, SOCOFingFingers, SOCOFingSubjects
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf

print("Tensorflow version " + tf.__version__)


genderClassNames=[
            'F',
            'M'
            ]
fingersClassNames=[
            'R_thumb',
            'R_index',
            'R_middle',
            'R_ring',
            'R_little',
            'L_thumb',
            'L_index',
            'L_middle',
            'L_ring',
            'L_little'
            ]


SOCOGender = SOCOFingGender()
SOCOSubjects = SOCOFingSubjects()
SOCOFingers = SOCOFingFingers()

genderDS = SOCOGender.createDatasets(splitsRatio=[0.7, 0.15, 0.15], shuffle=True, sampling=SOCOFingers.UNDER_SAMPLING)
subjectDS = SOCOSubjects.createDatasets(splitsRatio=[0.7, 0.15, 0.15], shuffle=True)
fingersDS = SOCOFingers.createDatasets(splitsRatio=[0.7, 0.15, 0.15], shuffle=True)

dsNames = ['SOCOGender  ', 'SOCOSubjects', 'SOCOFingers ']
splitNames = ['train', 'test ', 'valid']
datasets = [genderDS, subjectDS, fingersDS]

data = []
for ds in datasets:
    data.append([len(i) for i in ds])

row_format ="{:>15}" * (len(dsNames) + 2)
print(row_format.format("", *splitNames, 'total'))
for name, row in zip(dsNames, data):
    print(row_format.format(name, *row, np.sum(row)))

# def display_images_from_dataset(dataset, title='', numOfImages=10, cNames=None):
#   plt.figure(figsize=(13,13))
#   plt.suptitle(title)
#   rows = int(np.ceil(numOfImages/10))
#   for i, (image, label) in enumerate(dataset):
#     plt.subplot(rows, 10, i+1)
#     plt.axis('off')
#     plt.imshow(image, cmap='gray')
#     parseLabel = label.numpy()
#     if cNames:
#       parseLabel = cNames[tf.argmax(parseLabel)]
#     plt.title(str(parseLabel), fontsize=16)
#     if i==numOfImages-1:
#       break
#   plt.tight_layout()
#   plt.subplots_adjust(wspace=0.1, hspace=0.1)
#   plt.show()

# display_images_from_dataset(dsF, 'Gender - Female')