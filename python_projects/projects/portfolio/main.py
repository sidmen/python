import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=300)

with col2:
    st.title("Sidharth Menon")
    about_me = """
    Hi, I am Sidharth Menon.  \n
    I am trying to learn Python
    """
    # st.write(content)     # to show text directly
    st.info(about_me)  # to show text in a box as info

content2 = """ Below you will find the projects I built using Python. 
                Please feel free to contact me for more info """
st.write(content2)