import streamlit as st
import requests
import time

# 1. SET PAGE CONFIG (Must be the very first Streamlit command)
st.set_page_config(page_title="Radar", layout="wide", initial_sidebar_state="collapsed")

# 2. THE ULTRA-COMPACT CSS
st.markdown("""
    <style>
    /* Kill the top header and the 'Deploy' button area */
    [data-testid="stHeader"] {display: none !important;}
    
    /* Pull the content container to the absolute top */
    .main .block-container {
        padding-top: 0px !important;
        margin-top: -70px !important; 
    }
    
    /* Optional: Shrink sidebar width for mobile */
    [data-testid="stSidebar"] { width: 200px !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. TINY HEADER
st.write("### 📈 Radar")

# 4. FETCH ENGINE
SECRET_LOGIC_URL = "https://gist.githubusercontent.com/DataDaveWave/c9880ea215c310126e8960ae82dbbb21/raw/stockmovementtracker.py"

try:
    # Cache buster ensures you don't see old code after updating the Gist
    cache_buster = f"?v={int(time.time())}"
    response = requests.get(SECRET_LOGIC_URL + cache_buster, timeout=15)
    
    if response.status_code == 200:
        # Runs your "Card" logic from the Gist
        exec(response.text)
    else:
        st.error(f"Engine Offline ({response.status_code})")
        
except Exception as e:
    st.error("Engine Connection Error")
    st.exception(e)
