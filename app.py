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

# Custom CSS for clean styling
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
    .instruction-box {
        padding: 25px;
        background-color: #f0f8ff;
        border: 2px solid #b3d9ff;
        border-radius: 10px;
        margin: 20px 0;
    }
    .step-number {
        background-color: #007bff;
        color: white;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-right: 10px;
        font-weight: bold;
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
        response = requests.get(
            'https://sede.administracionespublicas.gob.es',
            timeout=10
        )
        return response.status_code == 200
    except:
        return False

# Main dashboard
st.markdown("### 🔍 Check System Status")

col1, col2 = st.columns([2, 1])
with col1:
    if st.button("**Check if System is Online**", use_container_width=True, type="primary"):
        with st.spinner("Checking official system..."):
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

# Instructions - CLEAN AND READABLE
st.markdown("---")
st.markdown("## 📋 How to Book Appointments")

st.markdown("""
<div class="instruction-box">
<h3 style="color: #d9534f; margin-top: 0;">🚨 Important: You must book manually</h3>

<div style="margin: 20px 0;">
<div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
    <div class="step-number">1</div>
    <div>
        <strong>Go to the official website:</strong><br>
        <a href="https://sede.administracionespublicas.gob.es" target="_blank" style="font-size: 1.1em;">
        https://sede.administracionespublicas.gob.es
        </a>
    </div>
</div>

<div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
    <div class="step-number">2</div>
    <div>
        <strong>Navigate manually:</strong><br>
        • Click "Acceso al sistema de Cita Previa"<br>
        • Select "Policía - Certificados UE"<br>
        • Choose your province (Barcelona, Girona, etc.)<br>
        • Follow the step-by-step process
    </div>
</div>

<div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
    <div class="step-number">3</div>
    <div>
        <strong>Best times to check:</strong><br>
        • 🕗 8:00-10:00 AM (Monday-Friday)<br>
        • 🕑 2:00-4:00 PM (Tuesday-Thursday)<br>
        • 📅 First weekday of each month
    </div>
</div>

<div style="display: flex; align-items: flex-start;">
    <div class="step-number">4</div>
    <div>
        <strong>Have these ready:</strong><br>
        • Passport/NIE number<br>
        • Complete personal details<br>
        • Email and phone number
    </div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# Office tips
st.markdown("---")
st.markdown("## 📍 Office-Specific Tips")

office = st.selectbox(
    "Select your office:",
    ["Barcelona Police (Via Júlia)", "Barcelona Extranjería", "Girona", "Tarragona", "Lleida"]
)

if office == "Barcelona Police (Via Júlia)":
    st.success("**Best times:** 8:15-9:00 AM on weekdays")
elif office == "Barcelona Extranjería":
    st.success("**Best times:** Tuesday/Thursday mornings")
elif office == "Girona":
    st.success("**Best times:** 8:45 AM daily")
elif office == "Tarragona":
    st.success("**Best times:** 9:00 AM and 4:00 PM")
else:
    st.success("**Best times:** Weekday mornings 8:00-10:00 AM")

# Quick actions
st.markdown("---")
st.markdown("## ⚡ Quick Actions")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 Check Status Again"):
        st.rerun()
        
with col2:
    st.link_button("🌐 Open Official Website", "https://sede.administracionespublicas.gob.es")

# Legal disclaimer
st.markdown("---")
st.error("""
**Legal Disclaimer:** This tool only checks if the official appointment system homepage is accessible. 
Users must manually navigate and book appointments themselves. We do not automate bookings, 
bypass security measures, or provide legal advice.
""")
