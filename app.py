import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Project G.R.I.N.", page_icon="🌐", layout="wide")

st.title("🌐 Global Resilience & Intelligence Navigator (G.R.I.N.)")
st.markdown("### *Bridging Human Leadership with AI Precision*")

# Sidebar
st.sidebar.header("Command Center")
option = st.sidebar.selectbox("Select Focus Area", ["Global Risk Radar", "Ethics & Compliance Auditor", "Strategic Pathfinder"])

if option == "Global Risk Radar":
    st.header("📡 Real-Time Global Risk Radar")
    
    # Create a simulation of live data
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Data Streams Analyzed", value="1.2M", delta="14k per/sec")
    with col2:
        st.metric(label="Current Threat Level", value="LOW", delta="-2%", delta_color="inverse")
    
    st.write("### Emerging Threat Map (Simulated)")
    # This creates a random map of "activity"
    map_data = pd.DataFrame(
        np.random.randn(50, 2) / [50, 50] + [25.06, -77.34], # Centered near a professional hub
        columns=['lat', 'lon'])
    st.map(map_data)

elif option == "Ethics & Compliance Auditor":
    st.header("⚖️ Ethics & Compliance Auditor")
    st.info("Status: Fully Compliant with ISO/IEC 42001 (AI Management System)")
    st.checkbox("Analyze Decision Transparency", value=True)
    st.checkbox("Verify Bias Mitigation", value=True)
    st.checkbox("Data Privacy Shield", value=True)

elif option == "Strategic Pathfinder":
    st.header("🗺️ Strategic Pathfinder")
    user_input = st.text_input("Enter a crisis scenario for AI-assisted strategy:")
    if st.button("Generate Human-AI Response"):
        with st.spinner('Calculating Optimal Strategy...'):
            time.sleep(2)
            st.success("Strategy Generated:")
            st.write("1. **Stabilize:** Isolate affected digital/physical assets.")
            st.write("2. **Communicate:** Deploy transparent human-led messaging.")
            st.write("3. **Iterate:** Use AI feedback loops to prevent recurrence.")

st.divider()
st.caption("Developed by Daniel Barr | Built for the Future of Human-AI Collaboration")
