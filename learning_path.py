import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")


def get_learning_recommendations(topic: str) -> str:
    try:
        prompt = f"""
Create a personalized learning path for the following topic:

Topic:
{topic}

Create a structured learning roadmap.

Include:

1. Beginner level
2. Intermediate level
3. Advanced level
4. Topics to study at each level
5. Suggested timeline
6. Practice activities
7. Useful learning resources
8. Projects or exercises
9. Final skills the learner should achieve

Make the roadmap suitable for a student.

Use clear headings and bullet points.
"""

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        return f"Error in Learning Recommendations: {e}"