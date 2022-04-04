import os
import tensorflow as tf

class FPDataset:

    def __init__(self, name, path, subDS, imgFormat, inputDim, classNames=None, seed=9):
        self.name = name        
        self.path = path        
        self.subDS = subDS                
        self.imgFormat = imgFormat                
        self.inputDim = inputDim        
        self.seed = seed        
        self.classNames = classNames        

    def getLabel(self):
        raise NotImplementedError

    def getFile(self, pathFile):
        # Load the raw data from the file as a string
        img = tf.io.read_file(pathFile)
        # Convert the compressed string to a 3D uint8 tensor
        img = tf.io.decode_bmp(img, channels=3)
        # Resize the image to the desired size
        img = tf.image.resize(img, self.inputDim[0:2])
        return tf.cast(img, dtype=tf.uint8, name=None)

    def proccessPath(self, pathFile):
        label = self.getLabel(pathFile)
        file = self.getFile(pathFile)
        return file, label

    def createDatasets(self):
        datasets = []
        for sub in self.subDS:
            path = '{}{}/{}/*.{}'.format(os.getcwd(), self.path[1:], sub, self.imgFormat)
            ds = tf.data.Dataset.list_files(path, shuffle=True, seed=self.seed)
            nb_images = len(tf.io.gfile.glob(path))
            print("create '{} - {}' dataset with {} samples.".format(self.name, sub, nb_images))
            ds = ds.map(self.proccessPath, num_parallel_calls=tf.data.AUTOTUNE)
            datasets.append(ds)
        return datasets
