import numpy as np
from tensorflow import keras


def predict_CNN(img):
    model = keras.models.load_model("G:\App\App\models\my_CNN_model.model")
    img = img.reshape((28, 28, 1))
    img = np.invert(np.array([img]))
    img = img + 256

    img = img.astype(float)
    prediction = model.predict(img)

    return np.argmax(prediction)
