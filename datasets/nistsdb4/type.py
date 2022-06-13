import tensorflow as tf
import numpy as np
from .nistsdb4 import NISTSDB4

class NISTSDB4Type(NISTSDB4):

    def __init__(self, **kargs):
        NISTSDB4.__init__(
            self, 
            name='NISTSDB4Type', 
            classNames=['L', 'W', 'R', 'T', 'A'], # L = left loop, W = whirl, R = right loop, T = tented arch, and A = arch
            **kargs
            )
     
    def getLabel(self, pathFile):
        # Convert the file path to metadata file path
        fileName = tf.strings.regex_replace(pathFile, 'png_txt', '-&%&-')
        fileName = tf.strings.regex_replace(fileName, '.png', '.txt')
        fileName = tf.strings.regex_replace(fileName, '-&%&-', 'png_txt')
        # read metadata and get label
        file = tf.io.read_file(fileName)
        label = tf.strings.split(file, '\n')[1]
        label = tf.strings.regex_replace(label, 'Class: ', '')
        one_hot = label == self.classNames
        return tf.cast(one_hot, dtype=tf.int8, name=None)
    