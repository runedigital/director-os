import streamlit as st
import json
import copy

# ==========================================
# CONFIGURATION
# ==========================================
st.set_page_config(page_title="Director OS | Agent Forge", layout="wide", page_icon="🏗️")

# Custom CSS for the "Hacker" aesthetic
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #C5C6C7; }
    .stButton>button { width: 100%; background-color: #00ADB5; color: white; border: none; }
    .stButton>button:hover { background-color: #00FFF5; color: black; }
    </style>
""", unsafe_allow_html=True)

st.title("🏗️ Director OS: Agent Forge")
st.caption("Sophisticated Asset Fabrication System")

# ==========================================
# 1. LOAD THE MASTER TEMPLATE
# ==========================================
# In a real app, you'd load this from a file. Here is a Mock "Master JSON" structure.
# This represents a simple workflow: Webhook -> AI Agent -> Google Sheets
mock_template = {
    "nodes": [
        {
            "name": "Webhook",
            "type": "n8n-nodes-base.webhook",
            "parameters": {"path": "REPLACE_ME_PATH"}
        },
        {
            "name": "AI Agent",
            "type": "@n8n/n8n-nodes-langchain.agent",
            "parameters": {
                "prompt": {
                    "messages": [
                        {
                            "role": "system",
                            "content": "REPLACE_ME_SYSTEM_PROMPT"
                        }
                    ]
                }
            }
        }
    ],
    "connections": {} # Connections would go here
}

# ==========================================
# 2. THE CONFIGURATOR (The "No-Code" Interface)
# ==========================================
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Client Parameters")
    
    client_name = st.text_input("Client Name", "Acme Corp")
    agent_role = st.selectbox("Agent Archetype", ["Lead Qualifier", "Support Sentinel", "Market Researcher"])
    
    st.subheader("2. Intelligence Configuration")
    industry = st.text_input("Target Industry", "Commercial Real Estate")
    tone = st.select_slider("Agent Persona Tone", options=["Formal", "Helpful", "Aggressive", "Witty"])
    
    # Dynamic Prompt Building
    base_instruction = f"You are a highly skilled {agent_role} working for {client_name} in the {industry} sector."
    
    if agent_role == "Lead Qualifier":
        specific_instruction = "Your goal is to read the incoming lead, research them on LinkedIn, and decide if they are 'High Value' or 'Low Value'."
    elif agent_role == "Support Sentinel":
        specific_instruction = "Your goal is to de-escalate angry customers and draft a refund confirmation if needed."
    else:
        specific_instruction = "Your goal is to summarize complex topics into 3 bullet points."

    final_system_prompt = st.text_area("Generated System Prompt (Editable)", 
                                       f"{base_instruction} Your tone is {tone}. {specific_instruction}", height=150)

with col2:
    st.subheader("3. Blueprint Preview")
    st.info("This JSON is your 'Product'. You sell this file.")
    
    # LOGIC: INJECT VARIABLES INTO JSON
    if st.button("⚙️ Fabricate Agent JSON"):
        # Create a deep copy to avoid modifying the template
        new_agent = copy.deepcopy(mock_template)
        
        # Find and Replace Logic (This is the "Auto Builder" magic)
        # In reality, you would loop through nodes to find specific IDs or Names
        
        # 1. Inject Webhook Path
        safe_client_name = client_name.lower().replace(" ", "-")
        new_agent["nodes"][0]["parameters"]["path"] = f"{safe_client_name}-{agent_role.lower().replace(' ', '-')}"
        
        # 2. Inject System Prompt
        # Note: Accessing deep nested JSON keys requires knowing the exact path in your template
        new_agent["nodes"][1]["parameters"]["prompt"]["messages"][0]["content"] = final_system_prompt
        
        # Output
        json_str = json.dumps(new_agent, indent=2)
        st.code(json_str, language='json')
        
        # Download Button
        st.download_button(
            label="💾 Download Asset (.json)",
            data=json_str,
            file_name=f"{safe_client_name}_{agent_role}_v1.json",
            mime="application/json"
        )
        st.success(f"Asset Created! Webhook Endpoint: /webhook/{safe_client_name}-{agent_role.lower().replace(' ', '-')}")

# ==========================================
# 4. STRATEGY GUIDANCE
# ==========================================
with st.expander("📖 How to Monetize This (The 12-Week Plan)", expanded=True):
    st.markdown("""
    **The Strategy:**
    1. **Don't sell the builder.** Use this builder yourself to speed up your delivery time by 10x.
    2. **Sell the Outcome.** Go to a Real Estate agent and say: *"I can install a bot that pre-screens your leads instantly."*
    3. **Delivery:** - They pay you $1,500.
       - You open this app.
       - Type "Real Estate", "Friendly".
       - Download JSON.
       - Import into your n8n instance.
       - **Profit.**
    """)
