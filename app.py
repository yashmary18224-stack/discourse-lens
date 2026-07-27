import streamlit as st
import re
from collections import Counter

# Page Configuration
st.set_page_config(
    page_title="DiscourseLens — Text & Rhetoric Analyzer",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 DiscourseLens")
st.caption("Automated Critical Discourse & Rhetorical Analysis Tool")

# Sidebar Controls
st.sidebar.header("Analysis Settings")
analysis_type = st.sidebar.selectbox(
    "Select Analysis Focus:",
    [
        "General Critical Discourse Analysis",
        "Media & Social Media (FOMO & Urgency)",
        "Political Framing & Rhetoric"
    ]
)

# Text Input
user_text = st.text_area(
    "Paste text snippet for analysis:",
    height=200,
    placeholder="e.g., Everyone in college is buying this app before finals week! Don't get left behind..."
)

def analyze_discourse(text):
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    
    # Emotional & Rhetorical Markers
    fomo_words = ["everyone", "don't", "miss", "behind", "urgent", "now", "exclusive", "limited", "secret", "must"]
    fomo_matches = [w for w in words if w in fomo_words]
    
    modal_verbs = ["must", "should", "could", "would", "might", "can", "will"]
    modal_matches = [w for w in words if w in modal_verbs]
    
    # Stopwords filter for key theme extraction
    stopwords = set(["the", "a", "an", "is", "are", "and", "or", "to", "in", "of", "for", "on", "with", "this", "that", "it", "at", "by", "from", "be", "has", "have", "not"])
    filtered_words = [w for w in words if w not in stopwords and len(w) > 2]
    word_counts = Counter(filtered_words).most_common(5)
    
    return {
        "total_words": total_words,
        "fomo_count": len(fomo_matches),
        "fomo_list": list(set(fomo_matches)),
        "modal_count": len(modal_matches),
        "modal_list": list(set(modal_matches)),
        "top_keywords": word_counts
    }

if st.button("🚀 Analyze Discourse", type="primary"):
    if not user_text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        results = analyze_discourse(user_text)
        
        st.success("Analysis Complete!")
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("1. Core Themes & Keyword Density")
            if results["top_keywords"]:
                for word, count in results["top_keywords"]:
                    st.write(f"- **{word.capitalize()}**: repeated {count} time(s)")
            else:
                st.write("No distinct recurring keywords detected.")

            st.subheader("2. Linguistic & Rhetorical Devices")
            st.write(f"- **Modal Verbs (Authority/Power Positioning)**: {results['modal_count']} found")
            if results["modal_list"]:
                st.caption(f"Detected: {', '.join(results['modal_list'])}")
                
        with col2:
            st.subheader("3. Emotional Triggers & Urgency (FOMO)")
            st.write(f"- **Urgency/FOMO Markers**: {results['fomo_count']} found")
            if results["fomo_list"]:
                st.caption(f"Detected words: {', '.join(results['fomo_list'])}")
            else:
                st.caption("Low urgency or persuasion-heavy language detected.")

            st.subheader("4. Academic Summary")
            st.info(
                f"The analyzed text comprises **{results['total_words']} words** evaluated under the **{analysis_type}** framework. "
                f"Primary discourse features include {results['fomo_count']} urgency markers and {results['modal_count']} modal constructs shaping persuasive stance."
            )
