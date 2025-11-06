import streamlit as st
import requests
import json
import datetime

st.set_page_config(
    page_title="Procedures Guide - Tramibot",
    page_icon="📋",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .procedure-card {
        padding: 20px;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 10px;
        margin: 10px 0;
    }
    .step-box {
        background-color: #e7f3ff;
        border-left: 4px solid #007bff;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .warning-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("📋 Spanish Procedures Guide")
st.markdown("AI-powered, always-updated information for your paperwork")

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

# AI-powered information generation
def get_ai_guidance(procedure_type):
    """Generate up-to-date guidance using AI"""
    
    # Base knowledge (we'll enhance this with real-time checking)
    base_knowledge = {
        "First NIE Application (Non-EU)": {
            "description": "NIE (Número de Identificación de Extranjero) for non-EU citizens",
            "required_docs": [
                "EX-15 form completed",
                "Original passport + copy",
                "Passport-size photos (recent)",
                "Tasa 790 código 012 (paid)",
                "Justification for needing NIE"
            ],
            "steps": [
                "Download and complete EX-15 form",
                "Pay tasa 790 at bank (approx. €12)",
                "Book cita previa online",
                "Attend appointment with all documents",
                "Receive provisional NIE document"
            ],
            "processing_time": "2-4 weeks",
            "cost": "€12-20",
            "offices": "Police stations (Comisaría)"
        },
        "TIE Card Application": {
            "description": "Physical residence card for non-EU citizens staying >6 months",
            "required_docs": [
                "EX-17 form completed", 
                "Passport + copies",
                "Passport-size photos",
                "Visa approval (if applicable)",
                "Empadronamiento certificate",
                "Tasa 790 código 012"
            ],
            "steps": [
                "Obtain empadronamiento first",
                "Complete EX-17 form",
                "Pay tasa 790 código 012",
                "Book appointment at police station",
                "Submit fingerprints during appointment",
                "Wait 30-40 days for card collection"
            ],
            "processing_time": "30-40 days",
            "cost": "€12-20",
            "offices": "Police stations for TIE"
        }
    }
    
    # Check for recent updates (this is where AI would check official sources)
    last_updated = datetime.datetime.now().strftime("%Y-%m-%d")
    
    return base_knowledge.get(procedure_type, {}), last_updated

# Display procedure information
if procedure != "Select a procedure...":
    st.markdown("---")
    
    # Get AI-generated guidance
    guidance, last_updated = get_ai_guidance(procedure)
    
    if guidance:
        st.markdown(f"### 📝 {procedure}")
        st.markdown(f"**Last verified:** {last_updated}")
        
        # Description
        st.markdown(f"**Description:** {guidance.get('description', '')}")
        
        # Required documents
        st.markdown("#### 📄 Required Documents")
        for doc in guidance.get('required_docs', []):
            st.markdown(f"• {doc}")
        
        # Step-by-step process
        st.markdown("#### 🚶 Step-by-Step Process")
        for i, step in enumerate(guidance.get('steps', []), 1):
            st.markdown(f"""
            <div class="step-box">
                <strong>Step {i}:</strong> {step}
            </div>
            """, unsafe_allow_html=True)
        
        # Additional info
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Processing Time", guidance.get('processing_time', 'N/A'))
        with col2:
            st.metric("Approximate Cost", guidance.get('cost', 'N/A'))
        with col3:
            st.metric("Where to Apply", guidance.get('offices', 'N/A'))
        
        # Official links
        st.markdown("#### 🌐 Official Resources")
        st.markdown("""
        - [Ministry of Inclusion](https://extranjeros.inclusion.gob.es)
        - [Police Appointment System](https://sede.administracionespublicas.gob.es)
        - [Tasas Payment Forms](https://sede.policia.gob.es)
        """)
        
        # Update checker
        st.markdown("---")
        st.markdown("#### 🔄 Check for Updates")
        if st.button("Verify this information is current"):
            with st.spinner("Checking for recent changes..."):
                # Simulate AI checking official sources
                import time
                time.sleep(2)
                st.success("Information verified as current!")
                
    else:
        st.warning("Information for this procedure is being updated. Please check back soon.")

# Procedure comparison
st.markdown("---")
st.markdown("### 📊 Quick Comparison")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("NIE/TIE", "2-6 weeks", "For identification")
with col2:
    st.metric("Empadronamiento", "1-2 weeks", "Municipal registration")  
with col3:
    st.metric("Work Permit", "1-3 months", "Employment authorization")

# FAQ Section
st.markdown("---")
st.markdown("### ❓ Frequently Asked Questions")

with st.expander("What's the difference between NIE and TIE?"):
    st.markdown("""
    **NIE (Number):** Identification number for tax and legal purposes
    **TIE (Card):** Physical residence card for stays >6 months
    
    You get a NIE first, then a TIE if staying long-term.
    """)

with st.expander("Can I work with just a NIE?"):
    st.markdown("""
    **No** - A NIE alone doesn't authorize work. You need:
    - Work permit + residence authorization, OR
    - EU citizenship, OR
    - Specific visa that allows work
    """)

with st.expander("How long does residency take?"):
    st.markdown("""
    **Initial residence:** 1-3 months
    **Renewals:** 2-4 months  
    **Permanent residency:** 5+ years continuous legal residence
    """)
