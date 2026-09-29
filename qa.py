import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")


def answer_question(question: str) -> str:
    try:
        prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.

Question:
{question}

Instructions:
- Use simple language.
- Give a concise answer.
- Explain important points.
- Use examples when useful.
"""

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        return f"Error in Q&A: {e}"