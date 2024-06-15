import streamlit as st


st.header('Image Classification Source Code')
st.subheader('This python code is implemented for Streamlit')
st.code(''' 
        
import joblib
import streamlit as st
import pandas as pd
from nltk.corpus import names
from PIL import Image
from io import BytesIO
from img2vec_pytorch import Img2Vec
from sklearn.exceptions import NotFittedError
from sklearn.utils.validation import check_is_fitted
import torch
from torchvision.models import resnet18
import os

st.set_page_config(layout="wide", page_title="Image Classification for Shoes Brand")

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
class Img2Vec:
    def __init__(self):
        try:
            # Check if resnet18.pth exists, then load it
            if os.path.exists('resnet18.pth'):
                self.model = resnet18(pretrained=False)
                self.model.load_state_dict(torch.load('resnet18.pth'))
                self.model.eval()
                self.extraction_layer = -1  # Example extraction layer, adjust as needed
            else:
                self.model = None  # Placeholder or default behavior when file is missing
                st.warning("resnet18.pth not found. Using default behavior for Img2Vec.")
        except Exception as e:
            st.error(f"Error initializing Img2Vec: {e}")

    def get_vec(self, image):
        if self.model is None:
            return None  # Handle gracefully if model is not initialized
        try:
            # Process image and get features
            # Example code, adjust based on img2vec-pytorch usage
            img = Image.open(image).convert('RGB')
            img = img.resize((224, 224))  # Resize as per model requirement
            tensor = transforms.ToTensor()(img)
            with torch.no_grad():
                feature = self.model(tensor.unsqueeze(0))
            return feature.squeeze().numpy()  # Example return, adjust as needed
        except Exception as e:
            st.error(f"Error getting image features: {e}")
            return None

# Streamlit Web App Interface
st.write("##  👟Shoes Brand Classification Model 👟")
st.write("Upload an image of shoes, and we'll predict its brand based on our trained model!")
st.write("Prediction is limited to the brand of Adidas and Nike")
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
    col1.write("### Image to be Predicted :camera:")
    col1.image(image, use_column_width=True)

    col2.write("### Brand Predicted: :wrench:")
    features = img2vec.get_vec(image)
    try:
        if features is not None and model is not No



    

        ''')
