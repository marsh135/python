#IMPORTS
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Flatten
import matplotlib.pyplot as plt

#import MNIST DATA
(x_train, y_train),(x_test, y_test) = keras.datasets.mnist.load_data()

print(y_train)

plt.imshow(x_train[50000])
plt.show()