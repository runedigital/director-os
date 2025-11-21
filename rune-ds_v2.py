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

    /* THE "ENTROPY
