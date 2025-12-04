import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("The beggining of streamlit")

# Displaying simple text
st.write("The simpler the text the better the product")

# Creating a simple dataframe
df = pd.DataFrame({
    "first_col": [1, 2, 3, 4],
    "second_col": [10, 20, 30, 40]
})

# Displaying the dataframe
st.write("This is the dataframe")
st.write(df)

# Creating a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns = ["a", "b", "c"]
)
st.line_chart(chart_data)

