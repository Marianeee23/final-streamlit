import joblib
import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
from img2vec_pytorch import Img2Vec
from sklearn.exceptions import NotFittedError
from sklearn.utils.validation import check_is_fitted

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_title="👟Shoes Brand Classification Model 👟")

# Function to load the model
def load_model():
    try:
        model = joblib.load('pages/shoes.p')
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please upload the model file.")
        return None
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Function to check if the model is fitted
def is_model_fitted(model):
    try:
        check_is_fitted(model)
        return True
    except NotFittedError:
        return False

# Load the model
model = load_model()

# Initialize Img2Vec
img2vec = Img2Vec()

# Streamlit Web App Interface
st.write("##  👟Shoes Brand Classification Model 👟")
st.write("Upload an image of shoes, and we'll predict its brand based on our trained model!")
st.write("Prediction is limited to the brand of Adidas and Nike.")
st.sidebar.write("## Upload and Download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Function to convert the image to bytes
@st.cache_data
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    return byte_im

# Function to process and predict the uploaded image
def fix_image(upload):
    image = Image.open(upload)
    col1.image(image, caption="Uploaded Image", use_column_width=True)

    if model is not None and is_model_fitted(model):
        col2.write("### Predicted Classification :wrench:")
        features = img2vec.get_vec(image)
        try:
            pred = model.predict([features])
            col2.header(pred[0])
        except Exception as e:
            col2.error(f"Error during prediction: {e}")
    else:
        col2.error("The model is not fitted or not loaded correctly. Please check the model status.")

# Streamlit columns for displaying the image and prediction
col1, col2 = st.columns(2)

# File uploader in the sidebar
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Handling the uploaded file
if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    st.write("## Welcome!")
    st.write("Upload an image to get started.")
    st.write("by Mariane Tumbagahan.")
