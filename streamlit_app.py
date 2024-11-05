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
        ("https://i.imgur.com/cPHIx8j.jpeg", "These two photos are of one of my classrooms and the school library. Although I don't want to, I will inevitably feel sleepy when I am in class or studying. If I am in the classroom, I will try my best to restrain myself from falling asleep, but my eyelids are out of my control. At this time, I will pinch myself to wake myself up, but it usually doesn't work, and I don't learn anything at all. If I am in the library, I will just lie on the table and sleep until I am no longer sleepy.")
    ]
    
    for img_url, default_description in images:
        if img_url == "https://i.imgur.com/cPHIx8j.jpeg":
            st.image(img_url, width = 500)
            st.write(default_description, key=img_url)
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
    st.write("Creating this website was both an exciting and challenging experience. It allows me to explore and brainstorm my sleeping places and what I did there. Inspired by Georges Perec's Species of Spaces, I wanted to list the places where I have slept, each associated with unique memories and meanings.")
    st.write("I gained a lot when I'm recalling the memories from places I have slept. Each sleeping places brought me memories, not just of because of the place itself, but of how I felt at that time. I realized that even the simplest places carry pieces of my life story, such as the front seat of my car or the subway.")
    st.write("In the process of creating this website, I faced many challenges. One of them is because I recently learned how to use Streamlit. It's the tool I used to build the website. I had to figure out how to display images and make the format look good. I used the file path to store the image first but found out that only I could open the website with the images because the file is local. Next, I tried Google Drive but the images don't show up correctly. After some trial and error, I decided to use Imgur to host the images, which solved the problem.")
    st.write("Another challenge was that the code I wrote wasn't correctly committed to the main git branch, which means the URL didn't reflect my modifications to the website. I tried many methods to solve this problem, but I finally found out that it was just a bug of Streamlit that delayed the detection of updates to the GitHub repository. I was badly battered by this problem since if this really happens, it means that I cannot do anything to the URL so I cannot even do this project.")
    st.write("Overall, this project taught me a lot about sharing personal stories online. It gave me a chance to look back on places that mean something to me, and also made me think about how each of us has these hidden memories connected to everyday places, and how powerful it can be to reflect on them.l it can be to reflect on them.")