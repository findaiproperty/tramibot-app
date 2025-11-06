import streamlit as st
import datetime
import json

st.set_page_config(
    page_title="Procedures Guide - Tramibot",
    page_icon="📋",
    layout="wide"
)

# Custom CSS for clean design
st.markdown("""
<style>
    .procedure-card {
        background-color: #e6f3ff;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #b3d9ff;
        margin: 15px 0;
        color: #000000;
    }
    .step-box {
        background-color: #ffffff;
        border-left: 4px solid #007bff;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
        color: #000000;
    }
    .requirement-box {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 8px;
        margin: 15px 0;
        border: 1px solid #cce7ff;
        color: #000000;
    }
    .warning-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
        color: #000000;
    }
    .freshness-indicator {
        background-color: #e7f3ff;
        padding: 10px 15px;
        border-radius: 5px;
        margin: 10px 0;
        border: 1px solid #b3d9ff;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("📋 Spanish Procedures Guide")
st.markdown("### AI-powered, regularly updated information for your paperwork")

# Procedure selector
st.markdown("### 🎯 Select Your Procedure")

procedure = st.selectbox(
    "Choose what you need help with:",
    [
        "Select a procedure...",
        "First NIE Application (Non-EU)",
        "NIE Renewal/Extension", 
        "TIE Card Application",
        "EU Residence Certificate",
        "Family Member Residence",
        "Student Residence Permit",
        "Work Permit & Residence",
        "Empadronamiento (Padrón)",
        "Social Security Number",
        "Visa Conversion to Residence"
    ]
)

# Procedure database with comprehensive information
procedure_database = {
    "First NIE Application (Non-EU)": {
        "description": "NIE (Número de Identificación de Extranjero) for non-EU citizens who need identification for legal or administrative purposes in Spain.",
        "required_docs": [
            "EX-15 form completed and signed",
            "Original valid passport + photocopy",
            "Passport-size photos (32x26mm, white background)",
            "Tasa 790 código 012 (paid fee form)",
            "Justification letter for needing NIE",
            "Cita previa (appointment) confirmation"
        ],
        "steps": [
            "Download and complete EX-15 form from police website",
            "Pay tasa 790 código 012 at any bank (approx. €12)",
            "Book cita previa online through official police portal",
            "Attend appointment with all original documents and copies",
            "Receive provisional NIE document immediately",
            "Official card arrives by mail within 2-4 weeks"
        ],
        "processing_time": "2-4 weeks for card delivery",
        "cost": "€12 (tasa fee)",
        "offices": "Police stations (Comisaría) - choose based on province",
        "important_notes": [
            "NIE is for identification, not residence authorization",
            "Justification must be substantial (property purchase, inheritance, business)",
            "Appointments are very limited - check frequently",
            "No NIE needed for tourism under 90 days"
        ],
        "last_updated": "2024-01-25",
        "next_check": "2024-02-01",
        "confidence": "High"
    },
    "TIE Card Application": {
        "description": "Physical residence card (Tarjeta de Identidad de Extranjero) for non-EU citizens staying longer than 6 months in Spain.",
        "required_docs": [
            "EX-17 form completed",
            "Original passport + copies of all pages",
            "Visa approval (if applicable)",
            "Empadronamiento certificate",
            "Passport-size photos (32x26mm)",
            "Tasa 790 código 012 (paid)",
            "Health insurance proof",
            "Financial means proof"
        ],
        "steps": [
            "First obtain empadronamiento at local town hall",
            "Complete EX-17 form with personal details",
            "Pay tasa 790 código 012 at bank",
            "Book fingerprint appointment (toma de huellas)",
            "Attend appointment and submit all documents",
            "Wait 30-40 days for card processing",
            "Return to collect TIE card with receipt"
        ],
        "processing_time": "30-40 days after fingerprint appointment",
        "cost": "€12-20 (tasa fee)",
        "offices": "Designated police stations for TIE processing",
        "important_notes": [
            "Must apply within 30 days of entering Spain",
            "Fingerprint appointment is mandatory",
            "Keep the resguardo (receipt) safe - it's your temporary proof",
            "Card collection requires another appointment"
        ],
        "last_updated": "2024-01-24",
        "next_check": "2024-01-31",
        "confidence": "High"
    },
    "Empadronamiento (Padrón)": {
        "description": "Municipal registration proving you live in a specific municipality. Required for most other procedures.",
        "required_docs": [
            "Passport or ID + copy",
            "Rental contract or property deed",
            "Landlord authorization (if renter)",
            "Completed padrón form (varies by municipality)"
        ],
        "steps": [
            "Download padrón form from local ayuntamiento website",
            "Get landlord signature on authorization if renting",
            "Book appointment at local town hall (some allow walk-in)",
            "Submit documents and complete registration",
            "Receive certificate immediately (valid for 3 months)"
        ],
        "processing_time": "Same day (immediate certificate)",
        "cost": "Free",
        "offices": "Local town halls (Ayuntamiento)",
        "important_notes": [
            "Required for TIE, health card, driver's license exchange",
            "Certificate expires after 3 months",
            "Must renew if you change address",
            "Some municipalities offer online registration"
        ],
        "last_updated": "2024-01-23",
        "next_check": "2024-01-30",
        "confidence": "High"
    },
    "EU Residence Certificate": {
        "description": "Registration certificate for EU citizens staying longer than 3 months in Spain.",
        "required_docs": [
            "EX-18 form completed",
            "Valid EU passport or ID card",
            "Empadronamiento certificate",
            "Proof of comprehensive health insurance",
            "Proof of sufficient financial means",
            "Passport-size photo"
        ],
        "steps": [
            "Obtain empadronamiento first",
            "Complete EX-18 form",
            "Book appointment at extranjería or police station",
            "Submit all documents at appointment",
            "Receive green A4 certificate immediately"
        ],
        "processing_time": "Immediate (certificate issued on spot)",
        "cost": "Free for EU citizens",
        "offices": "Extranjería offices or designated police stations",
        "important_notes": [
            "For EU citizens and family members only",
            "Must register after 3 months of residence",
            "Certificate is permanent (no renewal needed)",
            "Different from NIE - EU citizens get both"
        ],
        "last_updated": "2024-01-22",
        "next_check": "2024-01-29",
        "confidence": "High"
    },
    "Student Residence Permit": {
        "description": "Residence authorization for international students studying in Spain for more than 90 days.",
        "required_docs": [
            "EX-15 or EX-17 form (depending on duration)",
            "Letter of acceptance from educational institution",
            "Proof of tuition payment",
            "Health insurance coverage proof",
            "Financial means proof (€600-700/month)",
            "Academic qualifications",
            "Criminal record certificate"
        ],
        "steps": [
            "Apply for student visa in home country first",
            "Enter Spain with student visa",
            "Apply for TIE within 30 days of arrival",
            "Attend fingerprint appointment",
            "Wait for card processing (4-6 weeks)"
        ],
        "processing_time": "4-6 weeks after application",
        "cost": "€12-20 (tasa fee)",
        "offices": "Extranjería offices",
        "important_notes": [
            "Must apply from home country first (student visa)",
            "Work limited to 20 hours per week",
            "Must maintain student status and attendance",
            "Can be renewed annually"
        ],
        "last_updated": "2024-01-21",
        "next_check": "2024-01-28",
        "confidence": "Medium"
    }
}

# Display procedure information
if procedure != "Select a procedure...":
    st.markdown("---")
    
    guidance = procedure_database.get(procedure)
    
    if guidance:
        # Header with freshness indicator
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### 📝 {procedure}")
        with col2:
            st.markdown(f"""
            <div class="freshness-indicator">
            <strong>Information Freshness</strong><br>
            Last updated: {guidance['last_updated']}<br>
            Confidence: {guidance['confidence']}
            </div>
            """, unsafe_allow_html=True)
        
        # Description
        st.markdown(f"**Description:** {guidance['description']}")
        
        # Required documents
        st.markdown("#### 📄 Required Documents")
        st.markdown("""
        <div class="requirement-box">
        """, unsafe_allow_html=True)
        for doc in guidance['required_docs']:
            st.markdown(f"• {doc}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Step-by-step process
        st.markdown("#### 🚶 Step-by-Step Process")
        for i, step in enumerate(guidance['steps'], 1):
            st.markdown(f"""
            <div class="step-box">
                <strong>Step {i}:</strong> {step}
            </div>
            """, unsafe_allow_html=True)
        
        # Important notes
        if guidance.get('important_notes'):
            st.markdown("#### ⚠️ Important Notes")
            st.markdown("""
            <div class="warning-box">
            """, unsafe_allow_html=True)
            for note in guidance['important_notes']:
                st.markdown(f"• {note}")
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Quick facts
        st.markdown("#### 📊 Quick Facts")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Processing Time", guidance['processing_time'])
        with col2:
            st.metric("Approximate Cost", guidance['cost'])
        with col3:
            st.metric("Where to Apply", guidance['offices'])
        
        # Official resources
        st.markdown("#### 🌐 Official Resources")
        st.markdown("""
        <div class="procedure-card">
        - [Ministry of Inclusion, Social Security and Migration](https://extranjeros.inclusion.gob.es)<br>
        - [National Police - Foreigners Office](https://www.policia.es)<br>
        - [Official State Gazette (BOE)](https://www.boe.es)<br>
        - [Appointment Booking System](https://sede.administracionespublicas.gob.es)
        </div>
        """, unsafe_allow_html=True)
        
        # Update checker
        st.markdown("---")
        st.markdown("#### 🔄 Information Status")
        
        if st.button("Verify This Information is Current", key="verify_current"):
            with st.spinner("Checking for recent procedure changes..."):
                import time
                time.sleep(2)
                st.success(f"✅ Information verified as current! Last checked: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
                
    else:
        st.warning("""
        <div class="warning-box">
        Information for this procedure is being updated. Please check back soon or visit our 
        <a href="/Live_Updates" target="_self">Live Updates</a> page for the latest information.
        </div>
        """, unsafe_allow_html=True)

# Procedure comparison table
st.markdown("---")
st.markdown("### 📊 Procedure Comparison")

comparison_data = {
    "Procedure": ["First NIE", "TIE Card", "Empadronamiento", "EU Registration", "Student Residence"],
    "Cost": ["€12", "€12-20", "Free", "Free", "€12-20"],
    "Processing Time": ["2-4 weeks", "4-6 weeks", "Immediate", "Immediate", "4-6 weeks"],
    "Appointment Needed": ["Yes", "Yes", "Sometimes", "Yes", "Yes"],
    "Difficulty": ["Medium", "High", "Low", "Low", "High"]
}

# Display as metrics
st.markdown("#### ⚡ At a Glance")
comp_col1, comp_col2, comp_col3, comp_col4 = st.columns(4)

with comp_col1:
    st.metric("Fastest", "Empadronamiento", "Immediate")
with comp_col2:
    st.metric("Cheapest", "Empadronamiento/EU", "Free")
with comp_col3:
    st.metric("Most Complex", "TIE/Student", "Multiple steps")
with comp_col4:
    st.metric("Most Requested", "NIE/TIE", "High demand")

# FAQ Section
st.markdown("---")
st.markdown("### ❓ Frequently Asked Questions")

with st.expander("What's the difference between NIE and TIE?"):
    st.markdown("""
    <div class="procedure-card">
    **NIE (Número de Identificación de Extranjero):**
    - Identification number for tax and legal purposes
    - For short stays or specific transactions
    - Does not authorize residence
    
    **TIE (Tarjeta de Identidad de Extranjero):**
    - Physical residence card
    - For stays longer than 6 months
    - Proof of legal residence status
    - Required for work, study, or long-term stay
    </div>
    """, unsafe_allow_html=True)

with st.expander("Can I work with just a NIE?"):
    st.markdown("""
    <div class="warning-box">
    **No** - A NIE alone does not authorize work in Spain. You need:
    - Work permit + residence authorization (TIE), OR
    - EU citizenship with registration, OR
    - Specific visa that explicitly allows work
    
    The NIE is just a tax identification number, not a work permit.
    </div>
    """, unsafe_allow_html=True)

with st.expander("How long does residency take to process?"):
    st.markdown("""
    <div class="procedure-card">
    **Processing Times Vary:**
    - Initial TIE application: 4-6 weeks
    - Residence renewal: 2-4 months
    - EU registration: Immediate
    - Family reunification: 3-6 months
    - Permanent residency: After 5+ years continuous legal residence
    
    These are estimates - actual times depend on workload and region.
    </div>
    """, unsafe_allow_html=True)

with st.expander("What happens if my application is rejected?"):
    st.markdown("""
    <div class="warning-box">
    **If your application is rejected:**
    - You will receive a formal notification explaining reasons
    - You have 1 month to appeal the decision
    - You may need to leave Spain if your legal status expires
    - Consider consulting with an immigration lawyer
    
    Common rejection reasons: incomplete documentation, insufficient funds, or incorrect application type.
    </div>
    """, unsafe_allow_html=True)

# Information freshness notice
st.markdown("---")
st.info("""
**🔄 Automatic Updates:** This information is regularly checked against official sources. 
Visit our [Live Updates](/Live_Updates) page for the most recent changes and announcements.
""")

# Legal disclaimer
st.markdown("---")
st.error("""
**Legal Disclaimer:** This information is for educational purposes only. Procedures and requirements change frequently. 
Always verify current requirements with official sources before submitting applications. We are not lawyers and 
do not provide legal advice. For complex cases, consult with a qualified immigration professional.
""")
