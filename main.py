import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

from modules.qa import answer_question
from modules.explain import explain_topic
from modules.quiz import generate_quiz
from modules.summarize import summarize_text
from modules.learning_path import get_learning_recommendations


load_dotenv()

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(
    directory="templates"
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/qa")
async def qa(request: Request):
    data = await request.json()
    question = data.get("text", "").strip()

    if not question:
        return {"error": "Please enter a question."}

    return {"result": answer_question(question)}


@app.post("/explain")
async def explain(request: Request):
    data = await request.json()
    topic = data.get("text", "").strip()

    if not topic:
        return {"error": "Please enter a topic."}

    return {"result": explain_topic(topic)}


@app.post("/quiz")
async def quiz(request: Request):
    data = await request.json()
    text = data.get("text", "").strip()

    if not text:
        return {"error": "Please enter some content for the quiz."}

    return {"result": generate_quiz(text)}


@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "").strip()

    if not text:
        return {"error": "Please enter text to summarize."}

    return {"result": summarize_text(text)}


@app.post("/learn/recommendations")
async def learning_recommendations(request: Request):
    data = await request.json()
    topic = data.get("text", "").strip()

    if not topic:
        return {"error": "Please enter a learning topic."}

    return {
        "result": get_learning_recommendations(topic)
    }