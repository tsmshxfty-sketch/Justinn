import streamlit as st
import random  # Add this if you use random choices in scoring

st.title("🐾 What Type of Dog Are You?")  # Quiz Title
st.write("Take this fun BuzzFeed-style quiz to find out what kind of dog matches your personality!")

# Question 1 - Multiple Choice
q1 = st.radio(  # NEW
    "What's your ideal weekend activity?",
    ["Hiking in the mountains", "Binge-watching Netflix", "Going to a party", "Sleeping all day"]
)

# Question 2 - Multi-select
q2 = st.multiselect(  # NEW
    "Pick your favorite snacks:",
    ["Pizza", "Ice Cream", "Salad", "Burgers", "Sushi"]
)

# Question 3 - Number Input
q3 = st.number_input(  # NEW
    "How many hours of sleep do you usually get?",
    min_value=0, max_value=24, step=1
)

# Question 4 - Slider
q4 = st.slider(
    "How much do you enjoy meeting new people?",
    min_value=0, max_value=10, value=5
)

# Question 5 - Selectbox
q5 = st.selectbox(
    "Pick a vacation destination:",
    ["Beach", "Mountains", "City", "Countryside"]
)

# Images (local file or URL)
st.image("Images/dog.jpeg", caption="A playful puppy 🐕")
st.image("Images/images.jpeg", caption="A sleepy dog 😴")
st.image("Images/imogyou.jpeg", caption="An adventurous husky ❄️")

# Button to get results
if st.button("Get My Result!"):
    score = 0
    if q1 == "Hiking in the mountains":
        score += 3
    elif q1 == "Binge-watching Netflix":
        score += 1
    elif q1 == "Going to a party":
        score += 2
    else:
        score += 0

    score += len(q2)  # snacks add to personality points
    score += q3 // 3  # more sleep = calmer dog
    score += q4

    # Simple scoring logic
    if score < 10:
        st.success("You’re a **Bulldog** – calm, loyal, and love your rest! 🐶")
    elif score < 20:
        st.success("You’re a **Golden Retriever** – friendly, outgoing, and always positive! 🐕")
    else:
        st.success("You’re a **Husky** – adventurous, energetic, and full of life! ❄️")

    st.balloons()  # NEW 🎈
