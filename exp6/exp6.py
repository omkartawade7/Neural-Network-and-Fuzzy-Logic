import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv('datasets/train.csv').as_matrix()
clf = DecisionTreeClassifier()
#training_dataet
xtrain = data[0:21000,1:]
train_label = data[0:21000,0]
clf.fit(xtrain,train_label)
#testing_data
xtest = data[21000:,1:]
actual_label = data[21000:,0]
d = xtest[15]
d.shape = (28,28)
pt.imshow(255-d,cmap='gray')
print(clf.predict([xtest[15]]))
pt.show()
