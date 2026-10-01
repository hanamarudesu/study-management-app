from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/study", methods=["GET", "POST"])
def study():

    if request.method == "POST":
        subject = request.form.get("subject")
        topic = request.form.get("topic")
        content = request.form.get("content")
        minutes = request.form.get("minutes")

        print("学習科目:", subject)
        print("学習分野:", topic)
        print("学習内容:", content)
        print("目標時間:", minutes)

    return render_template("study.html")


if __name__ == "__main__":
    app.run(debug=True)