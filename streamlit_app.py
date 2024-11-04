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
        ("https://i.imgur.com/R58idKL.jpeg", "Car interior - A late-night rest in a parked car."),
        ("https://i.imgur.com/16aFnVG.jpeg", "Airport lounge - Awaiting a flight in the calm of a business lounge."),
        ("https://i.imgur.com/xM495Zn.jpeg", "My bedroom - A familiar and comforting place."),
        ("https://i.imgur.com/3oMhe3L.jpeg", "Subway ride - An unexpected nap during transit."),
        ("https://i.imgur.com/KFlMkAv.jpeg", "Lecture hall - Dozing off during a lecture."),
        ("https://i.imgur.com/cPHIx8j.jpeg", "Library - A quiet study space that sometimes turns into a napping spot.")
    ]
    
    for img_url, default_description in images:
        st.image(img_url, use_column_width=True)
        st.text_area("Description", default_description, key=img_url)

# Writer's Memo Page
elif page == "Writer's Memo":
    st.title("Writer's Memo")
    st.write("Provide your thoughts on the creative process here.")
    st.text_area("Memo")
