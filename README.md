# PDF Merge App

A small web app for combining multiple PDF files into one PDF. It uses **Flask** for the web server and **PyPDF2** to merge the files. The page has a vintage editorial style and works on desktop and mobile screens.

**GitHub repository:** https://github.com/astha34-co/pdfmerger

**Live app:** https://pdfmerger-oqrm.onrender.com

## What the app does

- Lets a user select or drop multiple PDF files.
- Shows the selected files and lets the user change their order or remove a file.
- Requires at least two files before merging.
- Merges PDFs in the displayed order and downloads the result as `merged.pdf`.
- Rejects requests larger than 50 MB and shows an error if a PDF cannot be read.

## Run the app on your computer

Install Python 3.10 or newer. Open a terminal in the project folder and create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment. Use the command for your terminal:

```bash
# Git Bash on Windows
source .venv/Scripts/activate

# PowerShell on Windows
# .venv\Scripts\Activate.ps1

# macOS or Linux
# source .venv/bin/activate
```

Install the packages and start the app:

```bash
python -m pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000> in a browser. Stop the local server by pressing **Ctrl+C** in the terminal.

## How to use it

1. Choose PDF files with **Select PDF Sheets**, or drop them on the composing table.
2. Review the galley proof. Use the arrows to set the order and **Remove** to take out a file.
3. Select **Run the Press**. The browser downloads `merged.pdf` when the merge succeeds.

## Project files

| File | Purpose |
| --- | --- |
| `app.py` | Flask routes, upload validation, PyPDF2 merge, and download response. |
| `templates/index.html` | Page structure and browser-side file selection, ordering, and submission behavior. |
| `static/style.css` | Page colors, typography, layout, and responsive styling. |
| `requirements.txt` | Python packages needed to run the app. |
| `.gitignore` | Keeps local environments, secrets, and PDF files out of Git commits. |
| `GUIDE.txt` | Plain-text project overview, setup, usage, and review instructions. |

## Uploads and privacy

The app accepts requests up to 50 MB total. Uploaded files are passed to PyPDF2 as in-memory streams and are not saved as uploaded files by this code. When hosted, files are sent to the server running the app for processing. Avoid using a public deployment for confidential PDFs unless you have reviewed the hosting provider and added any access controls you need.

## Publish or deploy

The GitHub repository stores the source code; GitHub does not run this Flask app as a website. This project is deployed on Render as a Python web service:

- **Live app:** <https://pdfmerger-oqrm.onrender.com>
- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`

Open the live app URL in a browser to use it. On Render's free plan, the service can spin down after inactivity, so the first visit after it has been idle may take 50 seconds or more to respond. Wait for it to wake up and load.

Closing the browser tab only closes your view of the app; the Render service and its URL remain available. To take the app offline, use the service controls in the Render dashboard to suspend or delete the web service. Suspending can be reversed; deleting removes the service configuration. The GitHub repository remains separate from the deployed service.



