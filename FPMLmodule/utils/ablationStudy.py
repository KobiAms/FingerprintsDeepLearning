import FPMLmodule.utils as utils
import FPMLmodule.backbones as backbones
import FPMLmodule.classifiers as classifiers
from tensorflow.keras.optimizers import Adam, Nadam, RMSprop
from FPMLmodule.fpml import FPML 
import copy

# import tensorflow as tf



def fingerprintsProjectMainStudyAbalation(configureDS, trainDs, testDs, valDs, imgDim, epochsForSearch, epochsForBest, outPath, verbose=1):
    
    
    weightsRN50 = "./weights/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5"
    weightsMNV2 = "./weights/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5"
    weightsENB2 = "./weights/efficientnetb2_notop.h5"
    weightsINCEPTIONV3 = "./weights/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5"
    weightsXCEPTION = "./weights/xception_weights_tf_dim_ordering_tf_kernels_notop.h5"
    
    nbClasses = len(configureDS.classNames)
    activation = "softmax"
    hypers = {
        "optimizer": Adam,
        "learningRate": 0.001,
        "loss": 'binary_crossentropy',
        "metrics": 'accuracy'
    }


    # Training Mode
    trainingModeStudy =  {
        "mobilenetV2" : {
            "architecture": {
                "backbone": [
                    backbones.MobileNetV2(imgDim, weights=weightsMNV2, trainable=False),
                    backbones.MobileNetV2(imgDim, weights=weightsMNV2, trainable=True),
                    backbones.MobileNetV2(imgDim, weights=None, trainable=True)
                    ],
                "classfier": classifiers.DefaultClassifier(nbClasses, activation),
                "inputLayer": None, 
                "inputDim": imgDim
            },
            "hyperparameters":hypers
        }
    }
    trainingModeHistories = utils.researchStudies(trainDs, valDs, trainingModeStudy, epochsForSearch, verbose)
    trainingModeBestModel = utils.getBestStudyFromHistories(trainingModeHistories)
    trainable = 'Backbone0' not in trainingModeBestModel
    pretrained = 'Backbone2' not in trainingModeBestModel
    utils.saveStudyDefaultConfigToFile(trainingModeStudy, './'+configureDS.name+'.csv')
    utils.saveStudyHistoriesToFile(trainingModeHistories, './'+configureDS.name+'.csv')
    print("Training Mode Selected - Pretrained:", pretrained, 'Trainable:', trainable)

    # Backbone
    bestBackboneStudy = {
        "bbstudy" : {
            "architecture": {
                "backbone": [
                    backbones.ResNet50(imgDim, weights=weightsRN50, trainable=trainable),
                    backbones.EfficientNetB2(imgDim, weights=weightsENB2, trainable=trainable),
                    backbones.InceptionV3(imgDim, weights=weightsINCEPTIONV3, trainable=trainable),
                    backbones.Xception(imgDim, weights=weightsXCEPTION, trainable=trainable)
                    ],
                "classfier": classifiers.DefaultClassifier(nbClasses, activation),
                "inputLayer":"", 
                "inputDim": imgDim
            },
            "hyperparameters": hypers
        },
    }
    bestBackboneHistories = utils.researchStudies(trainDs, valDs, bestBackboneStudy, epochsForSearch, verbose)
    bestBackboneHistories[trainingModeBestModel] = trainingModeHistories[trainingModeBestModel]
    bestBackbone = utils.getBestStudyFromHistories(bestBackboneHistories)
    utils.saveStudyDefaultConfigToFile(bestBackboneStudy, './'+configureDS.name+'.csv')
    utils.saveStudyHistoriesToFile(bestBackboneHistories, './'+configureDS.name+'.csv')
    print("Best DNN Backbon:", bestBackbone)


    # Optimizer
    optimizersStudy = copy.deepcopy(bestBackboneHistories[bestBackbone]['config'])
    optimizersStudy["hyperparameters"]["optimizer"] = [Nadam, RMSprop]
    optimizersHistories = utils.researchStudies(trainDs, valDs, {bestBackbone : optimizersStudy}, epochsForSearch, verbose)
    optimizersHistories[bestBackbone+"_Adam"] = bestBackboneHistories[bestBackbone]
    bestOptimizier = utils.getBestStudyFromHistories(optimizersHistories)
    utils.saveStudyDefaultConfigToFile({bestBackbone: optimizersStudy}, './'+configureDS.name+'.csv')
    utils.saveStudyHistoriesToFile(optimizersHistories, './'+configureDS.name+'.csv')
    print("Best Optimizier:", bestOptimizier)


    # Learning rate
    learningRatesStudy = copy.deepcopy(optimizersHistories[bestOptimizier]['config'])
    learningRatesStudy['hyperparameters']['learningRate'] = [0.1, 0.1e-1, 0.1e-3, 0.1e-4]
    learningRatesHistories = utils.researchStudies(trainDs, valDs, {bestOptimizier: learningRatesStudy}, epochsForSearch, verbose)
    learningRatesHistories[bestOptimizier+"_"+str(hypers["learningRate"])] = optimizersHistories[bestOptimizier]
    bestLearningRate = utils.getBestStudyFromHistories(learningRatesHistories)
    utils.saveStudyDefaultConfigToFile({bestOptimizier: learningRatesStudy}, './'+configureDS.name+'.csv')
    utils.saveStudyHistoriesToFile(learningRatesHistories, './'+configureDS.name+'.csv')
    print("Best Learning Rate:", bestLearningRate)

    lossStudy = copy.deepcopy(learningRatesHistories[bestLearningRate]['config'])
    lossStudy['hyperparameters']["loss"] = ['binary_focal_crossentropy', 'hinge']
    lossesHistories = utils.researchStudies(trainDs, valDs, {bestLearningRate: lossStudy}, epochsForSearch, verbose)
    lossesHistories[bestLearningRate+"_"+str(hypers["loss"])] = learningRatesHistories[bestLearningRate]
    bestLoss = utils.getBestStudyFromHistories(lossesHistories)
    utils.saveStudyDefaultConfigToFile({bestLearningRate: lossStudy}, './'+configureDS.name+'.csv')
    utils.saveStudyHistoriesToFile(lossesHistories, './'+configureDS.name+'.csv')
    print(bestLoss)

    bestModelName = bestLoss
    bestModelSetting = lossesHistories[bestLoss]['config']
    trainValDs = trainDs.concatenate(valDs)
    bestModel = FPML(**bestModelSetting["architecture"]).create(**bestModelSetting["hyperparameters"])
    bestModelHistory = bestModel.fit(trainValDs, validation_data=testDs, epochs=epochsForBest, verbose=2)
    bestModel.save('./weights/FPML_'+configureDS.name+'_'+bestModelName+".h5")
    
