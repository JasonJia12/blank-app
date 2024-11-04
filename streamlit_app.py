import streamlit as st
from PIL import Image

# Title of the website
st.set_page_config(page_title="Creative Project: Places I've Slept", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Introduction", "Content", "Writer's Memo"])

# Introduction Page
if page == "Introduction":
    st.title("Welcome to 'Places I've Slept'")
    st.write("""
    This website is a creative exploration inspired by Georges Perec's *Species of Spaces*. 
    Each place we sleep has a story, a unique memory tied to a time and a feeling. In this project, 
    I've documented different sleeping spaces I've experienced, capturing not only the physical locations 
    but the atmosphere and personal reflections associated with them. I invite you to explore these spaces 
    and consider your own experiences with places you've rested.
    """)

# Content Page
elif page == "Content":
    st.title("Places I've Slept")
    st.write("Below are various places I've slept, each accompanied by a photo and a personal description.")

    # Display each image with a text area for description
    images = [
        ("/mnt/data/4S4WMAWDXR3424792--06.jpg", "Car interior - A late-night rest in a parked car."),
        ("/mnt/data/Asiana-Business-Lounge-Seoul-Incheon-West-ICN-Review-6.jpeg", "Airport lounge - Awaiting a flight in the calm of a business lounge."),
        ("/mnt/data/WechatIMG105.jpg", "My bedroom - A familiar and comforting place."),
        ("/mnt/data/WechatIMG106.jpg", "Subway ride - An unexpected nap during transit."),
        ("/mnt/data/WechatIMG110.jpg", "Lecture hall - Dozing off during a lecture."),
        ("/mnt/data/WechatIMG111.jpg", "Library - A quiet study space that sometimes turns into a napping spot.")
    ]
    
    for img_path, default_description in images:
        image = Image.open(img_path)
        st.image(image, use_column_width=True)
        st.text_area("Description", default_description, key=img_path)

# Writer's Memo Page
elif page == "Writer's Memo":
    st.title("Writer's Memo")
    st.write("Provide your thoughts on the creative process here.")
    st.text_area("Memo")
