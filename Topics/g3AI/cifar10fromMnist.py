import tensorflow as tf
import random
from tensorflow import keras
import numpy as np
from tensorflow.keras import Sequential, layers, Model, datasets
from tensorflow.keras.layers import Dense,Flatten
import matplotlib.pyplot as plt

BATCH_SIZE= 164
EPOCHS = 10

class_names = ["Airplane", "Automobile", "Bird", "Cat", "Deer",
               "Dog", "Frog", "Horse", "Ship", "Truck"]



#loads the data:label pairs
#(x_train, y_train),(x_test, y_test) = datasets.cifar10.load_data()

from pathlib import Path

dataPath =  Path(__file__).resolve().parent / "cifar10_students.npz"

with np.load(dataPath) as data:
    x_train = data["x_train"]
    y_train = data["y_train"]
    x_test = data["x_test"]
    y_test = data["y_test"]






#confirming the data:label pair
print(y_test[0]) #give me the label for the 1st item in the testing list
plt.imshow(x_test[0]) #show me the image from the 1st item in the test set
#plt.show()#put the image out

#CIFAR10 Labels have shape (N,1)
y_train = y_train.flatten()
y_test = y_test.flatten()

#Show an image from the set
x=  random.randint(0, 10000)
plt.imshow(x_test[x])
plt.title(class_names[y_test[x]])
plt.axis("off")
plt.show()
#ACTUALLY BUILD THE MODEL

x_train=  x_train.astype("float32")/255
x_test=  x_test.astype("float32")/255

model = Sequential() # each layer receive input from previous layer
model.add(layers.Conv2D(64, (3,3), activation='relu', padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Dropout(.25))

model.add(layers.Conv2D(32, (5,5), activation = 'relu', padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Dropout(.25))

model.add(layers.Flatten())
model.add(layers.Dense(128))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))
model.add(layers.Dropout(.5))
model.add(layers.Dense(10, activation='softmax'))

model.summary()
x_test = np.expand_dims(x_test, axis=-1)

# Select an image
index = random.randint(0, len(x_test)-1)
image = x_test[index]

model.compile(loss="sparse_categorical_crossentropy",
              optimizer = 'Adam',
              metrics= ["accuracy"])
#RUN
history = model.fit(x_train, y_train, batch_size =  BATCH_SIZE, epochs=EPOCHS, validation_data= (x_test, y_test))