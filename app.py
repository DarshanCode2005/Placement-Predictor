import streamlit as st
import numpy as np
import joblib

# Load the pre-trained model
model = joblib.load('placement_predictor.pkl')

# Streamlit app
st.title('Job Placement Prediction')

# Input bar for user data
user_input = st.text_input('Enter space-separated data:')

def validator(x):
    if (x != 'True') and (x != 'False'):
        return float(x)
    elif x == 'True':
        return True
    else:
        return False

if user_input:
    # Parse the input data
    input_data = np.array([validator(x) for x in user_input.split()]).reshape(1, -1)
    
    # Get predictions from the model
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.write(f'Placement Prediction: {"Placed" if prediction[0] == 1 else "Not Placed"}')