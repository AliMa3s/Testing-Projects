import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# install these libraries beforehand: pip install Pillow
# pip install tensorflow
# pip install --upgrade tensorflow

# Load the pre-trained ResNet50 model
model = ResNet50(weights='imagenet')

def classify_image(img_path):
    # Load and prepare the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    img_ready = preprocess_input(img_array_expanded_dims)

    # Perform the prediction
    predictions = model.predict(img_ready)
    # Decode the prediction
    label = decode_predictions(predictions, top=1)[0][0][1]
    confidence = decode_predictions(predictions, top=1)[0][0][2]
    return label, confidence

# Example usage
img_path = 'deer-1367217_640.jpg'
label, confidence = classify_image(img_path)
print(f'This image is a {label} with {confidence:.2f}% confidence.')
