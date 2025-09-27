import streamlit as st

# Title of App
st.title("Web Development Lab01")

# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["Home", "Portfolio", "Quiz"])

# Home Page
if page == "Home":
    st.header("CS 1301")
    st.subheader("Web Development - Section X")
    st.subheader("Name")

    st.write("""
    Welcome to our Streamlit Web Development Lab01 app! You can navigate between the pages using the sidebar to the left. The following pages are:

    1. **Portfolio**: All about Justin Palmer  
    2. **Quiz**: Quiz about Justin Palmer
    """)

# Portfolio Page
elif page == "Portfolio":
    st.header("Portfolio")
    st.write("All about Justin Palmer")

# Quiz Page
elif page == "Quiz":
    st.header("Quiz")
    st.write("Take a quiz about Justin Palmer!")
