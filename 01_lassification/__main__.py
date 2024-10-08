from sklearn import datasets, model_selection, preprocessing
import numpy as np
#import tensorflow as tf

print("\n\n")

data = datasets.load_breast_cancer()

X_treino, X_teste, Y_treino, Y_teste = model_selection.train_test_split(data.data, data.target, test_size=0.33)

X_treino = preprocessing.StandardScaler.fit_transform(X_treino)
Y_treino = preprocessing.StandardScaler.fit_transform(Y_treino)
X_teste = preprocessing.StandardScaler.transform(X_teste)

print("\n\n")