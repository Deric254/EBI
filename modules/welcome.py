import streamlit as st
from utils import navigate_to

def bold_green(msg):
    st.markdown(f"<span style='font-weight:bold;color:#198754;'>{msg}</span>", unsafe_allow_html=True)

def show():
    st.subheader("🧭 Welcome to EBI")
    st.markdown("""
    This console helps you:
    - Browse and explore databases  
    - Preview and audit tables  
    - Clean data for analysis  
    - Run advanced SQL queries  
    - Reset session anytime  

    Built for analysts and admins.  
    Visit [EXES Analytics](https://deric-exes-analytics.netlify.app) to learn more.
    """)
    if st.button("Start →"):
        navigate_to("Navigator")
    #if st.button("Reset →"):
     #   navigate_to("Reset")
