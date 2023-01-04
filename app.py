import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            frequency_penalty=0.0,
            max_tokens=100,
            model="text-davinci-003",
            prompt=generate_prompt(question),
            temperature=0,
            top_p=1,
        )
        return redirect(url_for("index", query=question, result=response.choices[0].text))

    query = request.args.get("query")
    result = request.args.get("result")

    return render_template("index.html", query=query, result=result)

def generate_prompt(question):
    return question
