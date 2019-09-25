import tensorflow as tf


def get_data():
    return tf.compat.v2.keras.datasets.mnist.load_data()
