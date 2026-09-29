import os
import json
import re
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")


def clean_json_block(text: str) -> str:
    text = text.strip()

    # Remove ```json and ``` wrappers
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    return text.strip()


def generate_quiz(python -m venv venvtext: str):
    try:
        prompt = f"""
Create a quiz from the following educational content.

Content:
{text}

Generate exactly 3 multiple-choice questions.

Each question must have exactly 4 options.

Return ONLY valid JSON in this format:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Correct option"
  }}
]

Do not include Markdown.
Do not include explanations outside the JSON.
"""

        response = model.generate_content(prompt)

        cleaned = clean_json_block(response.text)

        quiz = json.loads(cleaned)

        return quiz

    except json.JSONDecodeError as e:
        return {
            "error": f"Quiz JSON parsing error: {e}"
        }

    except Exception as e:
        return {
            "error": f"Error in Quiz Generation: {e}"
        }