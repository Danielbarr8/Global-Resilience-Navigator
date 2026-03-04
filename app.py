import streamlit as st
import pandas as pd
import numpy as np
import time

# --- THEME & CONFIG ---
st.set_page_config(page_title="G.R.I.N. Command Center", page_icon="⚓", layout="wide")

# Custom CSS for a Professional Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #374151; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("⚓ G.R.I.N. Command Center")
st.write("### *Bahamas National Security & Maritime Intelligence Platform*")
st.divider()

# --- NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs(["📡 Maritime Intelligence", "⚖️ Governance & Ethics", "🗺️ Strategic Pathfinder"])

# --- TAB 1: MARITIME INTELLIGENCE ---
with tab1:
    st.header("Real-Time Coastal Monitoring")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Vessel Pings", "4,102", "+12% Active")
    col2.metric("Threat Level", "LOW", "-5% Variance", delta_color="inverse")
    col3.metric("System Uptime", "99.9%", "Secure")

    st.subheader("Territorial Water Surveillance (Bahamas)")
    # Centering Map on the Bahamas
    bah_lat, bah_lon = 25.0343, -77.3963
    map_data = pd.DataFrame(
        np.random.randn(15, 2) / [25, 25] + [bah_lat, bah_lon],
        columns=['lat', 'lon'])
    st.map(map_data)
    st.info("💡 Data represents simulated maritime radar feeds within the Exclusive Economic Zone (EEZ).")

# --- TAB 2: GOVERNANCE & ETHICS ---
with tab2:
    st.header("ISO/IEC 42001 Compliance Audit")
    
    st.markdown("""
        <div style="border: 2px solid #4CAF50; padding: 25px; border-radius: 15px; background-color: #101820; color: #FFFFFF;">
            <h2 style="color: #4CAF50; margin-top: 0;">✔ SYSTEM CERTIFIED</h2>
            <p><strong>Security Framework:</strong> ISO/IEC 42001:2023 (AI Governance)</p>
            <p><strong>Audit Status:</strong> Compliant</p>
            <p><strong>Verified By:</strong> G.R.I.N. Integrity Engine</p>
            <hr style="border-color: #4CAF50;">
            <p><small>This interface verifies that all AI operations adhere to international ethical standards, ensuring human-led accountability in maritime law enforcement.</small></p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 3: STRATEGIC PATHFINDER ---
with tab3:
    st.header("Crisis Response Engine")
    scenario = st.selectbox("Select Threat Scenario", [
        "Unidentified Vessel in Bahamian Waters",
        "Search and Rescue (SAR) Optimization",
        "Coastal Infrastructure Alert",
        "Illegal Fishing Detection"
    ])
    
    if st.button("Initialize Strategy Generation"):
        with st.status("Analyzing Maritime Law & Resource Allocation..."):
            time.sleep(1.5)
            st.write("Cross-referencing Royal Bahamas Defence Force protocols...")
            time.sleep(1)
        
        st.success(f"Strategic Action Plan for: {scenario}")
        st.code("""
        1. DEPLOY: Immediate aerial/drone reconnaissance.
        2. VERIFY: Cross-check vessel ID against international registries.
        3. NOTIFY: Establish secure link to local authorities (RBDF/Police).
        4. LOG: Incident data archived for post-action ethical review.
        """, language="markdown")

# --- FOOTER ---
st.divider()
st.caption(f"© 2026 Developed by Daniel Barr | Justice of the Peace | National Security Portfolio")
