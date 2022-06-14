from FPMLmodule.fpml import FPML
from FPMLmodule.utils import encapsulationStudies
import copy

def encapsulationStudies(studies):
    explicitStudies = {}
    for study in studies:
        entered = False
        for parameterGroup in studies[study]:
            for specificParameterKey in studies[study][parameterGroup]:
                specificParameter = studies[study][parameterGroup][specificParameterKey]
                if(isinstance(specificParameter, list)):
                    entered = True
                    for i, parameter in enumerate(specificParameter):
                        studyName = study+"_"
                        if(specificParameterKey == 'optimizer'):
                            studyName += parameter.__name__
                        elif(specificParameterKey == 'backbone'):
                            studyName = parameter.name+str(i)
                        else:
                            studyName = study+"_"+str(parameter)
                        explicitStudies[studyName] = copy.deepcopy(studies[study])
                        explicitStudies[studyName][parameterGroup][specificParameterKey] = parameter
        if not entered:
            explicitStudies[study] = copy.deepcopy(studies[study])
    return explicitStudies

def researchStudies(train_set, val_set, studies, epochs=10, verbose=1):
    studies = encapsulationStudies(studies)
    histories = {}
    for study, config in studies.items():
        fpml = FPML(**config["architecture"])
        model = fpml.create(**config["hyperparameters"])
        model_history = model.fit(train_set, validation_data=val_set, epochs=epochs, verbose=verbose)
        histories[study] = {
            "history":model_history,
            "config": config
            }
    return histories