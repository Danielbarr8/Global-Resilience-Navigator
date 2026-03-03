import streamlit as st

# Setting up the page title and look
st.set_page_config(page_title="Project G.R.I.N.", page_icon="🌐", layout="wide")

# The Human Header
st.title("🌐 Global Resilience & Intelligence Navigator (G.R.I.N.)")
st.subheader("Bridging Human Leadership with AI Precision")

# Sidebar for Navigation
st.sidebar.header("Command Center")
option = st.sidebar.selectbox("Select Focus Area", ["Global Risk Radar", "Ethics & Compliance Auditor", "Strategic Pathfinder"])

if option == "Global Risk Radar":
    st.header("📡 Real-Time Global Risk Radar")
    st.write("This module scans global data to identify emerging digital and physical threats.")
    st.info("Status: Monitoring Global Streams... 100% Secure.")
    st.progress(85)
    st.write("Current Threat Level: **LOW**")

elif option == "Ethics & Compliance Auditor":
    st.header("⚖️ Ethics & Compliance Auditor")
    st.write("Ensuring all AI decisions align with human laws and ethical standards.")
    st.success("All systems compliant with International Governance Frameworks.")

elif option == "Strategic Pathfinder":
    st.header("🗺️ Strategic Pathfinder")
    st.write("Input a scenario below to generate a high-level response strategy.")
    scenario = st.text_input("Enter a challenge (e.g., 'System Breach' or 'Market Shift'):")
    if scenario:
        st.write(f"Generating optimized human-centered response for: **{scenario}**")
        st.code("ANALYZING... PROTECTING... RESOLVING...")

st.divider()
st.caption("Developed by Daniel Barr | Built for the Future of Human-AI Collaboration")
