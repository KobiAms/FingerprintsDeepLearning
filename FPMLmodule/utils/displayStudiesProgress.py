from matplotlib import pyplot as plt

def displayStudiesProgress(studiesHistories, savePath=None, fileName=None):
    nbStudies = len(studiesHistories)
    cur = 1
    plt.figure(figsize=(5*nbStudies, 4))
    for study, history in studiesHistories.items():
        
        acc_history = history['history'].history['accuracy']
        val_acc_history = history['history'].history['val_accuracy']
        loss_history = history['history'].history['loss']
        val_loss_history = history['history'].history['val_loss']
        
        plt.subplot(1, nbStudies, cur)
        plt.plot(acc_history, color='blue')
        plt.plot(val_acc_history, color='purple')
        plt.tick_params(axis='y')
        plt.ylabel('Accuracy')
        plt.xlabel('Epochs')
        plt.legend(['train-acc', 'test-acc'])
        pltT = plt.twinx()
        pltT.plot(loss_history, color='red')
        pltT.plot(val_loss_history, color='orange')
        pltT.tick_params(axis='y')
        plt.ylabel('Loss')
        plt.grid()
        plt.title(study)
        plt.xlabel('Epochs')
        plt.legend(['train-loss', 'test-loss'])
        cur+=1
    plt.tight_layout()
    
    if savePath:
        if fileName:
            plt.savefig(savePath+fileName+'.png', bbox_inches='tight')
            plt.suptitle(fileName, size=16)
        else:
            plt.savefig(savePath+'studiesProgress.png', bbox_inches='tight')
            plt.suptitle('studiesProgress', size=16)
        plt.close()
    else:   
        plt.show()