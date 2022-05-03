from FPMLmodule.fpml import FPML 

def researchStudies(train_set, val_set, studies, epochs=10, verbose=2):
    histories = {}
    for study, config in studies.items():
        fpml = FPML(**config["architecture"])
        model = fpml.create(**config["hyperparameters"])
        model_history = model.fit(train_set, validation_data=val_set, epochs=epochs, verbose=verbose)
        histories[study] = model_history
    return histories