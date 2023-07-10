import variables as var
import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(var.about_me_img, width=300)

with col2:
    st.title(var.my_title)
    # st.write(content)     # to show text directly
    st.info(var.about_me)  # to show text in a box as info

st.write(var.content2)

# col3, col4 = st.columns(2)
col3, empty_col, col4 = st.columns([3, 1, 3])

dataframe = pandas.read_csv(var.data_file, sep=';')
with col3:
    for index, row in dataframe[:10].iterrows():  # iterrows() is a method to iterate by rows | dataframe[10:] => first 10 items
        st.subheader(row["title"])                   # title is defined in data.csv
        st.write(row["description"])
        st.image(f"images/{row['image']}", width=300)
        st.write(f"[Source Code]({row['url']})")  # this is a link | Text in [] and actual link in ()

with col4:
    for index, row in dataframe[10:].iterrows():  # dataframe[:10] => from 10 to last items
        st.subheader(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}", width=300)
        st.write(f"[Source Code]({row['url']})")