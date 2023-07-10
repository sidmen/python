import streamlit as st
from PIL import Image  # pillow module to be imported as PIL

st.subheader("Color to Grayscale Converter")


def converter(image):
    # Create a pillow image instance
    img = Image.open(image)
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")  # L is a notation to set gray scale algorithm | L = R * 299/1000 + G * 587/1000 + B * 114/1000
    # Render the grayscale image on the webpage
    st.image(gray_img)


# Start the camera
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")
    if camera_image:
        converter(camera_image)

# Upload the image
with st.expander("Upload Image"):
    uploaded_image = st.file_uploader("Upload Image")
    if uploaded_image:
        converter(uploaded_image)
