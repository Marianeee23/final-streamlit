import streamlit as st

st.title("Description of Different Streamlit Application")


st.header('Simple Sentiment Analyzer App')
st.image("./picture/s2.jpg")

with st.expander("🔮Sentiment Analyzer"):
    st.markdown("""
    
    #
                A Sentiment Analyzer 
A Sentiment Analyzer is a computational tool designed to determine the sentiment expressed in a piece of text. It leverages natural language processing (NLP) and machine learning algorithms to categorize text as positive, negative, or neutral. This tool is widely used in applications like social media monitoring, customer feedback analysis, and market research to gauge public opinion, improve customer service, and inform strategic decisions. By analyzing sentiment at scale, organizations can quickly identify trends and respond to the emotional tone of their audience.







    """, unsafe_allow_html=True)

st.header('Image Classification')
st.image("./picture/s3.jpg")

with st.expander("Shoes Image Classification Project"):
    st.markdown("""
    
    #
                Image Classification
    Image classification is a computer vision task where a machine learning model assigns a label to an image based on its visual content. This process involves training the model on a dataset of labeled images, enabling it to recognize patterns and features associated with specific categories. Applications of image classification include identifying objects in photos, diagnosing medical images, and enabling autonomous vehicles to detect and interpret their surroundings.
                
    """, unsafe_allow_html=True)

st.header('🔍Prediction')
st.image("./picture/s1.jpg")

with st.expander("Prediction "):
    st.markdown("""
    
    #
                Prediction 
This project aims to predict Oscar award winners by analyzing historical data from Kaggle. By leveraging quantitative methods and machine learning algorithms, we will identify patterns and key factors that influence award outcomes. The dataset includes features such as film genre, director, cast, budget, box office performance, and previous award wins. Our goal is to build a predictive model that accurately forecasts future Oscar winners, providing valuable insights for filmmakers, studios, and enthusiasts.







    """, unsafe_allow_html=True)