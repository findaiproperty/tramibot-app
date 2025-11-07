import streamlit as st
import datetime
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

try:
    from ai_core import immigration_ai
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False

st.set_page_config(
    page_title="AI Procedures Guide - Tramibot",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .ai-card {
        background-color: #e6f7ff;
        padding: 25px;
        border-radius: 10px;
        border: 2px solid #91d5ff;
        margin: 15px 0;
        color: #000000;
    }
    .ai-thinking {
        background-color: #f6ffed;
        border: 2px solid #b7eb8f;
        padding: 20px;
        border-radius: 8px;
        margin: 15px 0;
    }
    .update-alert {
        background-color: #fff2e8;
        border: 2px solid #ffbb96;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .step-box {
        background-color: #ffffff;
        border-left: 4px solid #1890ff;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 AI Spanish Procedures Guide")
st.markdown("### Generative AI-powered, real-time updated immigration guidance")

# AI Status
if AI_AVAILABLE:
    st.success("✅ Advanced AI System: ONLINE - Generating current guidance")
else:
    st.warning("⚠️ AI System: OFFLINE - Using cached information")

# User context collection
st.markdown("### 🎯 Tell Us About Your Situation")
col1, col2 = st.columns(2)

with col1:
    user_nationality = st.selectbox(
        "Your Nationality",
        ["EU Citizen", "Non-EU Citizen", "UK Citizen", "Other"]
    )
    
    current_location = st.selectbox(
        "Your Current Location", 
        ["Outside Spain", "In Spain (Tourist)", "In Spain (Legal Residence)", "In Spain (Other)"]
    )

with col2:
    time_in_spain = st.selectbox(
        "Planned Stay Duration",
        ["Less than 90 days", "3-6 months", "1-2 years", "Long-term/Permanent"]
    )
    
    purpose = st.selectbox(
        "Purpose of Stay",
        ["Work", "Study", "Family Reunification", "Retirement", "Entrepreneur", "Other"]
    )

user_context = f"""
Nationality: {user_nationality}
Current Location: {current_location} 
Planned Duration: {time_in_spain}
Purpose: {purpose}
"""

# Procedure selection
st.markdown("### 📋 Select Procedure for AI Analysis")

procedure = st.selectbox(
    "Choose procedure for AI guidance:",
    [
        "Select a procedure...",
        "First NIE Application",
        "TIE Card Application", 
        "EU Residence Registration",
        "Family Reunification",
        "Student Residence Permit",
        "Work Authorization",
        "Long-Term EU Residence",
        "Nationality Application",
        "Visa Extension/Change",
        "Empadronamiento Process"
    ]
)

# AI Guidance Generation
if procedure != "Select a procedure...":
    st.markdown("---")
    
    # Generate AI guidance
    if st.button("🤖 Generate AI-Powered Guidance", type="primary"):
        with st.spinner("🔄 AI is analyzing current procedures and recent updates..."):
            
            if AI_AVAILABLE:
                try:
                    # Call the real AI system
                    ai_guidance = immigration_ai.generate_procedure_guide(procedure, user_context)
                    
                    # Display AI-generated content
                    st.markdown(f"""
                    <div class="ai-card">
                    <h3>🤖 AI-Generated Guide: {procedure}</h3>
                    <p><strong>Generated:</strong> {ai_guidance['generated_at']}</p>
                    <p><strong>Sources Checked:</strong> {', '.join(ai_guidance['sources_checked'])}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display the AI guidance
                    st.markdown("### 📝 AI Guidance")
                    st.markdown(ai_guidance['ai_guidance'])
                    
                    # Show recent updates considered
                    if ai_guidance['recent_updates_considered']:
                        st.markdown("### 🔄 Recent Updates Considered")
                        for update in ai_guidance['recent_updates_considered']:
                            with st.expander(f"📅 {update['date']} - {update['title']}"):
                                st.markdown(f"**Source:** {update['source']}")
                                st.markdown(f"**AI Impact Analysis:** {update['ai_analysis']}")
                                st.markdown(f"**[Read Full Update]({update['link']})**")
                    
                except Exception as e:
                    st.error(f"AI service error: {str(e)}")
                    st.info("Please try again or check the official sources directly.")
            else:
                st.warning("""
                **AI System Offline**
                Our AI service is currently unavailable. 
                
                Please visit:
                - [Ministry of Inclusion](https://extranjeros.inclusion.gob.es)
                - [Official BOE](https://www.boe.es)
                - [Police Procedures](https://www.policia.es)
                """)
    
    # Quick info while AI loads
    st.markdown("### 💡 What AI Will Analyze:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="ai-thinking">
        **📊 Current Requirements**
        - Latest document lists
        - Updated fee structures  
        - Eligibility criteria
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="ai-thinking">
        **🔄 Recent Changes**
        - Legal updates
        - Procedure modifications
        - Form changes
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="ai-thinking">
        **🎯 Personalized Advice**
        - Your specific situation
        - Common pitfalls to avoid
        - Timeline expectations
        </div>
        """, unsafe_allow_html=True)

# Real-time Update Monitoring
st.markdown("---")
st.markdown("## 🔄 Live AI Monitoring")

if st.button("Scan for Recent Procedure Changes"):
    with st.spinner("AI is scanning official sources for updates..."):
        if AI_AVAILABLE:
            try:
                updates = immigration_ai.scan_official_updates()
                
                if updates:
                    st.success(f"Found {len(updates)} recent updates")
                    
                    for update in updates[:5]:  # Show latest 5
                        with st.expander(f"🚨 {update['date']} - {update['title']}", expanded=True):
                            st.markdown(f"**Source:** {update['source']}")
                            st.markdown(f"**AI Impact Analysis:** {update['ai_analysis']}")
                            st.markdown(f"**[Read Official Text]({update['link']})**")
                else:
                    st.info("No recent immigration-related updates found in official sources.")
                    
            except Exception as e:
                st.error(f"Update scan failed: {str(e)}")
        else:
            st.warning("AI monitoring unavailable")

# AI System Information
st.markdown("---")
st.markdown("## 🤖 About Our AI System")

st.markdown("""
<div class="ai-card">
<h4>Advanced Generative AI Features</h4>

**🔄 Real-time Monitoring:**
- Scans Official State Gazette (BOE) daily
- Monitors ministry announcements  
- Tracks legal changes automatically

**🧠 Intelligent Analysis:**
- Understands procedure complexities
- Analyzes impact of legal changes
- Provides personalized guidance

**🎯 Current Information:**
- Always uses latest official sources
- Considers recent legal updates
- Adapts to changing requirements

**Free AI Technologies Used:**
- Hugging Face Inference API
- OpenRouter Free Models
- Local Ollama Integration
</div>
""", unsafe_allow_html=True)

# Legal Disclaimer
st.markdown("---")
st.error("""
**AI System Disclaimer:** This AI provides guidance based on current official sources but cannot guarantee accuracy. 
Always verify critical information with official government sources. The AI may occasionally generate incorrect information - 
use as a helpful guide, not legal advice.
""")
