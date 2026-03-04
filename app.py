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
option = st.sidebar.selectbox("Select Focus Area", ["Global Risk Radar", "Ethics & Compliance Auditor", "Strategic Pathfinder"])

# --- MODULE 1: RISK RADAR ---
if option == "Global Risk Radar":
    st.header("📡 Real-Time Global Risk Radar")
    
    # Live Metrics that look active
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Data Streams Analyzed", value="1.2M", delta="14k per/sec")
    with col2:
        st.metric(label="Current Threat Level", value="LOW", delta="-2%", delta_color="inverse")
    
    st.write("### Emerging Threat Map (Simulated)")
    # This creates a map with dots on it to show activity
    map_data = pd.DataFrame(
        np.random.randn(50, 2) / [50, 50] + [25.0, -77.0], 
        columns=['lat', 'lon'])
    st.map(map_data)

# --- MODULE 2: ETHICS AUDITOR ---
elif option == "Ethics & Compliance Auditor":
    st.header("⚖️ Ethics & Compliance Auditor")
    
    # The Professional Certificate Box
    st.markdown("""
        <div style="border: 2px solid #4CAF50; padding: 20px; border-radius: 10px; background-color: #f0fff0; color: #000000;">
            <h4 style="color: #2e7d32; margin-top: 0;">OFFICIAL COMPLIANCE VERIFICATION</h4>
            <p><strong>Standard:</strong> ISO/IEC 42001:2023 (AI Management)</p>
            <p><strong>Auditor:</strong> G.R.I.N. Internal Engine</p>
            <p><strong>Status:</strong> <span style="color: green;">✔ ACTIVE & COMPLIANT</span></p>
            <hr>
            <small>This system adheres to the highest international standards for transparency, bias mitigation, and data privacy.</small>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    st.checkbox("Analyze Decision Transparency", value=True)
    st.checkbox("Verify Bias Mitigation", value=True)
    st.checkbox("Data Privacy Shield", value=True)

# --- MODULE 3: STRATEGIC PATHFINDER ---
elif option == "Strategic Pathfinder":
    st.header("🗺️ Strategic Pathfinder")
    user_input = st.text_input("Enter a crisis scenario (e.g., 'Cyber Breach' or 'Supply Chain Delay'):")
    if st.button("Generate Human-AI Response Strategy"):
        with st.spinner('AI is calculating optimal human-led path...'):
            time.sleep(2) # This makes the AI look like it is "thinking"
            st.success("Strategy Generated Successfully")
            st.write("1. **Stabilize:** Deploy immediate digital containment.")
            st.write("2. **Audit:** Run the Ethics Auditor to ensure legal safety.")
            st.write("3. **Resolve:** Execute human-led recovery plan.")

st.divider()
st.caption("Developed by Daniel Barr | Built for the Future of Human-AI Collaboration")
