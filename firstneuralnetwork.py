# -*- coding: utf-8 -*-
"""FirstNeuralNetwork.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rroaln5xJAfES_320AoL8xAtqiI4uTzy

Import numpy to manipulate python lists.
Keras is a framework for defining a neural network as a set of sequential layers.
"""

import tensorflow as tf
import numpy as np
from tensorflow import keras

"""Create a simple neural network with one layer consisting of a single neuron. Input shape to it is just 1 value."""

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

"""Compile the neural network by specifying loss and optimizer functions.



*   Initaially a guess is made by the neural network is trained with a guess.
*   The LOSS function measures the guessed answers against the known correct answers and measures how badly it did.
*   Then the OPTIMIZER function is used to make another guess. It will try to minimize the loss
*   This will be repeated for the specified number of EPOCHS. Optimizer used here is 'Stochastic Gradient Descent' and the loss function is 'Mean Squared Error'
"""

model.compile(optimizer='sgd', loss='mean_squared_error')

"""Feeding Data

Numpy is used to generate array type data structure to provide dara into the modal.

xs contains the x values and the respective answer is stored in ys.


> y = 3x -1
"""

xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-4.0, -1.0, 2.0, 5.0, 8.0, 11.0], dtype=float)

"""Training the Neural Network

In the model.fit call the neural network learns the relationship between the Xs and Ys. This will go through a loop using optimizer and loss functions for the specified number of EPOCHS. loss will be displayed in the right hand side of the each iteration
"""

model.fit(xs, ys, epochs=500)

"""Finally the model.predict method is used to predict Y value for a known X value."""

print(model.predict([10.0]))

"""The predicted value will be few decimals places smaller than the exact value. This is becuase Neural Networks deal with probabilities and with a very small dataset we can't know for sure that the model fits all other data points."""