def getBestStudyFromHistories(histories, studiesToReturn=1):
    if len(histories) < studiesToReturn:
        studiesToReturn = len(histories)
    sortedHistories = [k for k, v in sorted(histories.items(), key=lambda item: item[1]['history'].history['val_accuracy'][-1], reverse=True)]
    if studiesToReturn == 1:
        return sortedHistories[0]
    else:
        return sortedHistories[:studiesToReturn]
    