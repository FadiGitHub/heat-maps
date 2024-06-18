import streamlit as st 
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# App title
st.title('Heatmap App')

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    # Example heatmap creation
    st.subheader('Heatmap')
    heatmap_data = df.corr()  # Example correlation heatmap

    # Plot heatmap using seaborn
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_data, annot=True, cmap='coolwarm')
    st.pyplot()