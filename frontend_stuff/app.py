from flask import Flask, render_template

DEVELOPMENT_ENV = True

app = Flask(__name__)

app_data = {
    "name": "eduscribe.ai",
    "description": "Educational Video",
    "author": "Peter Simeth",
    "html_title": "eduscribe.ai",
    "project_name": "eduscribe.ai",
    "keywords": "flask, webapp, template, basic",
}


@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)


@app.route("/demo")
def demo():
    return render_template("demo.html", app_data=app_data)




if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV)