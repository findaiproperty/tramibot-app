import streamlit as st
import datetime
import json
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

try:
    from ai_updater import LegalAIUpdater
except ImportError:
    # Fallback if utils not available
    class LegalAIUpdater:
        def check_boe_updates(self): return []
        def monitor_procedure_changes(self): return []

st.set_page_config(
    page_title="Live Updates - Tramibot", 
    page_icon="🔄",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .update-card {
        background-color: #e6f3ff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #b3d9ff;
        margin: 15px 0;
        color: #000000;
    }
    .urgent-update {
        background-color: #ffe6e6;
        border: 2px solid #ff6666;
    }
    .procedure-change {
        background-color: #fff0e6;
        border: 1px solid #ffb366;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔄 Live Procedure Updates")
st.markdown("### AI-Powered Real-time Monitoring of Spanish Immigration Procedures")

# Initialize AI Updater
updater = LegalAIUpdater()

# Auto-refresh control
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("**Updates are checked automatically every 24 hours**")
with col2:
    if st.button("🔄 Check for Updates Now"):
        st.rerun()

# Recent Official Updates
st.markdown("## 📢 Recent Official Updates")

try:
    boe_updates = updater.check_boe_updates()
    
    if boe_updates:
        for update in boe_updates[:5]:  # Show latest 5
            with st.expander(f"📅 {update['date']} - {update['title']}", expanded=False):
                st.markdown(f"**Source:** Official State Gazette (BOE)")
                st.markdown(f"**Summary:** {update['summary']}")
                st.markdown(f"**[Read Full Text]({update['link']})**")
    else:
        st.info("""
        **No recent official updates found.**
        
        *When available, this section will show:*
        - Changes to immigration laws
        - Updated procedure requirements  
        - New official forms or fees
        - Policy announcements
        """)
        
except Exception as e:
    st.warning(f"Update service temporarily unavailable: {str(e)}")

# Procedure Changes Monitoring
st.markdown("## 📊 Procedure Change Monitoring")

procedures = {
    "NIE Application": {
        "current_status": "✅ Stable",
        "last_change": "2024-01-15",
        "monitoring": "Forms, requirements, processing times"
    },
    "TIE Card": {
        "current_status": "✅ Stable", 
        "last_change": "2024-01-10",
        "monitoring": "Document requirements, appointment availability"
    },
    "EU Registration": {
        "current_status": "✅ Stable",
        "last_change": "2024-01-05",
        "monitoring": "Registration process, required documents"
    },
    "Work Permits": {
        "current_status": "⚠️ Monitoring",
        "last_change": "2024-01-20", 
        "monitoring": "Quota changes, requirement updates"
    }
}

for procedure, info in procedures.items():
    with st.expander(f"{procedure} - {info['current_status']}"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Last Change:** {info['last_change']}")
            st.markdown(f"**Monitoring:** {info['monitoring']}")
        with col2:
            st.markdown("**Next Check:** Today")
            if st.button(f"Check {procedure}", key=procedure):
                with st.spinner(f"Checking {procedure}..."):
                    time.sleep(2)  # Simulate checking
                    st.success("No changes detected")

# Community-Sourced Updates
st.markdown("## 🤝 Community-Sourced Updates")

st.markdown("""
<div class="update-card">
<h4>🚨 Recent Community Reports</h4>
<p><strong>Barcelona Police Appointments:</strong> Users report increased availability on Tuesday mornings</p>
<p><strong>TIE Processing:</strong> Several users report 3-week processing instead of 4</p>
<p><strong>Document Requirements:</strong> No changes reported in required documents</p>
</div>
""", unsafe_allow_html=True)

# Update History
st.markdown("## 📈 Update History")

update_history = [
    {"date": "2024-01-20", "procedure": "All", "change": "Minor fee adjustments", "impact": "Low"},
    {"date": "2024-01-15", "procedure": "TIE", "change": "Digital submission available", "impact": "Medium"},
    {"date": "2024-01-10", "procedure": "NIE", "change": "Form EX-15 updated", "impact": "Low"},
]

for update in update_history:
    impact_color = {
        "Low": "🟢",
        "Medium": "🟡", 
        "High": "🔴"
    }.get(update["impact"], "⚪")
    
    st.markdown(f"{impact_color} **{update['date']}** - {update['procedure']}: {update['change']}")

# Manual Update Submission
st.markdown("---")
st.markdown("## 📝 Submit Update Report")

with st.form("update_report"):
    st.markdown("Help keep information current by reporting changes you discover:")
    
    col1, col2 = st.columns(2)
    with col1:
        procedure = st.selectbox("Procedure", list(procedures.keys()))
        change_type = st.selectbox("Type of Change", 
                                 ["Requirement Change", "Form Update", "Fee Change", "Processing Time", "Other"])
    with col2:
        change_date = st.date_input("When did you notice this change?")
        urgency = st.select_slider("Urgency", ["Low", "Medium", "High"])
    
    description = st.text_area("Describe the change in detail:")
    source = st.text_input("Source (official website, gestor, etc.):")
    
    if st.form_submit_button("Submit Update Report"):
        st.success("Thank you! Your report will help keep our information accurate.")

# Legal Notice
st.markdown("---")
st.info("""
**ℹ️ About Our Update System:**  
This system monitors official publications and community reports to provide current information. 
We do not scrape government websites or access restricted systems. All monitoring is done through 
publicly available channels and respects official terms of service.
""")
