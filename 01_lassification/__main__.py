from sklearn import datasets, model_selection, preprocessing
import numpy as np
import tensorflow as tf

print("\n\n")

data = datasets.load_breast_cancer()

X_treino, X_teste, Y_treino, Y_teste = model_selection.train_test_split(data.data, data.target, test_size=0.33)

scaler = preprocessing.StandardScaler()
X_treino = scaler.fit_transform(X_treino)
X_teste = scaler.transform(X_teste)

model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(D,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

r = model.fit(X_treino, Y_treino, validation_data=(X_teste, Y_teste), epochs=100)

print(r)

print("\n\n")