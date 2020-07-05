import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow import keras

data_set = keras.datasets.mnist

(train_digit, train_lable), (test_digit, test_lable) = data_set.load_data()

train_digit = train_digit.reshape(60000, 28, 28, 1)
test_digit = test_digit.reshape(10000, 28, 28, 1)

train_lable_hot = tf.keras.utils.to_categorical(train_lable)
test_lable_hot = tf.keras.utils.to_categorical(test_lable)

model = models.Sequential()
model.add(layers.Conv2D(64, kernel_size=3, activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, kernel_size=3, activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, kernel_size=3, activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_digit, train_lable, epochs=4,
                    validation_data=(test_digit, test_lable))

test_loss, test_acc = model.evaluate(test_digit, test_lable, verbose=2)
print(test_acc)

model.save("my_CNN_model.model")
