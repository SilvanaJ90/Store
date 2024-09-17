import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, Concatenate, Flatten

def create_model():
    # Input layers
    category_input = Input(shape=(1,), name='category')
    brand_input = Input(shape=(1,), name='brand')
    price_input = Input(shape=(1,), name='price')