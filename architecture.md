# Neural Network Model Architecture 🧠

---

## Definition: Evaluation Metrics 🎯

---

### Accuracy
- The proportion of true results (both true positives and true negatives) among the total number of cases examined.
```python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)
```

---

### [Precision, Recall, F1](https://emkademy.com/research/toolbox/2020-03-02-accuracy-precision-recall) 🎯
- Precision: The ratio of correctly predicted positive observations to the total predicted positives.
- Recall (Sensitivity): The ratio of correctly predicted positive observations to the all observations in actual class.
- F1 Score: The weighted average of Precision and Recall.

```python
from sklearn.metrics import precision_score, recall_score, f1_score
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
```
【19†source】【20†source】【21†source】【22†source】

---

### [AUC](https://paulvanderlaken.com/2019/08/16/roc-auc-precision-and-recall-visually-explained) 🎯
- Area Under the ROC Curve: A performance measurement for classification problem at various thresholds settings.
```python
from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_true, y_score)
```

---

## Definition: [Confusion Matrix](https://www.statology.org/confusion-matrix-python/) 🔍
* [TensorFlow Version](https://www.tensorflow.org/tutorials/audio/simple_audio#display_a_confusion_matrix)

```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
```

---

## Discussion: Loss functions vs model metrics? 📊
* Diving into the differences and implications

---

## Measuring Model Performance 💹

---

### Excel Neural Net Reflection

---

### [Custom Loss Functions](https://stackoverflow.com/questions/53980031/pytorch-custom-loss-function)

```python
import torch
import torch.nn as nn

class CustomLoss(nn.Module):
    def forward(self, y_pred, y_true):
        loss = torch.mean((y_pred - y_true)**2)
        return loss

custom_loss = CustomLoss()
```

---

### [Custom Loss Functions #2](https://discuss.pytorch.org/t/custom-loss-functions/29387/3)

---

## "The Price is Right" Loss Function? 💰
* Exploring a unique loss function perspective
* Back to the excel neural network...

---

## Layer Types and Template Models 🧩
* Unveiling the building blocks of neural networks
* [MNIST classifier visualized](https://m.youtube.com/watch?v=Tsvxx-GGlTg)
* [LLMs visualized](https://bbycroft.net/llm)

---

## Demo: [Industry "Example" Models](./example_models) 🏭
* Reviewing real-world model architectures

---

## Hyperparameters Tuning 🎛️
* Where to start and how to adjust for better performance

---

## Stealing Ideas: Learning from Others 🎓
* Gathering insights from existing architectures and research

---

# END
