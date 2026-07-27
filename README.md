# DiscourseLens — Critical Discourse & Rhetorical Analysis Assistant

> An AI-powered research assistant built for students and scholars to rapidly deconstruct social media content, news headlines, and textual media through Critical Discourse Analysis (CDA).

---

## 🚀 Live App URL
🔗 Deployed Application: https://discourse-lens-ya4j8w3axv7zpvfekhycww.streamlit.app/

---

## 📌 Problem & Purpose
Students and researchers in linguistics, communications, and media studies frequently analyze how power dynamics, emotional triggers (e.g., FOMO), and subtle rhetoric are constructed in everyday text. Manual discourse analysis is time-consuming. 

**DiscourseLens** automates the initial qualitative coding phase, helping users uncover implicit bias, linguistic devices, and target audience framing within seconds.

---

## ✨ Features
- **Instant Discourse Breakdown**: Generates 4 structured analytical sections for any input text.
- **Multiple Framework Focuses**: Toggle between general CDA, media/social media framing, rhetorical analysis, and political framing.
- **Academic Summary Generator**: Synthesizes textual findings into formal research-ready summaries.
- **Secure Key Handling**: Server-side secret management preventing client-side key leakage.

---

## 🤖 AI Feature & System Prompt
**AI Model:** Google Gemini 2.5 Flash (`gemini-2.5-flash`) via the official Google GenAI SDK.

### System Instructions / Prompt:
```text
You are DiscourseLens, an expert AI research assistant specializing in Critical Discourse Analysis (CDA), Linguistics, and Literary Rhetoric.
Your task is to analyze the user's provided text snippet (such as social media posts, news headlines, or speeches).

Structure your response into 4 distinct sections:
1. Core Themes & Power Dynamics: Identify underlying ideology, implicit bias, or authority positioning.
2. Linguistic & Rhetorical Devices: Highlight specific choices (metaphors, modal verbs, passive voice, exaggeration, framing).
3. Target Audience & Emotional Triggers: Explain who this text targets and what emotions (e.g., FOMO, urgency, trust, fear) it evokes.
4. Academic Summary: Provide a 2-sentence formal summary suitable for a research literature review.

Maintain an objective, academic, yet approachable tone. Use clear headings and bullet points.
