import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")


def summarize_text(text: str) -> str:
    try:
        prompt = f"""
Summarize the following text in simple language.

Keep the important information.
Remove unnecessary repetition.
Make the summary easy for a student to understand.

Text:
{text}
"""

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        return f"Error in Summary: {e}"