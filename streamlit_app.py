import streamlit as st 
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# App title
st.title('Heatmap App')



# Example data (replace with your own data loading logic)
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}


df = pd.DataFrame(data)

# Example heatmap creation
st.subheader('Heatmap')

# Compute correlation matrix
corr_matrix = df.corr()

# Create a Matplotlib figure and plot the heatmap
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)

# Display the plot using Streamlit's st.pyplot()
st.pyplot(fig)

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

