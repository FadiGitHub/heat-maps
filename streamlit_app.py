import streamlit as st 
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# App title
st.title('Heatmap App')

# File uploader for CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Load data from uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the dataset
    st.write("First few rows of the dataset:")
    st.write(df.head())

    # Display the shape of the dataset
    st.write("Shape of the dataset:")
    st.write(df.shape)

    # Check the column names
    st.write("Column names:")
    st.write(df.columns.tolist())

    # Generate and display the heatmap
    st.subheader('Heatmap')

    # Compute correlation matrix
    corr_matrix = df.corr()

    # Create a Matplotlib figure and plot the heatmap
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap='magma', ax=ax,
                xticklabels=corr_matrix.columns, yticklabels=corr_matrix.index,
                cbar_kws={'orientation': 'vertical'})

    # Display the plot using Streamlit's st.pyplot()
    st.pyplot(fig)