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

            # Validating file:
            if dataset_file and valid_file_format(dataset_file.filename):
                # Save the file to a temp dir
                dataset_file.save(
                    "/Users/main/Git_Projects/2023/Oh-no-data/temp/temp_csv.csv"
                )
                # File has been saved. Now go in and extract column names as a list. Forward it to the uploaded.html.

                # TODO: Introduce support for .xlsx and .xls files by converting to csv.
                #
                return render_template("uploaded.html")
                # TODO: Update uploaded.html to get user input on what to extract.

                # Or maybe render a new page with all the visualisations automatically.s

            return "Invalid file format. Try uploading again, as one of: .csv, .xlsx, .xls."

            # Process the uploaded dataset here (Save it to a temporary directory/convert to .csv for processing.)

    # If the request method is GET, or file upload was unsuccessful, render the uploading HTML again.
    return render_template("upload.html")


def valid_file_format(filename):
    return filename.lower().endswith((".csv", ".xlsx", "/xls"))
