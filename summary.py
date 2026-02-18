import requests
from config import HF_API_KEY, SUMMARY_MODEL

API_URL = f"https://api-inference.huggingface.co/models/{SUMMARY_MODEL}"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def generate_summary(profile1, profile2, meeting_value):
    prompt = f"""
    Person A: {profile1.name}, {profile1.capital_role}, Goal: {profile1.strategic_goal}
    Person B: {profile2.name}, {profile2.capital_role}, Goal: {profile2.strategic_goal}
    Meeting Value Score: {meeting_value:.2f}

    Create a short professional pre-meeting brief explaining:
    - Who they are
    - Why they match
    - Suggested discussion points
    """

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    result = response.json()

    if isinstance(result, list):
        return result[0]["summary_text"]
    else:
        return "Summary unavailable (API limit reached)."
