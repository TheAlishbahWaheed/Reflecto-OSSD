# Reflecto: Python/Flask Port

Personal productivity app: Mood · Journal · Study Notes · Tasks · Timer

## Stack
- **Language**: Python 3.10+
- **Framework**: Flask
- **Database**: JSON files (`data/` directory)
- **Libraries**: datetime, os, json, hashlib, csv, io, re, reportlab

## Setup

```bash
# 1. Clone / place files in a folder
cd reflecto/

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
python app.py

Open **http://localhost:5000** in your browser.

## Project Structure

reflecto/
├── app.py              # Flask routes + helpers
├── data.py             # JSON storage layer
├── requirements.txt
├── data/               # Auto-created; one .json per user
├── static/
    ├── app.js          # backend handling
│   └── style.css       # All themes (12 colour schemes)
└── templates/
    ├── index.html      # Login page
    └── app.html        # Main dashboard (all pages)
    └── base.html       # template for flask/jinja

## Features
| Feature | Details |
|---|---|
| Auth | Per-user SHA-256 hashed passwords, session-based |
| Mood Board | 16 mood chips, streak tracker, 90-entry log |
| Journal | Rich entries with tags, word count, edit/delete |
| Study Notes | Category filter, pin, CSV export per note |
| Tasks | Priority (high/medium/low), due dates, overdue detection |
| Timer | Countdown, Stopwatch (laps), Alarm, all client-side JS |
| PDF Export | Full data export via ReportLab (/export_pdf`) |
| Themes | 12 colour themes |
| Data Reset | Wipes all data but keeps theme |



## Git Setup
git init
git add .
git commit -m "Initial Reflecto Flask port"

