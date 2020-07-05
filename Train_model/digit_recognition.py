import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras

data_set = keras.datasets.mnist

(train_digit, train_lable), (test_digit, test_lable) = data_set.load_data()


def display(index):
    plt.figure()
    plt.imshow(train_digit[index], cmap=plt.cm.binary)
    print(train_lable[index])
    plt.show()


train_digit = train_digit / 255.0

test_digit = test_digit / 255.0

model = keras.Sequential([keras.layers.Flatten(input_shape=(28, 28)),
                          keras.layers.Dense(128, activation="relu", name="hidden_layer_1"),
                          keras.layers.Dense(128, activation="relu", name="hidden_layer_2"),
                          keras.layers.Dense(10, activation="softmax", name="output_layer")])

model.compile(optimizer="adam",
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
              )

model.fit(train_digit, train_lable, epochs=3)

test_loss, test_acc = model.evaluate(test_digit, test_lable, verbose=1)

model.save("digit_2.model")

print('Test accuracy:', test_acc)
