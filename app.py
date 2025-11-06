import streamlit as st
import requests
import time
import datetime

# Page configuration
st.set_page_config(
    page_title="Tramibot - Free Appointment Alerts",
    page_icon="🚀",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .status-online {
        padding: 20px;
        background-color: #d4edda;
        border: 2px solid #c3e6cb;
        border-radius: 10px;
        text-align: center;
        margin: 20px 0;
    }
    .status-offline {
        padding: 20px;
        background-color: #f8d7da;
        border: 2px solid #f5c6cb;
        border-radius: 10px;
        text-align: center;
        margin: 20px 0;
    }
    .check-button {
        display: block;
        width: 100%;
        padding: 15px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1.2rem;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🚀 Tramibot</div>', unsafe_allow_html=True)
st.subheader("Free Spanish Appointment Alerts")

# Initialize session state
if 'last_checked' not in st.session_state:
    st.session_state.last_checked = "Never"
if 'system_status' not in st.session_state:
    st.session_state.system_status = "unknown"

def check_appointment_system():
    """Check if the appointment system is accessible"""
    try:
        response = requests.get(
            'https://sede.administracionespublicas.gob.es/icpplus/',
            timeout=10
        )
        return response.status_code == 200
    except:
        return False

# Main dashboard
col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Check System Now", use_container_width=True):
        with st.spinner("Checking appointment system..."):
            is_online = check_appointment_system()
            st.session_state.system_status = "online" if is_online else "offline"
            st.session_state.last_checked = datetime.datetime.now().strftime("%H:%M:%S")

with col2:
    st.link_button(
        "📅 Go to Official Booking", 
        "https://sede.administracionespublicas.gob.es/icpplus/",
        use_container_width=True
    )

# Display status
st.markdown("---")

if st.session_state.system_status == "online":
    st.markdown(
        f'<div class="status-online">'
        f'<h3>✅ SYSTEM ONLINE</h3>'
        f'<p>Appointment system is accessible!</p>'
        f'<small>Last checked: {st.session_state.last_checked}</small>'
        f'</div>',
        unsafe_allow_html=True
    )
    st.balloons()
    
elif st.session_state.system_status == "offline":
    st.markdown(
        f'<div class="status-offline">'
        f'<h3>❌ SYSTEM OFFLINE</h3>'
        f'<p>Appointment system may be down</p>'
        f'<small>Last checked: {st.session_state.last_checked}</small>'
        f'</div>',
        unsafe_allow_html=True
    )
else:
    st.info("Click 'Check System Now' to see current status")

# Auto-refresh
st.markdown("---")
st.markdown("### 🔄 Auto-Refresh Status")
auto_refresh = st.checkbox("Check every 5 minutes")

if auto_refresh:
    st.write("Auto-refresh enabled - next check in 5 minutes")
    time.sleep(300)  # 5 minutes
    st.rerun()

# Legal disclaimer
st.markdown("---")
st.warning("""
**Legal Disclaimer:** This tool only checks if the official appointment system is accessible. 
Users must book appointments themselves on the government website. We do not automate bookings 
or provide legal advice.
""")

# Office information
st.markdown("### 📍 Office Monitoring")
selected_office = st.selectbox(
    "Select office to check:",
    [
        "Barcelona Police (Via Júlia)",
        "Barcelona Extranjería", 
        "Girona Police Station",
        "Tarragona Police Station"
    ]
)

st.write(f"**Best times to check {selected_office}:**")
st.write("- Monday-Friday: 8:00-10:00 AM")
st.write("- Tuesday-Thursday: 2:00-4:00 PM")
st.write("- First weekday of month: Increased availability")
