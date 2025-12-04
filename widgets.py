import streamlit as st
import pandas as pd

st.title("Streamlit text input")

#Creates a text box that takes an input
name = st.text_input("Enter your name:")

#Creates a slider
age = st.slider("Select your age: ", 0, 100, 15)

#Creating a select box
options = ["Python", "Java", "C++", "Javascript"]
choice = st.selectbox("Choose your favorite language: ", options)
st.write(f"You seleted {choice}.")

if name:
    st.write(f"Hello {name}")
    st.write(f"Being {age} is pretty cool")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

#Creates an upload button
uploaded_file = st.file_uploader("Choose a csv file", type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)