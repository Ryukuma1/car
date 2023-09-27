import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Streamlit app header
st.header("Visualization App")

# Allow users to choose car types or models to display in the histogram
selected_types = st.multiselect("Select Car Types or Models", df['type'].unique())

# Filter the dataset based on selected car types or models
filtered_df = df[df['type'].isin(selected_types)]

# Check if any selections were made
if len(selected_types) > 0:
    st.write("Histogram:")
    fig = px.histogram(filtered_df, x='price')
    st.plotly_chart(fig)
else:
    st.write("Please select one or more car types or models to display the histogram.")

st.write("Scatter Plot:")
fig = px.scatter(df, x='price', y='type')
st.plotly_chart(fig)
