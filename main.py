import joblib
import streamlit as st
import pandas as pd

load_model = joblib.load('5g_resource_model.pkl')
load_scaler = joblib.load('5g_scaler.pkl')

st.title('5G Resource Allocation & QoS Prediction')

st.info('''This application leverages Machine Learning to optimize 5G Resource Allocation.
        Adjust the network parameters in the sidebar to predict the ideal resource ratio and ensure optimal Quality of Service (QoS).''')

app_type = st.sidebar.selectbox('Select Application Type',('Video_Call', 'Voice_Call', 'Streaming', 'Emergency_Service',
                                 'Online_Gaming', 'Background_Download', 'Web_Browsing',
                                 'IoT_Temperature', 'Video_Streaming', 'File_Download', 'VoIP_Call'))

signal_strength = st.sidebar.slider('Signal Strength in dBm',min_value=-123.0, max_value=-40.0, value=-83.0, step=1.0)
required_bw = st.sidebar.slider('Required Bandwidth in Mbps',min_value=0.0, max_value=14.5, value=1.2, step=0.1)
latency = st.sidebar.slider('Latency in Seconds',min_value=0.0 ,max_value=0.11, value=0.03, step=0.01)


if st.button('Predict Resource Allocation'):

    app_columns = ['Emergency_Service','File_Download','IoT_Temperature','Online_Gaming','Streaming',
                   'Video_Call','Video_Streaming','VoIP_Call','Voice_Call','Web_Browsing']
    encoded_data = {col: [0] for col in app_columns}

    selected_column = f'{app_type}'
    if selected_column in encoded_data:
        encoded_data[selected_column] = [1]
    
    readings = {'Signal_Strength(dBm)':[signal_strength],
                'Latency(s)': [latency],
                'Required_Bandwidth(Mbps)': [required_bw]}
    
    readings.update(encoded_data)

    final_df = pd.DataFrame(readings)

    scaled_data = load_scaler.transform(final_df)

    prediction = load_model.predict(scaled_data)[0]

    st.metric(label="Predicted Resource Allocation Ratio", value=f"{prediction:.2%}")
    
    st.progress(min(max(prediction, 0.0), 1.0))
