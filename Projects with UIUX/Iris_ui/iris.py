from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix,precision_score,recall_score,f1_score,classification_report
import seaborn as sb
import matplotlib.pyplot as plt
import pickle
import pandas

iris = load_iris()
iris.keys()
X = iris.data
y = iris.target

#Split data into training & testing:-
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=30,random_state=42)

knn = KNeighborsClassifier()
knn.fit(X_train,y_train)

pred = knn.predict(X_test)

print(accuracy_score(y_test,pred))

pickle.dump(knn, open('iris.pkl', 'wb'))

model = pickle.load(open("iris.pkl", "rb"))