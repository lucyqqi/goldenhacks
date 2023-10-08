from flask import Flask, render_template, request
from backend import translate_audio_to_language

DEVELOPMENT_ENV = True

app = Flask(__name__)

text_content = ""

app_data = {
    "name": "eduscribe.ai",
    "description": "Educational Video",
    "author": "Peter Simeth",
    "html_title": "eduscribe.ai",
    "project_name": "eduscribe.ai",
    "keywords": "flask, webapp, template, basic",
    "summaryText": text_content,
}


@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)


@app.route("/demo")
def demo():
    return render_template("demo.html", app_data=app_data)


@app.route("/summary")
def summary():
    text_content = translate_audio_to_language()
    print(text_content)
    return render_template("summary.html", app_data={
    "name": "eduscribe.ai",
    "description": "Educational Video",
    "author": "Peter Simeth",
    "html_title": "eduscribe.ai",
    "project_name": "eduscribe.ai",
    "keywords": "flask, webapp, template, basic",
    "summaryText": text_content,
})

if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV)