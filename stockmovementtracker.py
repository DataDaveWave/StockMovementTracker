import streamlit as st
import requests

# 1. Page Config must be the very first Streamlit command
st.set_page_config(page_title="Stock Movement Tracker", layout="wide")
st.title("📈 Stock Movement Tracker")

# 2. Your RAW Gist URL
SECRET_LOGIC_URL = "https://gist.githubusercontent.com/DataDaveWave/c9880ea215c310126e8960ae82dbbb21/raw/stockmovementtracker.py"

# 3. Fetch and Execute the engine
try:
    # Adding a cache-buster at the end of the URL to ensure it always pulls the latest Gist version
    import time
    cache_buster = f"?v={int(time.time())}"
    
    response = requests.get(SECRET_LOGIC_URL + cache_buster, timeout=15)
    
    if response.status_code == 200:
        # This executes the Gist code inside this script's memory
        exec(response.text)
    else:
        st.error(f"Engine Load Failed (Status {response.status_code}). Please check Gist availability.")
        
except Exception as e:
    st.error("Fatal Error Connecting to Engine.")
    st.exception(e)
