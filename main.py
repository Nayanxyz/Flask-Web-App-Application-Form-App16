from datetime import datetime
from flask import Flask, render_template, request, flash


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date,"%Y-%m-%d")
        occupation = request.form["occupation"]


    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)