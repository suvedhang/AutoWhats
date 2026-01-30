import os
import json
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are an intent extraction agent for WhatsApp automation.

Return ONLY valid JSON.
No explanations.
No markdown.

Allowed intents:
- SEND_MESSAGE
- COUNT_UNREAD

JSON format:
{
  "intent": "...",
  "entities": {
    "contact": "... or null",
    "message": "... or null"
  }
}
"""

def gemini_agent(user_input: str) -> dict:
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        SYSTEM_PROMPT + "\nUser command: " + user_input
    )

    try:
        return json.loads(response.text)
    except Exception:
        return {
            "intent": "UNKNOWN",
            "entities": {
                "contact": None,
                "message": None
            }
        }
