import streamlit as st
import pandas
import variables as var

st.set_page_config(layout='wide')

st.title(var.title)

st.write(var.content1)

st.subheader("Our Team")

dataframe = pandas.read_csv(var.data_file)   # sep argument is not required as comma is default value for separator

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in dataframe[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in dataframe[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in dataframe[8:12].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")