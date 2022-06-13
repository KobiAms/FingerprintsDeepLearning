import os
import tensorflow as tf
from .nistsdb300a import NISTSDB300a
import random

class NISTSDB300aSamePerson(NISTSDB300a):
    
    def __init__(self, numOfSamplesPerSubject=-1, stichingModeStack=True,**kargs):
        self.numOfSamplesPerSubject = numOfSamplesPerSubject
        self.stichingModeStack = stichingModeStack
        NISTSDB300a.__init__(
            self, 
            name='NISTSDB300aSamePerson',
            classNames=['Different', 'Same'],
            **kargs
            )
    
        # 00001000_roll_500_01.png
    def getSubjectId(self, pathFile):
        # Convert the path to a list of path components
        fileName = tf.strings.split(pathFile, os.path.sep)[-1]
        className = tf.strings.split(fileName, '_')[0]  
        return className
    
    def makeTruesPairs(self, ds):
        sameDs = []
        for subject, paths in ds.items():
            random.shuffle(paths)
            subjectPairs = []
            for i in range(len(paths)):
                for j in range(i+1, len(paths)):
                    subjectPairs.append([paths[i], paths[j]])
            if self.numOfSamplesPerSubject == -1:
                sameDs.extend(subjectPairs)
            else:
                random.shuffle(subjectPairs)
                sameDs.extend(subjectPairs[:self.numOfSamplesPerSubject])
        return(sameDs)


    def makeFalsesPairs(self, ds, numOfSamples):
        notSameDs = []
        for i in range(numOfSamples):
            subjectA, subjectB = random.sample(ds.keys(), 2)
            pathA = random.choice(ds[subjectA])
            pathB = random.choice(ds[subjectB])
            notSameDs.append(tf.constant([pathA.numpy(), pathB.numpy()]))
        return notSameDs

    def proccessPath(self, pair):
        img0 = self.getFile(pair[0])
        img1 = self.getFile(pair[1])
        subj0 = self.getSubjectId(pair[0])
        subj1 = self.getSubjectId(pair[1])
        if self.stichingModeStack:
            final = tf.slice(tf.concat([img0, img1], axis=1), [0, 0, 0], [self.inputDim[1], self.inputDim[0]*2, 3])
        else:
            img0 = tf.slice(img0, [0, 0, 0], [self.inputDim[1], self.inputDim[0], 1])
            img1 = tf.slice(img1, [0, 0, 0], [self.inputDim[1], self.inputDim[0], 1])
            final = tf.concat([img0, img1, img0], axis=2)
        final = tf.image.resize(final, self.inputDim[0:2])
        one_hot_arc = [False, True]
        label = subj0 == subj1
        label = one_hot_arc == label
        return tf.cast(final, dtype=tf.uint8, name=None), label
    
    def create(self):
        PATH = '{}{}/*.png'
        path = PATH.format(os.getcwd(), self.path[1:])
        splittedDs = tf.data.Dataset.list_files(path, shuffle=False)
        if self.split:
            splittedDs = self.splitDatasetByRatio(splittedDs, self.split)
        finalDs = []
        for ds in splittedDs:  
            subjectsDs = {}
            for path in ds:
                label = self.getSubjectId(path).numpy()
                try:
                    subjectsDs[label]
                except:
                    subjectsDs[label] = []
                subjectsDs[label].append(path)
            finalDs.append(subjectsDs)
        pairsDs = []
        for ds in finalDs:
            trues = self.makeTruesPairs(ds)
            falses = self.makeFalsesPairs(ds, len(trues))
            trues.extend(falses)
            pairsDs.append(trues)
        for i, ds in enumerate(pairsDs):
            if self.shuffle:
                shuffleBS = len(pairsDs[i])
            else:
                shuffleBS = 1
            pairsDs[i] = tf.data.Dataset.from_tensor_slices(pairsDs[i]).map(self.proccessPath)
            pairsDs[i] = self.configureForPerformance(pairsDs[i], self.batchSize, shuffleBS)
        return pairsDs