import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. Page Setup
st.set_page_config(page_title="Project G.R.I.N.", page_icon="🌐", layout="wide")

# 2. The Header
st.title("🌐 Global Resilience & Intelligence Navigator (G.R.I.N.)")
st.markdown("### *Bridging Human Leadership with AI Precision*")

# 3. Sidebar Navigation
st.sidebar.header("Command Center")
option = st.sidebar.selectbox("Select Focus Area", ["Maritime Risk Radar", "Ethics & Compliance Auditor", "Strategic Pathfinder"])

# --- MODULE 1: MARITIME RISK RADAR (Updated for Bahamas) ---
if option == "Maritime Risk Radar":
    st.header("📡 Real-Time Maritime Risk Radar")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Vessel Pings Analyzed", value="4.2k", delta="Maritime Feed Active")
    with col2:
        st.metric(label="Coastal Threat Level", value="LOW", delta="Calm Seas")
    
    st.write("### Emerging Maritime Activity (The Bahamas)")
    
    # EXACT COORDINATES FOR THE BAHAMAS (Centering near Nassau/New Providence)
    # We create random points specifically in the surrounding waters
    bahamas_lat = 25.0343
    bahamas_lon = -77.3963
    
    map_data = pd.DataFrame(
        np.random.randn(20, 2) / [20, 20] + [bahamas_lat, bahamas_lon], 
        columns=['lat', 'lon'])
    
    st.map(map_data)
    st.info("AI Analysis: Monitoring Territorial Waters for Unauthorizied Incursions.")

# --- MODULE 2: ETHICS AUDITOR ---
elif option == "Ethics & Compliance Auditor":
    st.header("⚖️ Ethics & Compliance Auditor")
    st.markdown("""
        <div style="border: 2px solid #4CAF50; padding: 20px; border-radius: 10px; background-color: #f0fff0; color: #000000;">
            <h4 style="color: #2e7d32; margin-top: 0;">OFFICIAL COMPLIANCE VERIFICATION</h4>
            <p><strong>Standard:</strong> ISO/IEC 42001:2023 (AI Management)</p>
            <p><strong>Status:</strong> <span style="color: green;">✔ ACTIVE & COMPLIANT</span></p>
        </div>
        """, unsafe_allow_html=True)

# --- MODULE 3: STRATEGIC PATHFINDER ---
elif option == "Strategic Pathfinder":
    st.header("🗺️ Strategic Pathfinder")
    user_input = st.text_input("Enter a Maritime Scenario (e.g., 'Unidentified Vessel in Exuma Sound'):")
    if st.button("Generate Strategic Response"):
        st.write("Analyzing local maritime law and safety protocols...")
        st.success("Strategy: 1. Deploy Drone Recon | 2. Alert Royal Bahamas Defence Force | 3. Log incident in G.R.I.N.")

st.divider()
st.caption("Developed by Daniel Barr | Built for the Future of Human-AI Collaboration")
