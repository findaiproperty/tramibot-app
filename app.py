import streamlit as st
import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Tramibot - Spanish Procedures Assistant",
    page_icon="🚀",
    layout="wide"
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
    .feature-card {
        padding: 25px;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 10px;
        margin: 15px 0;
        height: 100%;
        color: #000000 !important;
    }
    .feature-card h3, .feature-card p, .feature-card li {
        color: #000000 !important;
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
    .success-story {
        background-color: #e7f3ff;
        border-left: 4px solid #007bff;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
        color: #000000 !important;
    }
    .office-card {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        color: #000000 !important;
    }
    .dark-text {
        color: #000000 !important;
    }
    .instruction-box {
        background-color: #e7f3ff;
        padding: 20px;
        border-radius: 10px;
        color: #000000 !important;
        border: 1px solid #b3d9ff;
    }
    .instruction-box h4 {
        color: #000000 !important;
    }
    .donation-box {
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 10px;
        margin: 20px 0;
        color: #000000;
        border: 1px solid #dee2e6;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🚀 Tramibot</div>', unsafe_allow_html=True)
st.markdown("### Your Legal Assistant for Spanish Bureaucracy")
st.markdown("*100% legal educational platform - No automated system access*")

# Navigation
st.sidebar.title("🧭 Navigation")
st.sidebar.page_link("app.py", label="🏠 Home Dashboard")
st.sidebar.page_link("pages/1_📋_Procedures_Guide.py", label="📋 Procedures Guide") 
st.sidebar.page_link("pages/2_🤝_Community.py", label="🤝 Community Reports")

# Three Pillars Dashboard
st.markdown("---")
st.markdown("## 🎯 Your Three-Part Solution")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #000000;">📚 Option 1: Manual Status Guide</h3>
        <p style="color: #000000;"><strong>Know exactly when and how to check</strong></p>
        <ul style="color: #000000;">
            <li>Best times for each office</li>
            <li>Step-by-step checking process</li>
            <li>Document preparation guides</li>
            <li>Office-specific strategies</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #000000;">🤝 Option 2: Community Reporting</h3>
        <p style="color: #000000;"><strong>Learn from others' success</strong></p>
        <ul style="color: #000000;">
            <li>Real user success stories</li>
            <li>Recent appointment findings</li>
            <li>Pattern identification</li>
            <li>Crowdsourced best times</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #000000;">🎓 Option 3: Educational Platform</h3>
        <p style="color: #000000;"><strong>Master the process</strong></p>
        <ul style="color: #000000;">
            <li>Complete procedure guides</li>
            <li>Document preparation help</li>
            <li>Legal requirement overviews</li>
            <li>Professional referrals</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ... (keep all your existing content here - manual guide, community, education sections)
# [Your existing app content remains unchanged]
# ...

# DONATION SECTION (Add this before the final legal disclaimer)
st.markdown("---")
st.markdown("""
<div class="donation-box">
<h3 style="color: #000000; text-align: center;">☕ Support This Project</h3>
<p style="color: #000000; text-align: center;">If Tramibot has helped you navigate Spanish bureaucracy, consider supporting its development and maintenance.</p>

<div style="text-align: center; margin: 25px 0;">
    <a href="https://ko-fi.com/tramibot" target="_blank" style="background-color: #29abe0; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; display: inline-block; font-weight: bold; margin: 5px;">
        ☕ Support on Ko-fi
    </a>
    <a href="https://buymeacoffee.com/tramibot" target="_blank" style="background-color: #ff813f; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; display: inline-block; font-weight: bold; margin: 5px;">
        🍪 Buy Me a Coffee
    </a>
</div>

<div style="background-color: #e7f3ff; padding: 15px; border-radius: 8px; margin: 15px 0; border: 1px solid #b3d9ff;">
<h4 style="color: #000000; margin-top: 0;">What Your Support Enables:</h4>
<ul style="color: #000000; margin-bottom: 0;">
    <li>Server and hosting costs</li>
    <li>Continuous platform improvements</li>
    <li>Research into procedure updates</li>
    <li>Community feature development</li>
</ul>
</div>

</div>
""", unsafe_allow_html=True)

# Legal disclaimers for donations
st.markdown("""
<div style="background-color: #fff3cd; padding: 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #ffeaa7;">
<h4 style="color: #000000; margin-top: 0;">📋 Important Legal Information</h4>
<div style="color: #000000; font-size: 0.9em;">
<p><strong>Donation Nature:</strong></p>
<ul>
    <li>Contributions are <strong>voluntary support</strong>, not payments for services</li>
    <li>All core features of Tramibot remain <strong>completely free forever</strong></li>
    <li>No premium features or paywalls will ever be added to current services</li>
</ul>

<p><strong>Tax Compliance:</strong></p>
<ul>
    <li>We comply with Spanish tax regulations (Ley 35/2006)</li>
    <li>Donations under €3,000/year are considered personal support</li>
    <li>All income over legal thresholds will be properly declared</li>
</ul>

<p><strong>Service Guarantee:</strong></p>
<ul>
    <li>Donations do not entitle donors to special services or guarantees</li>
    <li>Support is appreciated but never expected or required</li>
</ul>
</div>
</div>
""", unsafe_allow_html=True)

# Original Legal Disclaimer (keep this)
st.markdown("---")
st.error("""
**Legal Disclaimer:** Tramibot is an educational and informational platform. We do not automate any government processes, 
access appointment systems programmatically, or provide legal advice. All appointment booking must be done manually 
by users through official government portals. We connect users with licensed professionals for legal matters.
""")
