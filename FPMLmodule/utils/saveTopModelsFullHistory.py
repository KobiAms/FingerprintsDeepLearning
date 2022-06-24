import csv
from pathlib import Path
from matplotlib import pyplot as plt
import numpy as np

def saveTopModelsFullHistory(bestModels, path):
    
    for key, val in bestModels.items():
        datasetPath = path+key+'/'
        Path(path+key).mkdir(parents=True, exist_ok=True)
        f = open(datasetPath+'full_history.csv', 'w')
        writer = csv.writer(f)
        for key2, val2 in val.items():
            acc = ['Accuracy']
            val_acc = ['Val Accuracy']
            loss = ['Loss']
            val_loss = ['Validation Loss']
            writer.writerow([key2])
            for history in val2['model'].history:
                acc = [*acc, *history.history['accuracy']]
                val_acc = [*val_acc, *history.history['val_accuracy']]
                loss = [*loss, *history.history['loss']]
                val_loss = [*val_loss, *history.history['val_loss']]
            writer.writerow(acc)
            writer.writerow(val_acc)
            writer.writerow(loss)
            writer.writerow(val_loss)
            writer.writerow(['', ''])
            plt.figure(figsize=(10, 10))
            fig, ax1 = plt.subplots()

            ax2 = ax1.twinx()
            ax1.plot(np.asarray(acc[1:], float), 'o-', color="black" )
            ax1.plot(np.asarray(val_acc[1:], float), 'o-', color="gray" )
            ax2.plot(np.asarray(loss[1:], float), '-', color="red" )
            ax2.plot(np.asarray(val_loss[1:], float), '-', color="green" )

            ax1.legend(['train-acc', 'test-acc'])
            ax2.legend(['train-loss', 'test-loss'])
            ax1.set_xlabel('epochs')
            ax1.set_ylabel('Accuracy', color='g')
            ax2.set_ylabel('Loss', color='b')
            plt.grid()
            plt.savefig(datasetPath+key2+'.png', bbox_inches='tight')
            plt.close()

        f.close()