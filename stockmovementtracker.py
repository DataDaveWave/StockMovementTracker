import streamlit as st
import requests

# Your Raw Gist URL
SECRET_LOGIC_URL = "https://gist.githubusercontent.com/DataDaveWave/c9880ea215c310126e8960ae82dbbb21/raw/stockmovementtracker.py"

try:
    response = requests.get(SECRET_LOGIC_URL, timeout=15)
    if response.status_code == 200:
        exec(response.text)
    else:
        st.error(f"Logic Load Failed. Status: {response.status_code}")
except Exception as e:
    st.error("Engine Connection Error")
    st.exception(e)