import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Streamlit app header
st.header("Visualization App")

# Allow users to choose car types or models to display in the histogram
selected_types = st.multiselect("Select Car Types or Models", ['All'] + list(df['type'].unique()))

# Check if "All" is selected
if 'All' in selected_types:
    filtered_df = df  # Display all data if "All" is selected
else:
    filtered_df = df[df['type'].isin(selected_types)]

# Display the scatter plot alongside the histogram
st.write("Histogram and Scatter Plot:")
fig_histogram = px.histogram(filtered_df, x='price', color='type', title='Car Price Distribution by Type')
fig_scatter = px.scatter(filtered_df, x='price', y='type')

st.plotly_chart(fig_histogram)
st.plotly_chart(fig_scatter)
