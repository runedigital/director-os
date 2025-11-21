import streamlit as st
import json
import copy
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="RUNE DIGITAL | Director OS",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. THE "RUNE SKIN" (CSS INJECTION)
# ==========================================
# This maps your Webflow styles directly to Streamlit components
st.markdown("""
    <style>
    /* IMPORT FONTS (Using Rajdhani for that "Industrial/Tech" look similar to your custom font) */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Rajdhani:wght@500;600;700&display=swap');

    /* GLOBAL VARIABLES FROM YOUR CSS */
    :root {
        --runic-slate: #111827;
        --chalk-white: #f0f2f5;
        --chiral-gold: #c8a95c;
        --electric-cyan: #00ffff;
        --dim-slate: #1f2937;
    }

    /* MAIN APP BACKGROUND */
    .stApp {
        background-color: var(--runic-slate);
        color: var(--chalk-white);
        font-family: 'Inter', sans-serif;
    }

    /* HEADERS */
    h1, h2, h3 {
        font-family: 'Rajdhani', sans-serif;
        color: var(--chalk-white) !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    h1 { font-weight: 700; font-size: 3rem !important; }
    h2 { color: var(--chiral-gold) !important; font-size: 1.8rem !important; }

    /* CUSTOM HERO LABEL */
    .hero-label {
        font-family: 'Rajdhani', sans-serif;
        color: var(--electric-cyan);
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 2px;
        margin-bottom: 10px;
        border: 1px solid var(--electric-cyan);
        display: inline-block;
        padding: 4px 12px;
        border-radius: 4px;
        background: rgba(0, 255, 255, 0.05);
    }

    /* BUTTONS (Overriding Streamlit Default) */
    .stButton > button {
        background-color: var(--chiral-gold) !important;
        color: var(--runic-slate) !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        border-radius: 0px !important; /* Making it boxy/industrial */
        border: 1px solid var(--chiral-gold) !important;
        padding: 0.5rem 2rem !important;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: transparent !important;
        color: var(--chiral-gold) !important;
        border: 1px solid var(--chiral-gold) !important;
        box-shadow: 0 0 15px rgba(200, 169, 92, 0.3);
    }

    /* INPUT FIELDS */
    .stTextInput > div > div > input, 
    .stSelectbox > div > div > div, 
    .stTextArea > div > div > textarea {
        background-color: var(--dim-slate) !important;
        color: var(--chalk-white) !important;
        border: 1px solid #374151 !important;
        border-radius: 0px !important;
    }
    
    /* SIDEBAR STYLING */
    [data-testid="stSidebar"] {
        background-color: #0b101b !important;
        border-right: 1px solid #1f2937;
    }

    /* CARD STYLING (Custom HTML blocks) */
    .rune-card {
        background-color: var(--dim-slate);
        padding: 20px;
        border-left: 3px solid var(--chiral-gold);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR: COMMAND CENTER
# ==========================================
with st.sidebar:
    st.markdown("### 💠 SYSTEM STATUS")
    st.markdown("<div style='color:#00ffff; font-family:Rajdhani; font-size:14px;'>● OPERATIONAL</div>", unsafe_allow_html=True)
    st.write("---")
    st.metric(label="REVENUE (WEEKLY)", value="$1,250", delta="+$250")
    st.metric(label="ACTIVE AGENTS", value="4", delta="On Standby")
    
    st.write("---")
    st.markdown("#### 📂 CLIENT FILES")
    st.caption("Select a client to manage their employees.")
    client_select = st.selectbox("Active Clients", ["Real Estate: Adelaide", "E-Comm: GlowCo", "Legal: Smith & Partners"])

# ==========================================
# 4. MAIN HERO SECTION (From your HTML)
# ==========================================
st.markdown('<div class="hero-label">SYSTEM_STATUS: ONLINE</div>', unsafe_allow_html=True)
st.title("BREAK THE CYCLE OF ENTROPY")
st.markdown("""
<p style='font-size: 18px; opacity: 0.8; max-width: 700px;'>
We engineer digital infrastructure built to survive. Select a protocol below to deploy digital labor.
</p>
""", unsafe_allow_html=True)

st.write("---")

# ==========================================
# 5. THE "ARSENAL" (The Agent Forge)
# ==========================================

tab1, tab2, tab3 = st.tabs(["🛠️ FORGE NEW AGENT", "📡 LIVE FEEDS", "💰 INVOICING"])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 1. CONFIGURE DIGITAL EMPLOYEE")
        st.markdown("<div class='rune-card'>Define the parameters of your new asset. This will generate the neural architecture (JSON).</div>", unsafe_allow_html=True)
        
        agent_type = st.selectbox("Select Archetype", 
                                 ["The Research Intern (Lead Gen)", 
                                  "The Junior Copywriter (Content)", 
                                  "The Operations Manager (Support)"])
        
        client_industry = st.text_input("Target Industry", "Commercial Real Estate")
        tone = st.select_slider("Personality Matrix", ["Robotic", "Professional", "Witty", "Aggressive"])
        
        # Logic to change the prompt based on selection
        if "Research" in agent_type:
            default_prompt = f"You are an expert researcher for {client_industry}. Find 10 leads per day."
        elif "Copywriter" in agent_type:
            default_prompt = f"You are a social media manager for {client_industry}. Tone: {tone}."
        else:
            default_prompt = "You are a support agent. Be helpful."
            
        system_prompt = st.text_area("System Prompt (Override)", default_prompt, height=150)

    with col2:
        st.markdown("### 2. DEPLOYMENT")
        st.info("Ready to fabricate. This will generate the n8n Blueprint file.")
        
        if st.button("INITIATE SEQUENCE [BUILD AGENT]"):
            with st.spinner("Compiling Neural Pathways..."):
                time.sleep(2) # Effect
                
                # Mock JSON generation
                agent_data = {
                    "name": f"{client_industry} - {agent_type}",
                    "status": "active",
                    "nodes": [
                        {"name": "Webhook", "type": "trigger"},
                        {"name": "AI_Brain", "prompt": system_prompt},
                        {"name": "Output", "type": "google_sheets"}
                    ]
                }
                json_str = json.dumps(agent_data, indent=2)
                
                st.success("ASSET FABRICATED SUCCESSFULLY.")
                st.code(json_str, language="json")
                st.download_button("DOWNLOAD BLUEPRINT (.json)", json_str, "agent_v1.json")

# ==========================================
# 6. LIVE FEEDS TAB
# ==========================================
with tab2:
    st.markdown("### 📡 LIVE SYSTEM LOGS")
    st.dataframe({
        "Timestamp": ["10:42:01", "10:41:55", "09:30:00"],
        "Agent": ["Research Intern", "Copywriter #2", "Sentinel"],
        "Action": ["Found 12 Leads", "Generated 3 Posts", "Invoice Sent ($500)"],
        "Status": ["SUCCESS", "SUCCESS", "PENDING"]
    }, hide_index=True, use_container_width=True)

# ==========================================
# 7. FOOTER
# ==========================================
st.write("---")
st.markdown("<div style='text-align:center; color:#444;'>RUNE DIGITAL STUDIOS /// SYSTEM VERSION 2.0</div>", unsafe_allow_html=True)
