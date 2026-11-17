# IMPORTS
# Import TensorFlow, the machine-learning library (the tf alias is unused here).
import tensorflow as tf
# Keras is TensorFlow's high-level API for building and training neural networks.
from tensorflow import keras
# Sequential builds a model whose layers run in order, one after another.
from tensorflow.keras import Sequential
# Dense is a fully connected layer; Flatten reshapes images into flat vectors.
from tensorflow.keras.layers import Dense,Flatten
# pyplot provides functions for displaying the digit images.
import matplotlib.pyplot as plt
# accuracy_score measures the fraction of predictions that match the true labels.
from sklearn.metrics import accuracy_score


# LOAD MNIST DATA (original line 11)
# load_data() downloads MNIST if needed, then returns two pairs of NumPy arrays.
# The nested parentheses unpack those pairs into four variables:
# x_train: 60,000 training images, with shape (60000, 28, 28).
# y_train: 60,000 matching integer labels (digits 0 through 9), shape (60000,).
# x_test: 10,000 test images, with shape (10000, 28, 28).
# y_test: 10,000 matching test labels, shape (10000,).
# Each image is a 28-by-28 grayscale grid with pixel values from 0 to 255.
# The test set is kept separate to evaluate performance on unseen examples.
(x_train, y_train),(x_test, y_test) = keras.datasets.mnist.load_data()

# Print the training labels; NumPy usually abbreviates such a large array.
print(y_train)

# Display the 50,001st training image (Python indexes start at 0).
# imshow uses its default color map; cmap='gray' would show grayscale shades.
plt.imshow(x_train[50000])
# Open/render the plot so you can see the selected handwritten digit.
plt.show()

# Scale both image sets from 0-255 to floating-point values from 0-1.
# This keeps input magnitudes small and usually makes training easier.
x_train, x_test = x_train / 255.0, x_test / 255.0

# BUILD THE NETWORK (original lines 20-24)
# Create an empty Sequential model; each added layer receives the previous output.
model= Sequential()
# Specify that each input image has shape (28, 28), excluding the batch dimension.
# Flatten rearranges its 784 pixels into one vector: (batch, 28, 28) -> (batch, 784).
# It does not learn weights or change pixel values; it only changes their shape.
model.add(Flatten(input_shape=(28,28)))
# Add 128 neurons, each connected to all 784 inputs with learned weights and a bias.
# Each neuron computes a weighted sum plus bias, then applies ReLU: max(0, value).
# ReLU adds nonlinearity, allowing the network to learn more complex patterns.
model.add(Dense(128, activation='relu'))
# Add 32 neurons connected to the preceding 128 outputs, again using ReLU.
# This hidden layer combines the features learned by the preceding layer.
model.add(Dense(32,activation='relu'))

# OPTIONAL HIDDEN LAYERS: remove the leading "# " from a model.add(...) line
# to enable it. Leave the explanation comments in place, then rerun the script.
# Try one extra layer first; keep the epoch count fixed when comparing networks.
# Each enabled layer takes input from the nearest enabled layer above it.
# Keep these hidden layers BEFORE the final softmax output layer.
# More layers add learning capacity and computation, but do not guarantee better
# validation accuracy. They can also overfit (learn training-specific patterns).

# A wide layer: learn 256 new combinations of the preceding layer's features.
# Expanding from 32 to 256 outputs does not recover information already lost.
# model.add(Dense(256, activation='relu'))

# A 128-neuron layer: combine the previous features using new weights and biases.
# ReLU keeps positive values and replaces negative values with zero.
# model.add(Dense(128, activation='relu'))

# Another 128-neuron layer: increase depth while keeping the same width if the
# preceding optional layer is enabled. These neurons learn their own weights;
# repeating a layer size does not mean repeating the same calculation.
# model.add(Dense(128, activation='relu'))

# A 64-neuron layer: if it follows a wider layer, compress its representation
# into fewer features. Check model.summary() to see how parameter counts change.
# model.add(Dense(64, activation='relu'))

# A 32-neuron layer: add another nonlinear transformation before classification.
# A Dense layer has (number of inputs * number of neurons) + number of neurons
# trainable parameters: one weight per connection plus one bias per neuron.
# model.add(Dense(32, activation='relu'))

# A 16-neuron layer: try a narrow bottleneck that forces a compact representation.
# Too few neurons may limit what the network can learn (underfitting).
# model.add(Dense(16, activation='relu'))

# An 8-neuron layer: experiment with an even tighter bottleneck. Hidden layers
# may have fewer than 10 neurons; only the output needs one neuron per class.
# Compare training and validation accuracy to judge whether this is helpful.
# model.add(Dense(8, activation='relu'))

# Produce 11 class scores, then softmax converts them into probabilities summing to 1.
# NOTE: MNIST has only 10 classes (0-9), so Dense(10, ...) is the appropriate size.
# The existing 11 is preserved here; it adds an unused class at index 10 that the
# model could predict, even though no training label represents that class.
model.add(Dense(11,activation='softmax'))
# Print the layers, output shapes, and counts of learned parameters (weights/biases).
model.summary()

# CONFIGURE TRAINING
# loss='sparse_categorical_crossentropy' measures multiclass prediction error.
# "Sparse" means the true labels are integers such as 7, instead of one-hot
# vectors such as [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]. It does not mean sparse images.
# For one example, the loss is -log(probability assigned to its true class).
# A high probability for the correct digit gives a small loss; a low one gives
# a large loss. Training tries to reduce the average loss over examples.
# This default loss expects probabilities, which the softmax layer supplies.
# optimizer='Adam' selects Adaptive Moment Estimation: the weight-update algorithm.
# Backpropagation computes gradients showing how weights/biases affect the loss.
# Adam tracks moving averages of gradients and squared gradients, with bias
# correction, to adapt each parameter's update using the learning rate.
# This combines momentum-like smoothing with per-parameter step-size adaptation.
# metrics=['accuracy'] also reports the fraction of correct predictions; accuracy
# is monitored, while the crossentropy loss drives the gradient updates.
model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])
# Train for 25 epochs (passes through the training portion), updating in batches.
# validation_split=0.2 reserves the last 20% of the supplied training examples
# (12,000 images) for validation before shuffling; 48,000 are used for updates.
# Validation measures loss/accuracy after each epoch without updating weights.
# history stores the recorded training and validation metrics for each epoch.
history = model.fit(x_train,y_train,epochs=25,validation_split=0.2)

# Compute class probabilities for every test image, without training the model.
# With the current output layer, y_prob has shape (10000, 11).
y_prob = model.predict(x_test)
# Pick the index of the largest probability in each row (one predicted digit).
# axis=1 means look across the class columns, separately for each test image.
y_pred = y_prob.argmax(axis=1)
# Calculate test accuracy from 0 to 1 (e.g., 0.97 means 97% correct).
# In a script this value is discarded; wrap in print(...) to display it.
accuracy_score(y_test,y_pred)
