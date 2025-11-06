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

# Custom CSS
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
    .instructions {
        padding: 20px;
        background-color: #e7f3ff;
        border: 2px solid #b3d9ff;
        border-radius: 10px;
        margin: 20px 0;
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
    """Check if the appointment system homepage is accessible"""
    try:
        # Only check the main domain, not deep links
        response = requests.get(
            'https://sede.administracionespublicas.gob.es',
            timeout=10
        )
        return response.status_code == 200
    except:
        return False

# Main dashboard
st.markdown("### 🔍 System Status Check")

if st.button("Check if Appointment System is Online", use_container_width=True, type="primary"):
    with st.spinner("Checking official system accessibility..."):
        is_online = check_appointment_system()
        st.session_state.system_status = "online" if is_online else "offline"
        st.session_state.last_checked = datetime.datetime.now().strftime("%H:%M:%S")

# Display status
if st.session_state.system_status == "online":
    st.markdown(
        f'<div class="status-online">'
        f'<h3>✅ SYSTEM ONLINE</h3>'
        f'<p>The official appointment system is accessible!</p>'
        f'<p><strong>Best time to check:</strong> Right now!</p>'
        f'<small>Last checked: {st.session_state.last_checked}</small>'
        f'</div>',
        unsafe_allow_html=True
    )
    st.balloons()
    
elif st.session_state.system_status == "offline":
    st.markdown(
        f'<div class="status-offline">'
        f'<h3>❌ SYSTEM OFFLINE</h3>'
        f'<p>The official system may be down for maintenance</p>'
        f'<small>Last checked: {st.session_state.last_checked}</small>'
        f'</div>',
        unsafe_allow_html=True
    )
else:
    st.info("👆 Click the button above to check if the appointment system is online")

# Instructions
st.markdown("---")
st.markdown("### 📋 How to Book Appointments")

st.markdown("""
<div class="instructions">
<h4>🚨 Important: You must book manually</h4>

1. **Go to the official website:**
   🔗 <a href="https://sede.administracionespublicas.gob.es" target="_blank">https://sede.administracionespublicas.gob.es</a>

2. **Navigate manually:**
   - Click "Acceso al sistema de Cita Previa"
   - Select "Policía - Certificados UE" 
   - Choose your province (Barcelona, Girona, etc.)
   - Follow the step-by-step process

3. **Best times to check:**
   - 🕗 8:00-10:00 AM (Monday-Friday)
   - 🕑 2:00-4:00 PM (Tuesday-Thursday) 
   - 📅 First weekday of each month

4. **Have these ready:**
   - Passport/NIE number
   - Complete personal details
   - Email and phone number
</div>
""", unsafe_allow_html=True)

# Office tips
st.markdown("### 📍 Office-Specific Tips")

office = st.selectbox(
    "Select your office for best times:",
    ["Barcelona Police", "Barcelona Extranjería", "Girona", "Tarragona", "Lleida"]
)

if office == "Barcelona Police":
    st.write("**Via Júlia Office:** Slots often released 8:15-9:00 AM")
elif office == "Barcelona Extranjería":
    st.write("**Extranjería:** Check Tuesday/Thursday mornings")
else:
    st.write("**General tip:** Check weekday mornings 8:00-10:00 AM")

# Legal disclaimer
st.markdown("---")
st.warning("""
**Legal Disclaimer:** This tool only checks if the official appointment system homepage is accessible. 
Users must manually navigate and book appointments themselves. We do not automate bookings, 
bypass security measures, or provide legal advice.
""")

# Auto-refresh option
if st.session_state.system_status != "unknown":
    if st.button("Check Again"):
        st.rerun()
