import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st

# df = pd.read_csv('laptop_data.csv')
st.title('Laptop Price Predictor')

pipe = pickle.load(open('pipe.pkl' , 'rb'))
df = pickle.load(open('df.pkl' , 'rb'))
df_old = pd.read_csv('laptop_data.csv')
st.subheader('Dataset old')
st.write(df_old.head())
st.subheader('model dataset')
st.write(df.head())

st.selectbox('Select Brand/Company Name' , df['Company'].unique() )
st.selectbox('Select Type Name' , df['TypeName'].unique() )
st.selectbox('Select Ram Name' , sorted(df['Ram'].unique().tolist()))
st.selectbox('Select TouchScreen Name' , df['Touchscreen'].unique() )
# weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS
ips = st.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu = st.selectbox('CPU',df['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu brand'].unique())

os = st.selectbox('OS',df['os'].unique())



