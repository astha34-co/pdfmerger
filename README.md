# PDF Merge

A small Flask web app that combines PDF files in the order you choose. The merge is performed by PyPDF2 on the server; uploaded files are held in memory during the request and are not written to disk.

## Run locally

Requirements: Python 3.10 or newer.

```bash
git clone https://github.com/YOUR-USERNAME/pdf-merger-web.git
cd pdf-merger-web
python -m venv .venv
```

Activate the environment, then install and run:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux (use this activation command instead)
# source .venv/bin/activate

python -m pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>. To use it from another device on the same Wi-Fi, run `flask --app app run --host=0.0.0.0` and open `http://YOUR-COMPUTER-IP:5000` on that device. Both devices need to be on the same network, and the computer firewall must allow the connection.

## Publish the code on GitHub

Create an empty repository on GitHub, then from this project folder run:

```bash
git init
git add .
git commit -m "Initial PDF merger app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/pdf-merger-web.git
git push -u origin main
```

Replace the sample repository URL with your own. GitHub stores the code; it does not run this Flask app as a website.

## Deploy a shareable website

This repository includes `render.yaml` for Render. Push the project to GitHub, sign in to Render, choose **New > Blueprint**, and select the repository. Render reads the configuration, installs `requirements.txt`, and starts the web service. Once deployment finishes, open the provided `onrender.com` URL from any device.

## Usage and limits

1. Select or drop at least two PDFs.
2. Use the list to check their merge order and remove files if needed.
3. Choose **Merge PDFs**. The browser downloads `merged.pdf`.

The app accepts requests up to 50 MB total. It does not retain uploaded files after a request. For public production use with untrusted traffic, add rate limiting and stronger content validation, and review the hosting provider's upload and privacy limits.
