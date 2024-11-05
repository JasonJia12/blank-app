import streamlit as st
from PIL import Image

# Title of the website
st.set_page_config(page_title="Creative Project: 'Places I've Slept'", layout="wide")
# Sidebar Navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Introduction", "Content", "Writer's Memo"])

# Introduction Page
if page == "Introduction":
    st.markdown("### English 140")
    st.title("Welcome to 'Places I've Slept'")
    st.write("""
    This website is a creative exploration inspired by Georges Perec's Species of Spaces. Each place I’ve slept holds a story—a unique memory tied to a specific time and feeling. In this project, I’ve documented various sleeping spaces I’ve experienced, capturing not only the physical locations but also the atmosphere and personal reflections associated with each. Why did I sleep there? Who was I with? Why is this place meaningful to me? I invite you to explore these spaces and reflect on your own experiences with places you've rested.
    """)

# Content Page
elif page == "Content":
    st.title("Places I've Slept")
    st.write("")
    st.markdown("### Below are various places I've slept, each accompanied by a photo and a personal reflection.")
    st.write("")
    st.write("")

    # Display each image with a text area for description
    images = [
        ("https://i.imgur.com/R58idKL.jpeg", "This is where I slept throughout the second half of my high school career. Yes, you heard it right, on the front seat of my Subaru. Since I got this car, every lunch break, I would come to my car, lay the seat flat, use my own hands as a pillow, and start a wonderful nap time. Sometimes, if I am really hungry, I will drive my car to buy some food and then come back to take a nap. Sometimes, if I have an exam in the afternoon, I will sit on it to review. This is like my warm little nest. No matter how school goes or what happens, as long as I lie down here, my soul will be comforted."),
        ("https://i.imgur.com/16aFnVG.jpeg", "I am very familiar with this place, although it is neither my hometown nor the place where I go to school. But I appear here almost every year. Since the outbreak of the epidemic, there are very few direct flights between China and the United States. If I want to go home or come back to school, the most convenient way is to transfer, so Seoul Incheon International Airport has become one of my must-go routes. Every time I transfer here, I cherish my time here very much when I think about the next ten hours of flight. Whether I have to stay here for two hours, three hours or ten hours, I will find a quiet and comfortable place in the business lounge, lie down and take a nap, and prepare for my next tiring journey."),
        ("https://i.imgur.com/xM495Zn.jpeg", "This is my bed in Madison. I have slept in many beds. As a student who loves to travel and go to school in a foreign country, I have slept in almost all beds in the world, whether it's my home, a hotel, a dorm, or an Airbnb. There are comfortable beds, hard beds, beds that I fall asleep immediately, and beds that keep me awake all night. I have different memories in different beds, and I have experienced different things on different nights in the same bed. Every bed is unique to me."),
        ("https://i.imgur.com/3oMhe3L.jpeg", "This is the interior of Beijing Subway Line 10. This is also the place where I slept most during middle school, apart from my bed at home. Beijing is a big city, but the road planning of this big city is obviously not very good. During the morning rush hour every day, if I don’t leave by car two hours in advance, I will be late. So in order to let myself sleep more, I choose to take the subway to and from school, because the speed of the subway will not change. Although the hard seat is very uncomfortable for me and there is no place to support my head, who doesn’t want to take a nap on the way to work? (If I can grab a seat in the morning rush hour crowd)"),
        ("https://i.imgur.com/KFlMkAv.jpeg",""),
        ("https://i.imgur.com/cPHIx8j.jpeg", "Library - A quiet study space that sometimes turns into a napping spot.")
    ]
    
    for img_url, default_description in images:
        if img_url == "https://i.imgur.com/cPHIx8j.jpeg":
            st.image(img_url, width = 500)
        else: 
            st.image(img_url, use_column_width=True)
            st.write(default_description, key=img_url)
            st.write("")
            st.write("")
            st.write("")
            st.write("")

# Writer's Memo Page
elif page == "Writer's Memo":
    st.title("Writer's Memo")
    st.write("")
