import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Streamlit app header
st.header("Car Price Distribution by type")

# Allow users to choose car models to display
selected_models = st.multiselect("Select Car Models to Display", df['model'].unique())

# Filter the dataset based on selected car models
filtered_df = df[df['model'].isin(selected_models)]

# Display the histogram with color-coded models
st.write("Car Price Histogram:")
fig = px.histogram(filtered_df, x='price', color='model', title='Car Price Distribution by model')
st.plotly_chart(fig)
