
def getBestStudyFromHistories(histories):
    bestStudy = None
    bestAcc = 0
    for key, val in histories.items():
        if bestAcc < val['history'].history['val_accuracy'][-1]:
            bestAcc = val['history'].history['val_accuracy'][-1]
            bestStudy = key
    return bestStudy