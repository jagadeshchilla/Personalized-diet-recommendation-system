from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to DietDynamo!👋")

st.sidebar.success("Select a recommendation app.")

# Importing the image from another file
image = Image.open("D:\project files\Diet recommendation system\logo.png")
image_resized = image.resize((50, 50))
st.image(image, caption="DietDynamo Logo", use_column_width=True)

st.markdown(
    """
    DietDynamo is an innovative diet recommendation system powered by advanced algorithms and personalized data analysis.
    It utilizes cutting-edge technology to provide tailored dietary plans, taking into account factors such as individual preferences, health goals, lifestyle, and even real-time data like activity levels and metabolic rates. 
    With its dynamic approach, DietDynamo empowers users to make informed choices and achieve sustainable results on their journey towards better health and nutrition.
    A diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
    You can find more details and the whole project on my [repo](https://github.com/jagadeshchilla/personalized-diet-recommendation).
    """
)
