import streamlit as st
import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Tramibot - Spanish Procedures Assistant",
    page_icon="🚀",
    layout="wide"
)

# Clean CSS with white background and light blue boxes
st.markdown("""
<style>
    /* Main background - clean white */
    .main {
        background-color: #ffffff;
    }
    
    /* Main header */
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Light blue feature cards */
    .feature-card {
        padding: 25px;
        background-color: #e6f3ff;
        border: 1px solid #b3d9ff;
        border-radius: 10px;
        margin: 15px 0;
        height: 100%;
        color: #000000;
    }
    
    /* Light blue instruction boxes */
    .instruction-box {
        background-color: #e6f3ff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #b3d9ff;
        color: #000000;
        margin: 15px 0;
    }
    
    /* Light blue success stories */
    .success-story {
        background-color: #e6f3ff;
        border: 1px solid #b3d9ff;
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        color: #000000;
    }
    
    /* Step numbers */
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
    
    /* Donation box */
    .donation-box {
        background-color: #e6f3ff;
        padding: 25px;
        border-radius: 10px;
        margin: 20px 0;
        border: 1px solid #b3d9ff;
        color: #000000;
    }
    
    /* Legal info box */
    .legal-box {
        background-color: #fff3cd;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        border: 1px solid #ffeaa7;
        color: #000000;
    }
    
    /* Force black text everywhere */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown ul, .stMarkdown ol {
        color: #000000 !important;
    }
    
    /* Ensure all text is black */
    div[data-testid="stMarkdownContainer"] {
        color: #000000 !important;
    }
    
    /* Links */
    a {
        color: #0066cc !important;
        font-weight: bold;
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
        <h3>📚 Manual Status Guide</h3>
        <p><strong>Know exactly when and how to check</strong></p>
        <ul>
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
        <h3>🤝 Community Reporting</h3>
        <p><strong>Learn from others' success</strong></p>
        <ul>
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
        <h3>🎓 Educational Platform</h3>
        <p><strong>Master the process</strong></p>
        <ul>
            <li>Complete procedure guides</li>
            <li>Document preparation help</li>
            <li>Legal requirement overviews</li>
            <li>Professional referrals</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Manual Status Guide Section
st.markdown("---")
st.markdown("## 📚 Manual Status Guide")

st.markdown("""
### 🎯 Best Times to Check Manually
Based on historical patterns and community reports:
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **🕗 Morning Windows:**
    - Monday-Friday: 8:00-10:00 AM
    - Tuesday-Thursday: Most reliable
    - First weekday of month: Highest availability
    
    **📍 Barcelona Offices:**
    - Police (Via Júlia): 8:15-9:00 AM
    - Extranjería: 9:00-10:00 AM
    """)

with col2:
    st.markdown("""
    **🕑 Afternoon Windows:**
    - Tuesday-Thursday: 2:00-4:00 PM  
    - Some offices release cancellations
    - Less competitive than mornings
    
    **🏛️ Other Cities:**
    - Girona: 8:45 AM consistently
    - Tarragona: 9:00 AM & 4:00 PM
    - Lleida: 8:30 AM daily
    """)

# Quick Action Section
st.markdown("### ⚡ Ready to Check?")
st.markdown("""
<div class="instruction-box">
<h4>🚨 Manual Checking Process</h4>

<div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
    <div class="step-number">1</div>
    <div>
        <strong>Click the official link below</strong><br>
        You'll be redirected to the government portal
    </div>
</div>

<div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
    <div class="step-number">2</div>
    <div>
        <strong>Navigate manually through the system</strong><br>
        Select your procedure and province
    </div>
</div>

<div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
    <div class="step-number">3</div>
    <div>
        <strong>Check for available time slots</strong><br>
        Be prepared to book immediately if you find one
    </div>
</div>

<div style="display: flex; align-items: flex-start;">
    <div class="step-number">4</div>
    <div>
        <strong>Report your success to help others!</strong><br>
        Share what worked in our community section
    </div>
</div>
</div>
""", unsafe_allow_html=True)

# Official Links
st.markdown("### 🌐 Official Government Portals")
official_col1, official_col2, official_col3 = st.columns(3)

with official_col1:
    st.link_button("🎯 National Appointment System", 
                  "https://sede.administracionespublicas.gob.es")

with official_col2:
    st.link_button("📝 Ministry of Immigration", 
                  "https://extranjeros.inclusion.gob.es")

with official_col3:
    st.link_button("📄 Official Forms & Fees", 
                  "https://sede.policia.gob.es")

# Community Reports Section
st.markdown("---")
st.markdown("## 🤝 Community Reports")

st.markdown("""
### 📊 Recent Success Stories
*Community-driven insights - be the first to contribute!*
""")

# Placeholder for community content
st.info("""
**🚧 Community Building in Progress**  
As more users join and share their experiences, this section will show real success stories and patterns.
""")

# Sample success stories
st.markdown("#### 💡 Sample Success Patterns")

success_col1, success_col2 = st.columns(2)

with success_col1:
    st.markdown("""
    <div class="success-story">
    <strong>Barcelona Police (Via Júlia)</strong><br>
    ⏰ Most success: Tuesday 8:30 AM<br>
    📅 Best results: First week of month<br>
    🎯 Strategy: Check right at 8:15 AM
    </div>
    """, unsafe_allow_html=True)

with success_col2:
    st.markdown("""
    <div class="success-story">
    <strong>Girona Office</strong><br>
    ⏰ Most success: Weekdays 8:45 AM<br>
    📅 Consistent morning releases<br>
    🎯 Strategy: Daily checking at opening
    </div>
    """, unsafe_allow_html=True)

# Educational Resources Section
st.markdown("---")
st.markdown("## 🎓 Educational Resources")

st.markdown("""
### Master the Paperwork Process
Visit our Procedures Guide for complete step-by-step instructions for:
""")

edu_col1, edu_col2, edu_col3 = st.columns(3)

with edu_col1:
    st.markdown("""
    <div class="feature-card">
    <h4>📄 NIE Applications</h4>
    <ul>
        <li>First-time NIE (EX-15)</li>
        <li>NIE renewal process</li>
        <li>Required documents</li>
        <li>Fee payment guide</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with edu_col2:
    st.markdown("""
    <div class="feature-card">
    <h4>🏠 Residence Procedures</h4>
    <ul>
        <li>TIE card application</li>
        <li>EU registration</li>
        <li>Family reunification</li>
        <li>Student residence</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with edu_col3:
    st.markdown("""
    <div class="feature-card">
    <h4>📍 Local Registration</h4>
    <ul>
        <li>Empadronamiento</li>
        <li>Social security number</li>
        <li>Health card registration</li>
        <li>Driver's license exchange</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Donation Section
st.markdown("---")
st.markdown("""
<div class="donation-box">
<h3 style="text-align: center;">☕ Support This Project</h3>
<p style="text-align: center;">If Tramibot has helped you navigate Spanish bureaucracy, consider supporting its development.</p>

<div style="text-align: center; margin: 25px 0;">
    <a href="https://ko-fi.com/tramibot" target="_blank" style="background-color: #29abe0; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; display: inline-block; font-weight: bold; margin: 5px;">
        ☕ Support on Ko-fi
    </a>
    <a href="https://buymeacoffee.com/tramibot" target="_blank" style="background-color: #ff813f; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; display: inline-block; font-weight: bold; margin: 5px;">
        🍪 Buy Me a Coffee
    </a>
</div>

<div style="background-color: #ffffff; padding: 15px; border-radius: 8px; margin: 15px 0; border: 1px solid #b3d9ff;">
<h4 style="margin-top: 0;">What Your Support Enables:</h4>
<ul style="margin-bottom: 0;">
    <li>Server and hosting costs</li>
    <li>Continuous platform improvements</li>
    <li>Research into procedure updates</li>
    <li>Community feature development</li>
</ul>
</div>
</div>
""", unsafe_allow_html=True)

# Legal Information
st.markdown("""
<div class="legal-box">
<h4>📋 Important Legal Information</h4>
<p><strong>Donation Nature:</strong></p>
<ul>
    <li>Contributions are <strong>voluntary support</strong>, not payments for services</li>
    <li>All core features remain <strong>completely free forever</strong></li>
    <li>No premium features or paywalls will ever be added</li>
</ul>

<p><strong>Tax Compliance:</strong></p>
<ul>
    <li>We comply with Spanish tax regulations (Ley 35/2006)</li>
    <li>Donations under €3,000/year are considered personal support</li>
    <li>All income over legal thresholds will be properly declared</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Final Legal Disclaimer
st.markdown("---")
st.error("""
**Legal Disclaimer:** Tramibot is an educational and informational platform. We do not automate any government processes, 
access appointment systems programmatically, or provide legal advice. All appointment booking must be done manually 
by users through official government portals. We connect users with licensed professionals for legal matters.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
<p>🚀 Tramibot - Making Spanish bureaucracy more accessible | 100% Legal Educational Platform</p>
</div>
""", unsafe_allow_html=True)
