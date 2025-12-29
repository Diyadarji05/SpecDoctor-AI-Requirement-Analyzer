# app.py
import streamlit as st
from analyzer import detect_ambiguity, detect_missing_constraints, detect_contradictions
from scorer import calculate_score

st.set_page_config(
    page_title="SpecDoctor",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 SpecDoctor")
st.info(
    "SpecDoctor helps teams detect unclear or risky requirements *before* development begins."
)
st.caption("AI-powered Requirement Quality Analyzer")

st.markdown("---")

requirement_text = st.text_area(
    "Paste your Software Requirement / SRS below:",
    height=200,
    placeholder="Example: The system should be fast and user-friendly..."
)

if st.button("🔍 Analyze Requirements"):
    if not requirement_text.strip():
        st.warning("Please enter requirement text.")
    else:
        ambiguity = detect_ambiguity(requirement_text)
        missing = detect_missing_constraints(requirement_text)
        contradictions = detect_contradictions(requirement_text)

        score = calculate_score(ambiguity, missing, contradictions)

        st.markdown("## 📊 Analysis Report")

        st.metric("Requirement Quality Score", f"{score}/100")

        st.markdown("### ⚠️ Ambiguity Detected")
        if ambiguity:
            for word in ambiguity:
                st.write(f"- Ambiguous term: **{word}**")
        else:
            st.success("No ambiguous terms found.")

        st.markdown("### 📉 Missing Constraints")
        if missing:
            st.error("Performance or numeric constraints are missing.")
        else:
            st.success("Constraints look reasonable.")

        st.markdown("### 🔁 Contradictions")
        if contradictions:
            for c in contradictions:
                st.write(f"- {c}")
        else:
            st.success("No contradictions detected.")
