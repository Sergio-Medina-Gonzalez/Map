import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
df2= pd.read_csv('https://raw.githubusercontent.com/Sergio-Medina-Gonzalez/Map/main/data.csv')
#st.title('My map')
st.map(df)
st.map(df2)
