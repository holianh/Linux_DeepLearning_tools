# Interesting Machine Learning / Deep Learning Scenarios

This gist aims to explore interesting scenarios that may be encountered while training machine learning models.

## Increasing validation accuracy *and* loss
Let's imagine a scenario where the validation accuracy *and* loss both begin to increase.  Intuitively, it seems like this scenario should not happen, since loss and accuracy seem like they would have an inverse relationship.  Let's explore this a bit in the context of a binary classification problem in which a model parameterizes a Bernoulli distribution (i.e., it outputs the "probability" of the true class) and is trained with the associated negative log likelihood as the loss function (i.e., the "logistic loss" == "log loss" == "binary cross entropy").

Imagine that when the model is predicting a probability of 0.99 for a "true" class, the model is both correct (assuming a decision threshold of 0.5) and has a low loss since it can't do much better for that example.  Now, imagine that the model starts to predict a probability of 0.51 for that same example.  In this case, the model is still correct, but the loss will be much higher.  That covers the case of a flattened accuracy alongside increasing loss.  Let's now add in another example for which the model was originally incorrectly predicting 0.49 for a true class and is now correctly predicting 0.51.  For this individual example, there will only be a small decrease in loss.  If we imagine that both changes occur at the same time, the model will have both a higher accuracy *and* a higher loss (assuming the earlier loss increase is greater than the small decrease for this example).

Example:
```python
import numpy as np

def log_loss(pred, y):
  n = len(pred)
  losses = -y*np.log(pred) - (1-y)*np.log(1-pred)
  loss = np.sum(losses) / n
  return loss

def accuracy(pred, y, threshold=0.5):
  pred = pred >= threshold
  acc = np.mean(pred == y)
  return acc * 100

# almost perfect
pred = np.array([0.99])
y = np.array([1])
loss = log_loss(pred, y)
acc = accuracy(pred, y)
print(loss, acc)  # 0.0100503358535 100.0

# barely correct -- no change in accuracy, much higher loss
pred = np.array([0.51])
y = np.array([1])
loss = log_loss(pred, y)
acc = accuracy(pred, y)
print(loss, acc)  # 0.673344553264 100.0

# one barely incorrect prediction, one very correct prediction
pred = np.array([0.49, 0.99])
y = np.array([1, 1])
loss = log_loss(pred, y)
acc = accuracy(pred, y)
print(loss, acc)  # 0.361700111865 50.0

# two barely correct predictions -- higher accuracy, higher loss
pred = np.array([0.51, 0.51])
y = np.array([1, 1])
loss = log_loss(pred, y)
acc = accuracy(pred, y)
print(loss, acc)  # 0.673344553264 100.0
```
