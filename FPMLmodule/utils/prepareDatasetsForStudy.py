import FPMLmodule.utils as utils
from pathlib import Path

def prepareDatasetsForStudy(datasets, pathTamplate=None):
    prepared = {}
    for studyDs in datasets:
        readyDs = studyDs.create()
        path = None
        if pathTamplate:
            path = pathTamplate.format(studyDs.name)
            Path(path).mkdir(parents=True, exist_ok=True)
        utils.datasetAnalysisAndDisplay(readyDs, studyDs, path)
        prepared[studyDs.name] = {
            "configureDS" : studyDs,
            "datasets" : readyDs,
            "path" : path
        }
    return prepared