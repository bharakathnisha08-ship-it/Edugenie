from transformers import pipeline


# Load lightweight local model
explainer = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)


def explain_topic(topic: str) -> str:
    try:
        prompt = f"""
Explain the following educational topic in very simple language.

Topic:
{topic}

Requirements:
- Explain as if teaching a beginner.
- Use simple words.
- Give an example.
- Keep the explanation clear and concise.
"""

        result = explainer(
            prompt,
            max_length=300,
            do_sample=False
        )

        return result[0]["generated_text"]

    except Exception as e:
        return f"Error in Explanation: {e}"