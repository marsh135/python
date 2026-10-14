import tensorflow as tf

# Check for available GPU devices
print(tf.config.list_physical_devices('GPU'))