# Save as: scripts/streamlit_app.py and run with: streamlit run scripts/streamlit_app.py
import streamlit as st
import json

st.title("Market Intelligence Insights Explorer")
category = st.text_input("Type an app category to analyze:")

if category:
    user_prompt = (
        f"Share three new actionable insights with confidence score for apps in the '{category}' category "
        f"using the cleaned dataset."
    )
    insight = get_llm_insight(user_prompt)
    st.write(insight)

with open("insights/insights.json", "r") as f:
    base_insights = json.load(f)
st.markdown("## Precomputed Insights")
for rec in base_insights:
    st.write(f"{rec['insight']}  (Confidence: {rec['confidence']})")