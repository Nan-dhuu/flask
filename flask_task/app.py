from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    name = "Nandhini"
    course = "B.Tech Information Technology"
    college = "Adhi College of Engineering & Technology"

    skills = [
        "Java",
        "HTML",
        "CSS",
        "SQL"
    ]

    return render_template(
        "index.html",
        name=name,
        course=course,
        college=college,
        skills=skills
    )


if __name__ == "__main__":
    app.run(debug=True)