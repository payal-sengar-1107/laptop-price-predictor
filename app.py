import streamlit as st
import pickle
import numpy as np

# 1. Models aur Dataframe ko load karna
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")

# Dropdowns aur User Input fields
company = st.selectbox('Brand', df['Company'].unique())
type_name = st.selectbox('Type', df['TypeName'].unique())

# RAM options
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

weight = st.number_input('Weight of the Laptop (in kg)', min_value=0.5, max_value=5.0, value=1.5)
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.selectbox('IPS Panel', ['No', 'Yes'])
screen_size = st.number_input('Screen Size (in Inches)', min_value=10.0, max_value=20.0, value=15.6)

resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', 
    '2880x1800', '2560x1600', '2560x1440', '2304x1440'
])

cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())

# HDD aur SSD options
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())
os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    # Input formatting
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # PPI calculation
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    Y_res2 = Y_res
    ppi = ((X_res*2) + (Y_res2))*0.5 / screen_size

    import pandas as pd

    query_df = pd.DataFrame([{
        'Company': company,
        'TypeName': type_name,
        'Ram': ram,
        'Weight': weight,
        'Touchscreen': touchscreen,
        'Ips': ips,
        'ppi': ppi,
        'Cpu brand': cpu,
        'HDD': hdd,
        'SSD': ssd,
        'Gpu brand': gpu,
        'os': os
    }])

    predicted_price = int(np.exp(pipe.predict(query_df)[0]))
    st.success(f"The predicted price of this configuration is: ₹{predicted_price}")
