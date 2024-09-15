# app.py
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate some random data
st.title("Random Data Generation and Visualization")

st.write("Generating random data for demonstration:")

# Generate random data: 100 samples of 5 features (columns)
data = np.random.randn(100, 5)

# Convert to a pandas DataFrame
df = pd.DataFrame(data, columns=['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4', 'Feature 5'])

# Display the generated data
st.write(df)

# Plot the data for better visualization
st.subheader("Line plot of Generated Data")
st.line_chart(df)

# Basic statistics on the generated data
st.subheader("Basic Statistics of Generated Data")
st.write(df.describe())
