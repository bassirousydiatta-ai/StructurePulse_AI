import numpy as np


from sklearn.ensemble import RandomForestClassifier

import joblib


# Données d'entraînement
# vibration, temperature, humidity

X = np.array([

    [10, 25, 40],
    [15, 30, 50],
    [20, 35, 55],

    [85, 75, 90],
    [90, 80, 95],
    [95, 85, 98],

])

# 0 = normal
# 1 = danger

Y = np.array([
    0,
    0,
    0,
    1,
    1,
    1
])


# Création du modèle IA

model = RandomForestClassifier()

# Entraînement

model.fit(X, Y)

# Sauvegarder le modèle

joblib.dump(
    model,
    'ai_model.pkl'
)


def predict_risk(
    vibration,
    temperature,
    humidity
):

    model = joblib.load(
        'ai_model.pkl'
    )

    prediction = model.predict([[
        vibration,
        temperature,
        humidity
    ]])

    probability = model.predict_proba([[
        vibration,
        temperature,
        humidity
    ]])

    return {
        'prediction': int(prediction[0]),
        'probability': float(
            probability[0][1]
        )
    }





















"""
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


model = Sequential()

model.add(Dense(16, activation='relu', input_shape=(3,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# vibration, temperature, humidity

X = np.array([
    [10, 25, 40],
    [20, 30, 50],
    [90, 80, 95],
    [95, 85, 90],
    [15, 20, 35],
    [88, 70, 85]
])

# 0 = normal
# 1 = danger

Y = np.array([
    0,
    0,
    1,
    1,
    0,
    1
])

model.fit(X, Y, epochs=100)


def predict_risk(vibration, temperature, humidity):

    prediction = model.predict(
        np.array([[vibration, temperature, humidity]])
    )

    return float(prediction[0][0])
"""