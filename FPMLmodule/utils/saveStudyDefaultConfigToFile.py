import csv

def saveStudyDefaultConfigToFile(studies, filePath):
    f = open(filePath, 'a+')
    writer = csv.writer(f)
    row = []
    for key, val in studies.items():
        row.append(key)
        studyConfig = val['hyperparameters']
        for paramType, config in studyConfig.items():
            if(isinstance(config, list)):
                continue
            if paramType == 'optimizer':
                row.append(paramType+": "+str(config.__name__)) 
            else:
                row.append(paramType+": "+str(config))
        writer.writerow(row)
    f.close()