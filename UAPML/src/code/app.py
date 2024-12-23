import streamlit as st
from cnn import cnn_predict  # Impor fungsi utama untuk CNN
from vgg19 import vgg19_predict  # Impor fungsi utama untuk VGG19

# Fungsi utama untuk navigasi aplikasi
def main():
    st.set_page_config(
        page_title="Eye Disease Classification",
        page_icon="👁️",
        layout="wide"
    )

    # Header aplikasi
    st.title("Eye Disease Classification")
    st.sidebar.title("Navigation")
    st.sidebar.write("Use the sidebar to navigate between models.")

    # Navigasi model
    app_mode = st.sidebar.selectbox(
        "Choose Model:",
        ["Home", "CNN Model", "VGG19 Model"]
    )

    if app_mode == "Home":
        st.write("""
        ## Welcome to the Eye Disease Classification App! 👁️
        This application classifies eye diseases into the following categories:
        - **Cataract**
        - **Diabetic Retinopathy**
        - **Glaucoma**
        - **Normal**
        
        ### Features:
        - Use **CNN** or **VGG19** models to classify images.
        - Upload retina images or capture using your camera.
        - View prediction results with confidence scores.
        
        Navigate to the desired model using the sidebar.
        """)

    elif app_mode == "CNN Model":
        st.header("CNN Model Prediction")
        cnn_predict()  # Panggil fungsi dari cnn.py

    elif app_mode == "VGG19 Model":
        st.header("VGG19 Model Prediction")
        vgg19_predict()  # Panggil fungsi dari vgg19.py

# Jalankan aplikasi
if __name__ == "__main__":
    main()
