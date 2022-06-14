import imp
from .saveStudyDefaultConfigToFile import saveStudyDefaultConfigToFile 
from .saveStudyHistoriesToFile import saveStudyHistoriesToFile

def saveStudyHistory(study, history, filePath):
    saveStudyDefaultConfigToFile(study, filePath)
    saveStudyHistoriesToFile(history, filePath)