import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import streamlit as st #Ui Framework for ml applications

#What is data?'

@st.cache_data 
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns = iris.feature_names)
    df["species"] = iris.target
    return df, iris.target_names

df, target_names = load_data()

model = RandomForestClassifier()
# df[:, :-1] is all features but the last feature (the label)
model.fit(df.iloc[:, :-1], df["species"])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal Length", pd.to_numeric(df["sepal length (cm)"]).min(), pd.to_numeric(df["sepal length (cm)"].max())) 
sepal_width = st.sidebar.slider("Sepal Width", pd.to_numeric(df["sepal width (cm)"]).min(), pd.to_numeric(df["sepal width (cm)"].max()))
petal_length = st.sidebar.slider("Petal Length", pd.to_numeric(df["petal length (cm)"]).min(), pd.to_numeric(df["petal length (cm)"].max()))
petal_width = st.sidebar.slider("petal Width", pd.to_numeric(df["petal width (cm)"]).min(), pd.to_numeric(df["petal width (cm)"].max()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

## Prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")