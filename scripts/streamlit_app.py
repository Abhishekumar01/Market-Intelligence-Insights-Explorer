import streamlit as st
import json
import requests

# Google Gemini API key and endpoint - replace with your actual key
GEMINI_API_KEY = "AIzaSyDjznJl5Tp4AGNjvhY6JhEJ0ZSMMd-mK4o"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

def get_llm_insight(prompt: str) -> str:
    headers = {
        "x-goog-api-key": GEMINI_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gemini-2.5-flash",
        "prompt": {
            "messages": [
                {"role": "system", "content": "You are a market intelligence expert. Respond with clear, data-driven insights only."},
                {"role": "user", "content": prompt}
            ]
        }
    }
    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        generated_text = data.get("candidates", [])[0].get("content", "")
        return generated_text
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        st.error(f"An error occurred: {err}")
    return "Sorry, could not generate insights at this time."

st.title("Market Intelligence Insights Explorer")

category = st.text_input("Type an app category to analyze:")

if category:
    user_prompt = (
        f"Share three new actionable insights with confidence score for apps in the '{category}' category "
        f"using the cleaned dataset."
    )
    with st.spinner("Generating insights..."):
        insight = get_llm_insight(user_prompt)
    st.write(insight)

try:
    with open("insights/insights.json", "r") as f:
        base_insights = json.load(f)
    st.markdown("## Precomputed Insights")
    for rec in base_insights:
        st.write(f"{rec['insight']}  (Confidence: {rec['confidence']})")
except FileNotFoundError:
    st.warning("Precomputed insights file 'insights/insights.json' not found.")
