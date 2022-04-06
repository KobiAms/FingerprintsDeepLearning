import os
import tensorflow as tf
from .socofing import SOCOfing



class SOCOFingSubjects(SOCOfing):
    
    def __init__(self, **kargs):
        SOCOfing.__init__(
            self, 
            name='SOCOfingSubjects', 
            **kargs
            )
    
    def getLabel(self, pathFile):
        # Convert the path to a list of path components
        fileName = tf.strings.split(pathFile, os.path.sep)[-1]
        className = tf.strings.split(fileName, '_')[0]  
        return className

