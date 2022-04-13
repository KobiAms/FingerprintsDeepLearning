from matplotlib import pyplot as plt


def displayTrainingGraph(history):
    
    plt.figure(figsize=(10, 5))
    acc_history = history.history['accuracy']
    val_acc_history = history.history['val_accuracy']
    loss_history = history.history['loss']
    val_loss_history = history.history['val_loss']
    plt.subplot(1, 2, 1)
    plt.plot(acc_history)
    plt.plot(val_acc_history)
    plt.axis(ymin=0.2,ymax=1)
    plt.grid()
    plt.title('Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epochs')
    plt.legend(['train', 'Test'])

    plt.subplot(1, 2, 2)
    plt.plot(loss_history)
    plt.plot(val_loss_history)
    plt.grid()
    plt.title('Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epochs')
    plt.legend(['Train', 'Test'])
    plt.tight_layout(pad=2.0)
    plt.show()