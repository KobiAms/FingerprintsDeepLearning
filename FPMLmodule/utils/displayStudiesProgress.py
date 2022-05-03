from matplotlib import pyplot as plt

def displayStudiesProgress(studies):
    nbStudies = len(studies)
    cur = 1
    plt.figure(figsize=(10, 4*nbStudies))
    for study, history in studies.items():
        
        acc_history = history.history['accuracy']
        val_acc_history = history.history['val_accuracy']
        loss_history = history.history['loss']
        val_loss_history = history.history['val_loss']
        
        plt.subplot(nbStudies, 2, cur)
        plt.plot(acc_history)
        plt.plot(val_acc_history)
        plt.axis(ymin=0,ymax=1)
        plt.grid()
        plt.title('Accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epochs')
        plt.legend(['train', 'Test'])
        cur+=1
        
        plt.subplot(nbStudies, 2, cur)
        plt.plot(loss_history)
        plt.plot(val_loss_history)
        plt.grid()
        plt.title('Loss')
        plt.ylabel('Loss')
        plt.xlabel('Epochs')
        plt.legend(['Train', 'Test'])
        plt.tight_layout(pad=2.0)
        cur+=1
        
        
    location = 1
    height = 1/nbStudies
    for i, study in enumerate(studies):
        plt.figtext(0.5,location, study, ha="center", va="top", fontsize=14, color="b")
        location-=height
        
    