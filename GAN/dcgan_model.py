# Filename: dcgan_model.py
import tensorflow as tf
import numpy as np
from PIL import Image

def load_dcgan_model():
    generator = tf.keras.Sequential([
        tf.keras.layers.Dense(7 * 7 * 256, input_shape=(100,), use_bias=False),
        tf.keras.layers.Reshape((7, 7, 256)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.ReLU(),

        tf.keras.layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.ReLU(),

        tf.keras.layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.ReLU(),

        tf.keras.layers.Conv2DTranspose(32, (5, 5), strides=(2, 2), padding='same', use_bias=False),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.ReLU(),

        tf.keras.layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='sigmoid')
    ])

    dcgan_model = tf.keras.Sequential([generator])

    return dcgan_model


# Function to generate an image based on text input
def generate_image(text_input):
    # Create a random noise vector
    noise = np.random.normal(0, 1, (1, 100))

    # Generate an image using the GAN model
    generated_image = load_dcgan_model().predict(noise)

    # Rescale the pixel values to the range [0, 255]
    generated_image = 0.5 * generated_image + 0.5
    generated_image = (generated_image * 255).astype(np.uint8)

    # Convert the image array to a PIL Image
    pil_image = Image.fromarray(generated_image.squeeze(), mode='L')  # Ensure single channel (grayscale)

    # Save the generated image
    image_path = f"static/generated_images/{text_input.replace(' ', '_')}_generated_image.png"
    pil_image.save(image_path)

    return image_path
