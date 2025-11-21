import streamlit as st
import time

# ==========================================
# 1. SYSTEM CONFIG
# ==========================================
st.set_page_config(
    page_title="RUNE DIGITAL | DIRECTOR OS",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. THE VISUAL ENGINE (CSS INJECTION)
# ==========================================
st.markdown("""
    <style>
    /* --- IMPORTING 'TEKO' FOR THAT TALL INDUSTRIAL HEADER LOOK --- */
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600&family=Teko:wght@300;400;600&display=swap');

    :root {
        --void-black: #05070a;       /* Darker than slate, matches screenshot */
        --runic-slate: #111827;
        --chiral-gold: #c8a95c;
        --neon-cyan: #00ffff;
        --dim-text: #9ca3af;
    }

    /* --- RESET & BACKGROUND --- */
    .stApp {
        background-color: var(--void-black);
        font-family: 'Rajdhani', sans-serif; /* Body text */
        color: #f0f2f5;
    }

    /* REMOVE STREAMLIT PADDING */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 5rem !important;
        max-width: 95% !important;
    }

    /* --- TYPOGRAPHY (MATCHING SCREENSHOT) --- */
    .hero-tag {
        color: var(--neon-cyan);
        font-family: 'Rajdhani', sans-serif;
        font-size: 12px;
        letter-spacing: 2px;
        border: 1px solid rgba(0, 255, 255, 0.3);
        padding: 4px 12px;
        display: inline-block;
        margin-bottom: 15px;
        background: rgba(0, 255, 255, 0.02);
    }

    h1.mega-title {
        font-family: 'Teko', sans-serif; /* The tall font */
        font-size: 85px; /* Massive size */
        line-height: 0.9;
        font-weight: 400;
        text-transform: uppercase;
        margin: 0;
        padding: 0;
        letter-spacing: 1px;
        color: white;
    }

    /* THE "ENTROPY" OUTLINE EFFECT */
    .hollow-text {
        color: transparent;
        -webkit-text-stroke: 1px var(--chiral-gold); /* The Gold Outline */
        font-weight: 300;
    }

    .sub-text {
        color: var(--dim-text);
        font-size: 18px;
        max-width: 600px;
        margin-top: 20px;
        margin-bottom: 40px;
        line-height: 1.5;
    }

    /* --- CUSTOM BUTTONS (SQUARE BRACKETS) --- */
    div.stButton > button {
        background-color: transparent !important;
        color: var(--chiral-gold) !important;
        border: 1px solid var(--chiral-gold) !important;
        border-radius: 0px !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        letter-spacing: 2px;
        padding: 12px 30px !important;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        background-color: var(--chiral-gold) !important;
        color: black !important;
        box-shadow: 0 0 20px rgba(200, 169, 92, 0.2);
    }

    /* --- CARD STYLING (THE 3 COLUMNS) --- */
    .rune-card {
        background-color: rgba(17, 24, 39, 0.4);
        border: 1px solid #333;
        padding: 0px;
        margin-top: 20px;
        transition: transform 0.2s;
    }
    .rune-card:hover {
        border-color: var(--chiral-gold);
    }
    .card-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        opacity: 0.7;
        filter: grayscale(100%);
    }
    .card-content {
        padding: 20px;
    }
    .card-title {
        font-family: 'Teko', sans-serif;
        font-size: 28px;
        color: white;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    .card-desc {
        font-size: 14px;
        color: #888;
    }

    /* --- SIDEBAR & INPUTS --- */
    section[data-testid="stSidebar"] {
        background-color: #020305;
        border-right: 1px solid #222;
    }
    div[data-baseweb="input"] {
        background-color: #0f1219 !important;
        border: 1px solid #333 !important;
        color: white !important;
        border-radius: 0px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. THE HEADER (RAW HTML REPLICATION)
# ==========================================

# This creates the exact Hero section from your screenshot
st.markdown("""
    <div style="padding-top: 40px;">
        <div class="hero-tag">SYSTEM_STATUS: ONLINE</div>
        <h1 class="mega-title">BREAK THE CYCLE</h1>
        <h1 class="mega-title">OF <span class="hollow-text">ENTROPY</span></h1>
        <p class="sub-text">
            Most websites decay the moment they launch. We engineer digital infrastructure built to survive the count.
        </p>
    </div>
""", unsafe_allow_html=True)

# The "[ SUMMON THE SMITH ]" Button
col_cta, col_null = st.columns([1, 3])
with col_cta:
    st.button("[ SUMMON THE SMITH ]", use_container_width=True)

st.write("---")

# ==========================================
# 4. THE ARSENAL (GRID LAYOUT)
# ==========================================
st.markdown("<h2 style='font-family:Teko; font-size:36px; color:#c8a95c; margin-bottom:20px;'>THE ARSENAL</h2>", unsafe_allow_html=True)

# We mimic the 3-card layout from your screenshot
c1, c2, c3 = st.columns(3)

# Helper function to create the card look
def render_card(col, title, img_url, desc):
    with col:
        st.markdown(f"""
        <div class="rune-card">
            <img src="{img_url}" class="card-img">
            <div class="card-content">
                <div class="card-title">{title}</div>
                <div class="card-desc">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"[ DEPLOY {title.split()[0]} ]", key=title)

# Using placeholders or generic tech images to match your vibe
render_card(c1, "AUTOMATION CORE", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=500&q=80", "n8n Neural Pathways.")
render_card(c2, "WEBFLIGHT SYSTEMS", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&q=80", "React & Streamlit Interfaces.")
render_card(c3, "STRATEGIC OPS", "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500&q=80", "Revenue Architecture.")

# ==========================================
# 5. THE WORKSPACE (AGENT FORGE)
# ==========================================
st.write("")
st.write("")
st.markdown("<h2 style='font-family:Teko; font-size:36px; color:#c8a95c;'>DIGITAL EMPLOYEE FABRICATION</h2>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🛠️ CONFIGURE AGENT", "📡 LIVE FEED"])

with tab1:
    c_left, c_right = st.columns([2, 1])
    with c_left:
        client = st.text_input("CLIENT_ID")
        agent_role = st.selectbox("ROLE", ["Lead Qualifier", "Support Sentinel", "Outreach Bot"])
        st.text_area("PRIME DIRECTIVE", height=100, placeholder="Enter system prompt...")
        st.button("[ INITIATE BUILD SEQUENCE ]", key="build")
    with c_right:
        st.info("Ready to fabricate. This will output the JSON blueprint for n8n.")

with tab2:
    st.dataframe({"Time": ["10:00", "10:05"], "Event": ["System Check", "Agent Deployed"]}, use_container_width=True)

# ==========================================
# 6. SIDEBAR (COMMAND CENTER)
# ==========================================
with st.sidebar:
    st.markdown("<h3 style='font-family:Teko; font-size:30px; color:white;'>RUNE COMMAND</h3>", unsafe_allow_html=True)
    st.caption("Director Clearance: Lvl 5")
    st.write("---")
    st.metric("WEEKLY REVENUE", "$1,250", "+20%")
    st.metric("ACTIVE AGENTS", "4", "Online")
    st.write("---")
    st.selectbox("ACTIVE CLIENT", ["North Star Realty", "GlowCo Ecomm"])
