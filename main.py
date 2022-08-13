import streamlit as st
import pandas as pd
import numpy as np
import json


st.sidebar.selectbox(
    "Age"
    "?",
    ("18-20", "20-25", "25-30")
)
st.sidebar.selectbox(
    "Gender"
    "?",
    ("Male", "Female", "Others")
)
st.sidebar.selectbox(
    "Income"
    "?",
    ("20k", "30k", "40k")
)
st.sidebar.selectbox(
    "District"
    "?",
    ("Rajshahi", "Dhaka", "sylhet")
)
st.sidebar.selectbox(
    "Thana"
    "?",
    ("amchottor", "natore", "dhjs")
    #st.write('You selected:', option)
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

if st.sidebar.button('Filter'):

    st.write('result: %s')
col1, col2 = st.columns(2)

with col1:
    st.header("Creavision CRM Panel")
    #st.image("")



with col2:
    st.header("")
    #st.image("")


    #st.image("")
age = st.slider('How many data you need?', 0, 130, 25)
st.write("total", age, 'Data')
col1, col2, col3 = st.columns(3)
col1.metric("DATA", "70 %", "Total Data")
col2.metric("Selected", "900", "-8%")
col3.metric("Message", "86%", "4%")
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)
st.balloons()
st.snow()

title=txt = st.text_input('Enter text: ')
st.write('Start message Campgain', title)

if st.button('Submit'):

    st.write('result: %s')
