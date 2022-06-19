from .saveStudyDefaultConfigToFile import saveStudyDefaultConfigToFile 
from .saveStudyHistoriesToFile import saveStudyHistoriesToFile
import csv

def saveStudyHistory(study, history, filePath, headlineOnly=False):
    if headlineOnly:
        f = open(filePath, 'a+')
        writer = csv.writer(f)
        writer.writerow(study.keys())
        f.close()
    else:
        saveStudyDefaultConfigToFile(study, filePath)
    saveStudyHistoriesToFile(history, filePath)