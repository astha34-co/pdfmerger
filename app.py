from io import BytesIO

from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfMerger

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50 MB total request size


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/merge", methods=["POST"])
def merge_pdfs():
    files = [
        file
        for file in request.files.getlist("pdfs")
        if file and file.filename and file.filename.lower().endswith(".pdf")
    ]

    if len(files) < 2:
        return render_template(
            "index.html", error="Choose at least two PDF files to merge."
        ), 400

    merger = PdfMerger()
    output = BytesIO()
    try:
        for pdf in files:
            merger.append(pdf.stream)
        merger.write(output)
        output.seek(0)
    except Exception:
        app.logger.exception("PDF merge failed")
        return render_template(
            "index.html",
            error="One or more files could not be read as PDFs. Check the files and try again.",
        ), 400
    finally:
        merger.close()

    return send_file(
        output,
        as_attachment=True,
        download_name="merged.pdf",
        mimetype="application/pdf",
    )


@app.errorhandler(413)
def request_too_large(_error):
    return render_template(
        "index.html", error="The selected files exceed the 50 MB upload limit."
    ), 413


if __name__ == "__main__":
    app.run(debug=True)
