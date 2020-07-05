import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
import cv2

model = keras.models.load_model("my_CNN_model.model")

for i in range(0, 1):
    img = cv2.imread('{}.png'.format(i))[:, :, 0]  # reads image 'opencv-logo.png' as grayscale
    img = img.reshape((28, 28, 1))
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    img = img.reshape(28, 28)
    plt.imshow(img, cmap=plt.cm.binary)
    print("the result is probably ", np.argmax(prediction))
    plt.show()
