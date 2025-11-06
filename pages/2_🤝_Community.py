import streamlit as st
import datetime

st.set_page_config(
    page_title="Community Reports - Tramibot",
    page_icon="🤝",
    layout="wide"
)

# Dark text CSS
st.markdown("""
<style>
    .community-guidelines {
        background-color: #e7f3ff;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: #000000 !important;
    }
    .community-guidelines h4, .community-guidelines p {
        color: #000000 !important;
    }
    .form-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #dee2e6;
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🤝 Community Success Reports")
st.markdown("### Learn from real user experiences")

# Community guidelines
st.markdown("""
<div class="community-guidelines">
<h4>🎯 How This Works</h4>
<p>Share when and how you successfully found appointments. This helps everyone learn patterns and best strategies.</p>
<p><strong>Remember:</strong> We never automate booking - we share knowledge to help manual checking!</p>
</div>
""", unsafe_allow_html=True)

# Success report form
st.markdown("## 📝 Share Your Success")

with st.form("success_report"):
    st.markdown("""
    <div class="form-container">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        office = st.selectbox(
            "Which office?",
            ["Barcelona Police (Via Júlia)", "Barcelona Extranjería", "Girona", "Tarragona", "Lleida", "Other"]
        )
        procedure = st.selectbox(
            "What procedure?",
            ["NIE Application", "TIE Card", "Residence Renewal", "Empadronamiento", "Other"]
        )
    
    with col2:
        success_time = st.time_input("Approximate time you found appointment")
        success_date = st.date_input("Date you found appointment")
        wait_time = st.number_input("Days you had been looking", min_value=0, max_value=365)
    
    strategy = st.text_area("What strategy worked? (e.g., 'Checked at 8:15 AM on Tuesday')")
    tips = st.text_area("Any tips for others?")
    
    if st.form_submit_button("Share Success Story"):
        st.success("""
        Thank you for contributing to the community! 
        Your insights will help others navigate the process more successfully.
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Sample community reports
st.markdown("---")
st.markdown("## 📊 Community Insights")

st.info("""
**Community data will appear here as users share their experiences.** 
Early contributors will help establish patterns that benefit everyone!
""")

# Placeholder for future community content
st.markdown("### 🏆 Be a Community Pioneer!")
st.markdown("""
<div style="color: #000000;">
The first users to share their success stories will:
- Help establish reliable patterns
- Build valuable community knowledge  
- Make the platform more useful for everyone
- Receive recognition as early contributors
</div>
""", unsafe_allow_html=True)
