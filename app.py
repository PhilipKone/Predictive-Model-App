import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set up the title and description
st.title("Random Data Generation and Visualization")
st.write("Use the buttons below to generate random data and view visualizations:")

# Button to generate random data
if st.button('Generate New Data'):
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

    # Additional Button for plotting specific feature
    feature = st.selectbox('Select a feature to plot', df.columns)
    st.subheader(f"Line plot of {feature}")
    st.line_chart(df[[feature]])

else:
    st.write("Press the 'Generate New Data' button to start.")
