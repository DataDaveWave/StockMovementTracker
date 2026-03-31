import streamlit as st
import requests
import time

# 1. SET PAGE CONFIG (Auto allows it to collapse on mobile)
st.set_page_config(page_title="Radar", layout="wide", initial_sidebar_state="auto")

# 2. THE TOP-SPACE KILLER (Preserves Sidebar Button)
st.markdown("""
    <style>
    /* Hide the 'Deploy' button and the thick header bar */
    header[data-testid="stHeader"] { 
        background: transparent !important;
        height: 2rem !important;
    }
    
    /* Pull content up, but leave 2rem of space for the sidebar toggle */
    .main .block-container {
        padding-top: 0px !important;
        margin-top: -65px !important; 
    }
    
    /* Custom Thin Title */
    .thin-title {
        font-size: 1.1rem;
        font-weight: 800;
        margin-bottom: 5px;
        border-bottom: 1px solid #eee;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    </style>
    <div class="thin-title">📈 Radar</div>
    """, unsafe_allow_html=True)

# 3. FETCH ENGINE
SECRET_LOGIC_URL = "https://gist.githubusercontent.com/DataDaveWave/c9880ea215c310126e8960ae82dbbb21/raw/stockmovementtracker.py"

try:
    cache_buster = f"?v={int(time.time())}"
    response = requests.get(SECRET_LOGIC_URL + cache_buster, timeout=15)
    if response.status_code == 200:
        exec(response.text)
    else:
        st.error("Engine Load Error")
except Exception as e:
    st.error("Connection Failed")
