
import pandas as pd
import streamlit as st
import plotly.express as px
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "Advertising_F.csv"))

st.sidebar.header("Filters")
x_var=st.selectbox("X axis",["TV", "radio", "newspaper"])

#show scatterplot
fig=px.scatter(df, x=x_var, y='sales', 
           labels={'TV':'TV add spend', 'radio':'Radio add spend'})

st.plotly_chart(fig)

#show the barplot
sales_per_city=df.groupby('City')['sales'].sum().reset_index()
fig=px.bar(sales_per_city,x='City',y="sales",title="data is fun")
st.plotly_chart(fig)

#show data frame
st.dataframe(df)
