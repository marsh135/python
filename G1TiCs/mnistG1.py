#imports
import seaborn as sns
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#print out versions of libaries
print("Tensorflow: ", tf.__version__ , " Seaborn:" , sns.__version__)

#load the data set
mnist = tf.keras.datasets.mnist
#create the training and testing data frames
#(training images, training labels), (testing images, testing labels)
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#show the number of examples in each labeled set

sns.countplot(x=y_train)
#show the plot!
plt.show()

#check to make sure there are NO values that are not a number (NaN)
print("Any NaN Training:", np.isnan(x_train).any())
print("Any NaN Testing: ", np.isnan(x_test).any())

#tell the model what shape to expect
input_shape = (28, 28, 1) #28x28 p0x, 1 color channel (grayscale) - 3 for RGB

#reshape the training and testing data
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
x_train = x_train/255.0 #normalize the data to be between 0 and 1
#same for testing
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
x_test = x_test/255.0 #normalize the data to be between 0 and 1