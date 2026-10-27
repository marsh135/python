import sys
import tensorflow as tf

print("Python:", sys.executable)
print("TensorFlow:", tf.__version__)

gpus = tf.config.list_physical_devices("GPU")
print("GPUs:", gpus)

if not gpus:
    raise RuntimeError("Metal GPU was not detected.")

# Require the requested device rather than silently using the CPU.
tf.config.set_soft_device_placement(False)

with tf.device("/GPU:0"):
    a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
    result = tf.matmul(a, a)

print("Calculation device:", result.device)
print("Result:\n", result.numpy())

print("GPU calculation passed.")