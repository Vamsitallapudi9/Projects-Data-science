import streamlit as st 
import pandas as pd 

st.title('Hello Everyone this is my first Web application')
df=pd.read_csv(r"C:\Users\vamsi\Desktop\Pandas_assignment\Pandas_day_1\Iris.csv")

st.dataframe(df)