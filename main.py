import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/winequality-white.csv")
#print(df)
st.set_page_config(page_title="Wine Quality Dashboard",page_icon=":wine_glass:",layout="wide")
st.dataframe(df)
