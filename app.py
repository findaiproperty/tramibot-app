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

# Custom CSS with DARK TEXT for readability
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
        color: #155724 !important;  /* DARK GREEN TEXT */
    }
    .status-offline {
        padding: 20px;
        background-color: #f8d7da;
        border: 2px solid #f5c6cb;
        border-radius: 10px;
        text-align: center;
        margin: 20px 0;
        color: #721c24 !important;  /* DARK RED TEXT */
    }
    .instruction-box {
        padding: 25px;
        background-color: #f0f8ff;
        border: 2px solid #b3d9ff;
        border-radius: 10px;
        margin: 20px 0;
        color: #000000 !important;  /* BLACK TEXT */
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
    .dark-text {
        color: #000000 !important;  /* FORCE BLACK TEXT */
    }
    .instruction-box h3, .instruction-box h4, .instruction-box strong {
        color: #000000 !important;  /* BLACK HEADERS */
    }
    .instruction-box a {
        color: #0066cc !important;  /* BLUE LINKS */
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
        f'<h3 style="color: #155724;">✅ SYSTEM ONLINE</h3>'
        f'<p style="color: #155724;">The official appointment system is accessible!</p>'
        f'<p style="color: #155724;"><strong>Best time to check:</strong> Right now!</p>'
        f'<small style="color: #155724;">Last checked: {st.session_state.last_checked}</small>'
        f'</div>',
        unsafe_allow_html=True
    )
    st.balloons()
    
elif st.session_state.system_status == "offline":
    st.markdown(
        f'<div class="status-offline">'
        f'<h3 style="color: #721c24;">❌ SYSTEM OFFLINE</h3>'
        f'<p style="color: #721c24;">The official system may be down for maintenance</p>'
        f'<small style="color: #721c24;">Last checked: {st.session_state.last_checked}</small>'
        f'</div>',
        unsafe_allow_html=True
    )
else:
    st.info("👆 Click the button above to check if the appointment system is online")

# Instructions - CLEAN WITH DARK TEXT
st.markdown("---")
st.markdown("## 📋 How to Book Appointments")

st.markdown("""
<div class="instruction-box dark-text">
<h3 style="color: #d9534f !important; margin-top: 0;">🚨 Important: You must book manually</h3>

<div style="margin: 20px 0; color: #000000 !important;">
<div style="display: flex; align-items: flex-start; margin-bottom: 15px; color: #000000 !important;">
    <div class="step-number">1</div>
    <div style="color: #000000 !important;">
        <strong style="color: #000000 !important;">Go to the official website:</strong><br>
        <a href="https://sede.administracionespublicas.gob.es" target="_blank" style="color: #0066cc !important; font-weight: bold; font-size: 1.1em;">
        https://sede.administracionespublicas.gob.es
        </a>
    </div>
</div>

<div style="display: flex; align-items: flex-start; margin-bottom: 15px; color: #000000 !important;">
    <div class="step-number">2</div>
    <div style="color: #000000 !important;">
        <strong style="color: #000000 !important;">Navigate manually:</strong><br>
        <span style="color: #000000 !important;">• Click "Acceso al sistema de Cita Previa"</span><br>
        <span style="color: #000000 !important;">• Select "Policía - Certificados UE"</span><br>
        <span style="color: #000000 !important;">• Choose your province (Barcelona, Girona, etc.)</span><br>
        <span style="color: #000000 !important;">• Follow the step-by-step process</span>
    </div>
</div>

<div style="display: flex; align-items: flex-start; margin-bottom: 15px; color: #000000 !important;">
    <div class="step-number">3</div>
    <div style="color: #000000 !important;">
        <strong style="color: #000000 !important;">Best times to check:</strong><br>
        <span style="color: #000000 !important;">• 🕗 8:00-10:00 AM (Monday-Friday)</span><br>
        <span style="color: #000000 !important;">• 🕑 2:00-4:00 PM (Tuesday-Thursday)</span><br>
        <span style="color: #000000 !important;">• 📅 First weekday of each month</span>
    </div>
</div>

<div style="display: flex; align-items: flex-start; color: #000000 !important;">
    <div class="step-number">4</div>
    <div style="color: #000000 !important;">
        <strong style="color: #000000 !important;">Have these ready:</strong><br>
        <span style="color: #000000 !important;">• Passport/NIE number</span><br>
        <span style="color: #000000 !important;">• Complete personal details</span><br>
        <span style="color: #000000 !important;">• Email and phone number</span>
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

# Refresh note
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
🔄 This page updates automatically every 5 minutes
</div>
""", unsafe_allow_html=True)
