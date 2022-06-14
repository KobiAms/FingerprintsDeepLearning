from FPMLmodule.utils import displayDatasetSplitInformation, displayDsSamples

def datasetAnalysisAndDisplay(splittedDs, configureDs, path):
    displayDatasetSplitInformation(splittedDs, configureDs.classNames, path)
    displayDsSamples(splittedDs[0], shape=(1,6), title=configureDs.name, classNames=configureDs.classNames, savePath=path)