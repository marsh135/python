import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras import Sequential, layers, Model
from tensorflow.keras.layers import Dense,Flatten
import matplotlib.pyplot as plt

BATCH_SIZE= 128
EPOCHS = 5

#this is not specifically necessary
class_names = [
    "airplane", "automobile","bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]
#loads the data
(x_train, y_train),(x_test, y_test) = keras.datasets.cifar10.load_data()

#confirming the data:label pair
print(y_test[0]) #give me the label for the 1st item in the testing list
plt.imshow(x_test[0]) #show me the image from the 1st item in the test set
#plt.show()#put the image out



#Normalize our data
x_train=  x_train.astype("float32")/255.0
x_test = x_test.astype("float32")/255.0
y_test = y_test.flatten()
y_train = y_train.flatten()



#ACTUALLY BUILD THE MODEL

model = Sequential() # each layer receive input from previous layer

model.add(layers.Conv2D(32, (5,5), padding='same', input_shape=(32,32,3)))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Dropout(.25))

model.add(layers.Conv2D(64, (3,3), padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Dropout(.25))


model.add(layers.Flatten())
model.add(layers.Dense(128))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))
model.add(layers.Dropout(.5))
model.add(layers.Dense(10, activation='softmax'))

model.summary()



model.compile(loss="sparse_categorical_crossentropy",
              optimizer = 'Adam',
              metrics= ["accuracy"])
#RUN
history = model.fit(x_train, y_train, 
                    batch_size =  BATCH_SIZE, 
                    epochs=EPOCHS)




