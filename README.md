# AiDD Personal Website (Flask)

This repository contains a simple Flask wrapper around the static personal website. It serves your existing `assets/` and `images/` folders and converts the HTML pages to Jinja templates.

Quick start (Windows PowerShell):

1. Create a virtual environment (optional but recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python app.py
```

4. Open http://127.0.0.1:5000 in your browser.

Notes:
- Static files are served from the project root so your existing `assets/` and `images/` folders work without modification.
- The contact form posts to the server and currently redirects to a thank-you page; it does not yet send email or persist messages.
