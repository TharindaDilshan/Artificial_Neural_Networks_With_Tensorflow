# -*- coding: utf-8 -*-
"""ComputerVisionExample.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XDJwlcLXj1EsKdhOwLs4p257zTIxJAFP
"""

import tensorflow as tf

"""Fashion MNIST dataset will be used which is already available in tensorflow"""

mnist = tf.keras.datasets.fashion_mnist

Load_data will load 4 lists of data

(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

"""Visualizing data"""

import numpy as np
np.set_printoptions(linewidth=200)
import matplotlib.pyplot as plt
plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])

"""Normalizing data so it fits the range of 0-1"""

training_images = training_images / 255.0
test_images = test_images / 255.0

"""Model is created with 3 layers
First layer is used to convert the 28x28 data into a single array(784x1).
Second/middle layer will contain 1024 neurons 
Final layer will contain 10 neurons which indicates the 10 labels present in the dataset(0-9)
"""

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(1024, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)

model.evaluate(test_images, test_labels)

import tensorflow as tf
print(tf.__version__)

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('loss')<0.4):
      print("\nReached 60% accuracy so cancelling training!")
      self.model.stop_training = True

callbacks = myCallback()
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images/255.0
test_images=test_images/255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])