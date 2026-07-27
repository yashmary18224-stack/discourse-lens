import os
import streamlit as st
from google import genai

# Page Configuration
st.set_page_config(
    page_title="DiscourseLens — AI Rhetoric & Discourse Analyzer",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 DiscourseLens")
st.caption("Critical Discourse & Rhetorical Analysis Powered by Gemini AI")

# Retrieve API Key from Secrets or Manual Input
api_key = os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ Please enter a valid Gemini API Key to run the analysis.")
    api_key_input = st.text_input("Enter your Gemini API Key:", type="password")
    if api_key_input:
        api_key = api_key_input

# System Instructions for AI
SYSTEM_PROMPT = """
You are DiscourseLens, an expert AI research assistant specializing in Critical Discourse Analysis (CDA), Linguistics, and Literary Rhetoric.
Your task is to analyze the user's provided text snippet (such as social media posts, news headlines, or speeches).

Structure your response into 4 distinct sections:
1. **Core Themes & Power Dynamics**: Identify underlying ideology, implicit bias, or authority positioning.
2. **Linguistic & Rhetorical Devices**: Highlight specific choices (metaphors, modal verbs, passive voice, exaggeration, framing).
3. **Target Audience & Emotional Triggers**: Explain who this text targets and what emotions (e.g., FOMO, urgency, trust, fear) it evokes.
4. **Academic Summary**: Provide a 2-sentence formal summary suitable for a research literature review.

Maintain an objective, academic, yet approachable tone. Use clear headings and bullet points.
"""

# Sidebar Controls
st.sidebar.header("Analysis Framework")
analysis_focus = st.sidebar.selectbox(
    "Select Focus Area:",
    [
        "General Critical Discourse Analysis",
        "Media & Social Media (FOMO / Trends)",
        "Literary & Rhetorical Analysis",
        "Political Framing & Ideology"
    ]
)

# Text Input Area
user_text = st.text_area(
    "Paste text snippet for analysis:",
    height=200,
    placeholder="e.g., Everyone in college is buying this app before finals week! Don't get left behind..."
)

# Execution
if st.button("🚀 Analyze Discourse", type="primary"):
    if not api_key:
        st.error("Please provide a Gemini API Key to proceed.")
    elif not user_text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing linguistic structures and discourse..."):
            try:
                client = genai.Client(api_key=api_key)
                
                full_prompt = f"{SYSTEM_PROMPT}\n\nSelected Analytical Focus: {analysis_focus}\n\nText for Analysis:\n\"\"\"{user_text}\"\"\""
                
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=full_prompt
                )
                
                st.success("Analysis Complete!")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
