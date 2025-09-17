!pip install streamlit -q
!pip install pyngrok
!pip install google-generativeai


import streamlit as st
import pandas as pd
import numpy as np
import time
from pyngrok import ngrok
from subprocess import Popen, PIPE
import os
import google.generativeai as genai
from collections import Counter
import random

NGROK_AUTH_TOKEN = "3295Ynds2US1avvZXcObE2SiSCv_VKzSVzHdhPJapQM9EUuJ"
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

print("Setup complete. Now run the second cell to create and launch the web app.")

%%writefile app.py
import streamlit as st
import pandas as pd
import numpy as np
import time
import random

st.markdown("""
    <style>
        .main-header { font-size: 2.5rem; color: #1a56db; text-align: center; font-weight: bold; }
        .section-header { font-size: 1.8rem; color: #333; border-bottom: 2px solid #1a56db; }
        .metric-card { background-color: #f9f9f9; border-radius: 8px; padding: 15px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-header'>🩺 HealthAI - Intelligent Healthcare Assistant</div>", unsafe_allow_html=True)
st.sidebar.title("Patient Profile")

with st.sidebar:
    st.text_input("Name", "Rithvik")
    st.number_input("Age", 0, 120, 22)
    st.selectbox("Gender", ["Male", "Female", "Other"])
    st.text_area("Medical History", "None")

tab1, tab2, tab3, tab4 = st.tabs(["Disease Prediction", "Treatment Plan", "Patient Support", "Health Dashboard"])

with tab1:
    st.markdown("<div class='section-header'>🔬 Disease Prediction System</div>", unsafe_allow_html=True)
    symptoms = st.text_area("Current Symptoms", "Dry cough, shortness of breath...")
    if st.button("Generate Prediction"):
        if not symptoms:
            st.warning("Please describe your symptoms.")
        else:
            with st.spinner("Generating prediction..."):
                time.sleep(2)
                predictions = ["COVID-19", "Bronchitis", "Pneumonia"]
                st.subheader("Potential Conditions")
                for i, pred in enumerate(random.sample(predictions, 3)):
                    st.write(f"{i+1}. **{pred}**")

with tab2:
    st.markdown("<div class='section-header'>📝 Personalized Treatment Plan Generator</div>", unsafe_allow_html=True)
    condition = st.text_input("Medical Condition", "Mouth Ulcer")
    if st.button("Generate Treatment Plan"):
        if not condition:
            st.warning("Please enter a medical condition.")
        else:
            with st.spinner("Generating plan..."):
                time.sleep(2)
                st.subheader("Personalized Treatment Plan")
                st.markdown("1. Recommended medications: Use antiseptic mouthwash...")

with tab3:
    st.markdown("<div class='section-header'>💬 24/7 Patient Support</div>", unsafe_allow_html=True)
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask your health question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                time.sleep(2)
                response_text = "I am an AI assistant and cannot provide medical advice."
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})

with tab4:
    st.markdown("<div class='section-header'>📊 Health Analytics Dashboard</div>", unsafe_allow_html=True)
    st.subheader("Health Metrics Summary")
    c1, c2, c3 = st.columns(3)
    c1.metric("Avg. Heart Rate", "74.0 bpm")
    c2.metric("Avg. Blood Pressure", "120.8/79.9")
    c3.metric("Avg. Blood Glucose", "101.2 mg/dL")
    st.line_chart(np.random.normal(75, 5, 90).cumsum())

import streamlit as st
from pyngrok import ngrok
from subprocess import Popen, PIPE
import time

try:
    
    proc = Popen(['streamlit', 'run', 'app.py', '--server.port=8501'], stdout=PIPE, stderr=PIPE)
    time.sleep(5)  
    
    public_url = ngrok.connect(8501)
    
    print("Your Streamlit app is ready!")
    print(f"URL: {public_url}")

except Exception as e:
    print(f"Error starting Streamlit: {e}")
