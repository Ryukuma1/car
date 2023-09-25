import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header("Visualization App")

show_histogram = st.checkbox("Show Histogram")

if show_histogram:
    st.write("Histogram:")
    fig = px.histogram(df, x='price')
    st.plotly_chart(fig)

st.write("Scatter Plot:")
fig = px.scatter(df, x='price', y='type')
st.plotly_chart(fig)