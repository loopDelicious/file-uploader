"""File Uploader."""

from flask import Flask, request, render_template
from model import connect_to_db, db, File

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route('/upload', methods=["POST"])
def add_file():
    """User uploads a new file, and inserts into db."""

    fileURL = request.form.get("fileURL")
    file_id = request.form.get("file_id")

    new_file = File(file_id=file_id,
                    fileurl=fileURL)

    db.session.add(new_file)
    db.session.commit()

    return "Success"


if __name__ == "__main__":
    app.debug = True
    connect_to_db