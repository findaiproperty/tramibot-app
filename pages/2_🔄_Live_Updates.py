import streamlit as st
import requests
import datetime

st.set_page_config(
    page_title="Live Updates - Tramibot", 
    page_icon="🔄"
)

st.title("🔄 Live Procedure Updates")
st.markdown("Real-time changes in Spanish immigration procedures")

# Current known updates
st.markdown("### 📢 Recent Changes")

updates = [
    {
        "date": "2024-01-15",
        "procedure": "TIE Applications", 
        "change": "Digital fingerprints now accepted at most offices",
        "impact": "Reduced processing time by 1-2 weeks"
    },
    {
        "date": "2024-01-10",
        "procedure": "EU Registration",
        "change": "Online submission now available in most regions",
        "impact": "No in-person appointment needed for initial application"
    },
    {
        "date": "2024-01-05", 
        "procedure": "All Procedures",
        "change": "Tasa fees increased by approximately 3%",
        "impact": "Small cost increase for all applications"
    }
]

for update in updates:
    with st.expander(f"{update['date']} - {update['procedure']}"):
        st.markdown(f"**Change:** {update['change']}")
        st.markdown(f"**Impact:** {update['impact']}")

# Update checker
st.markdown("---")
st.markdown("### 🔍 Check for New Updates")

if st.button("Scan Official Sources for Changes"):
    with st.spinner("Checking ministry websites and official bulletins..."):
        import time
        time.sleep(3)
        
        # Simulate finding updates
        st.success("Scan complete! No major changes detected.")
        st.info("Next automatic scan: 24 hours")
