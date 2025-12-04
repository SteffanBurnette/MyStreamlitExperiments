import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

@st.cache_data 
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns = iris.feature_names)
    df["species"] = iris.target
    return df, iris.target_names

df, target_names = load_data()

print(len(df))
print(df.describe())