from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("database/studyhub.db")
    connection.row_factory = sqlite3.Row
    return connection


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

        return render_template(
            "timer.html",
            subject=subject,
            topic=topic,
            content=content,
            minutes=minutes
        )

    return render_template("study.html")


@app.route("/record")
def record():
    subject = request.args.get("subject")
    topic = request.args.get("topic")
    content = request.args.get("content")
    elapsed = request.args.get("elapsed")

    return render_template(
        "record.html",
        subject=subject,
        topic=topic,
        content=content,
        elapsed=elapsed
    )


@app.route("/save-record", methods=["POST"])
def save_record():
    subject = request.form.get("subject")
    topic = request.form.get("topic")
    content = request.form.get("content")
    elapsed = request.form.get("elapsed")

    material = request.form.get("material")
    start_position = request.form.get("start_position")
    end_position = request.form.get("end_position")
    understanding = request.form.get("understanding")
    next_plan = request.form.get("next_plan")

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO study_records (
            subject,
            topic,
            content,
            duration_seconds,
            material,
            start_position,
            end_position,
            understanding_level,
            next_plan
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            subject,
            topic,
            content,
            elapsed,
            material,
            start_position,
            end_position,
            understanding,
            next_plan
        )
    )

    connection.commit()
    connection.close()

    return "学習記録を保存しました！"

@app.route("/history")
def history():
    connection = get_db_connection()

    records = connection.execute(
        """
        SELECT *
        FROM study_records
        ORDER BY created_at DESC
        """
    ).fetchall()

    connection.close()

    return render_template(
        "history.html",
        records=records
    )


if __name__ == "__main__":
    app.run(debug=True)