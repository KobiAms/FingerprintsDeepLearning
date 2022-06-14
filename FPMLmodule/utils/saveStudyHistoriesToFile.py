import csv

def saveStudyHistoriesToFile(histories, filePath, historyType='val_accuracy'):
    f = open(filePath, 'a+')
    writer = csv.writer(f)
    headersCreated = False
    for net in histories:
        accHistory = histories[net]['history'].history[historyType]
        if not headersCreated:
            headers = []
            headers.append('Study')
            for i in range(len(accHistory)):
                headers.append('E-'+str(i))
            writer.writerow(headers)
            headersCreated=True
        row = []
        row.append(net)
        for acc in accHistory:
            row.append(str(round(acc*100, 2))+'%')
        writer.writerow(row)
    
    writer.writerow('')    
    f.close()