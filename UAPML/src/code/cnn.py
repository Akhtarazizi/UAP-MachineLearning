import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

def load_model():
    model_path = 'E:/Semester 7/Praktikum ML/UAPML/src/model/cnnuap_model.h5'
    model = tf.keras.models.load_model(model_path)
    return model

def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to match model input size
    image_array = np.array(image) / 255.0  # Normalize pixel values
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array

def predict_class(model, image_array):
    classes = ['Cataract', 'Diabetic Retinopathy', 'Glaucoma', 'Normal']
    predictions = model.predict(image_array)
    predicted_class = classes[np.argmax(predictions)]
    confidence = np.max(predictions)
    return predicted_class, confidence

def cnn_predict():
    st.write("### Upload a retina image for CNN model prediction")

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.write("")

        model = load_model()
        preprocessed_image = preprocess_image(image)
        predicted_class, confidence = predict_class(model, preprocessed_image)

        st.write(f"### Prediction: {predicted_class}")
        st.write(f"### Confidence: {confidence:.2f}")

    st.write("Or capture a new image using the camera below:")
    camera_image = st.camera_input("Take a picture")
    if camera_image is not None:
        image = Image.open(camera_image)
        st.image(image, caption="Captured Image", use_container_width=True)
        st.write("")

        model = load_model()
        preprocessed_image = preprocess_image(image)
        predicted_class, confidence = predict_class(model, preprocessed_image)

        st.write(f"### Prediction: {predicted_class}")
        st.write(f"### Confidence: {confidence:.2f}")
