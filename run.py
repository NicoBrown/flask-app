import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank You")
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    data = []
    with open("data/jobs.json", "r") as json_data:
        data = json.load(json_data)
        return render_template("careers.html" , page_title="Careers" , roles=data)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "8080")),
        debug=True)