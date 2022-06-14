import seaborn as sn
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


def displayConfusion(dataset, model, savePath=None):
    plt.subplots()
    test_images = []
    y_test = []
    y_predict = []

    for images, labels in dataset:

        tmp_predict = model.predict(images)
        tmp_true_max = np.argmax(labels.numpy(), axis=1).astype(np.uint8)
        tmp_pred_max = np.argmax(tmp_predict, axis=1).astype(np.uint8)
        test_images = [*test_images, *images]
        y_test = [*y_test, *tmp_true_max]
        y_predict = [*y_predict, *tmp_pred_max]

    cm = confusion_matrix(y_test, y_predict)
    sn.heatmap(cm ,annot = True, fmt='g')
    acc = (np.array(y_test) == np.array(y_predict)).sum()/len(y_test)
    plt.title("Test Set Accuracy:  "+str(round(acc*100, 2)))
    plt.tight_layout()
    if savePath:
        plt.savefig(savePath+'Confusion Matrix.png', bbox_inches='tight')
    else:   
        plt.show()
    return acc