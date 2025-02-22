from sklearn import metrics
import matplotlib.pyplot as plt 

class CalcMetrics():
    @staticmethod
    def auc(y_pred_prob, y_test):
        fpr, tpr, _ = metrics.roc_curve(y_test, y_pred_prob)

        roc_auc = metrics.auc(fpr, tpr)

        # Plot ROC curve
        plt.figure()
        plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend(loc='lower right')
        plt.show()
    
    @staticmethod
    def ks(y_pred_prob, y_test):
        fpr, tpr, _ = metrics.roc_curve(y_test, y_pred_prob)
        return max(tpr - fpr)