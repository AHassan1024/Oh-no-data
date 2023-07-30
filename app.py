from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Check if dataset file was uploaded
        if "input_data" in request.files:
            dataset_file = request.files["input_data"]
            # Process the uploaded dataset here (Save it to a temporary directory/convert to .csv for processing.)

            return render_template("uploaded.html")
    # If the request method is GET, or file upload was unsuccessful, render the uploading HTML again.
    return render_template("upload.html")
