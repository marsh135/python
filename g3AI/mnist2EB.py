import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras import Sequential, layers, Model
from tensorflow.keras.layers import Dense,Flatten
import matplotlib.pyplot as plt

BATCH_SIZE= 12
EPOCHS = 5

def show_feature_maps(feature_map, title):
    # Remove batch dimension
    features = feature_map[0]

    num_filters = features.shape[-1]
    cols = 8
    rows = int(np.ceil(num_filters / cols))

    fig, axes = plt.subplots(
        rows, cols,
        figsize=(14, rows * 1.8)
    )

    for i, ax in enumerate(axes.flat):
        if i < num_filters:
            ax.imshow(features[:, :, i], cmap="viridis")
            ax.set_title(f"Filter {i}", fontsize=9)

        ax.axis("off")

    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()


#loads the data:label pairs
(x_train, y_train),(x_test, y_test) = keras.datasets.mnist.load_data()

#confirming the data:label pair
print(y_test[0]) #give me the label for the 1st item in the testing list
plt.imshow(x_test[0]) #show me the image from the 1st item in the test set
#plt.show()#put the image out

#Normalize our data to Grayscale
x_train=  x_train/255.0
x_test = x_test/255.0
#diviging the value of every pixel by 255, which adjusts our color image to GS
plt.imshow(x_test[0], cmap="gray") #show me the image from the 1st item in the test set
#plt.show()#put the image out

#ACTUALLY BUILD THE MODEL

model = Sequential() # each layer receive input from previous layer

model.add(layers.Conv2D(32, (5,5), padding='same', input_shape=(28,28,1)))
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




# Add channel dimension: (10000, 28, 28, 1)
x_test = np.expand_dims(x_test, axis=-1)

# Select an image
index = 0
image = x_test[index:index+1]

print("Actual digit:", y_test[index])

plt.imshow(image[0, :, :, 0], cmap="gray")
plt.title("Original MNIST Image")
plt.axis("off")
plt.show()



# Find the two Activation layers
activation_layers = [
    layer.output
    for layer in model.layers
    if isinstance(layer, tf.keras.layers.Activation)
]

# Build a model that exposes those intermediate outputs
feature_model = Model(
    inputs=model.inputs,
    outputs=activation_layers[:2]
)
'''
# Run the digit through the network
feature_maps = feature_model.predict(image)

show_feature_maps(feature_maps[0], "First Convolution - 32 Feature Maps")
show_feature_maps(feature_maps[1], "Second Convolution - 64 Feature Maps")

for digit in [0, 1, 3, 5, 8]:
    index = np.where(y_test == digit)[0][0]
    image = x_test[index:index+1]

    maps = feature_model.predict(image, verbose=0)

    print(f"Digit: {digit}")
    show_feature_maps(maps[0], f"Digit {digit} - First Convolution")

# Results:
# feature_maps[0] = (1, 28, 28, 32)
# feature_maps[1] = (1, 14, 14, 64)
#BUILD IT
'''
model.compile(loss="sparse_categorical_crossentropy",
              optimizer = 'Adam',
              metrics= ["accuracy"])
#RUN
history = model.fit(x_train, y_train, batch_size =  BATCH_SIZE, epochs=EPOCHS)




