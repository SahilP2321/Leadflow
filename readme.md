# 🚀 SimplifIQ Lead Automation System

<div align="center">

# Intelligent Lead Capture & Automated Business Audit Platform

### Built with Django • Celery • Redis • HTMX • ReportLab

<br/>

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="70" alt="Python"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="70" alt="Django"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" width="70" alt="Redis"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="70" alt="SQLite"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="70" alt="HTML"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="70" alt="CSS"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="70" alt="JavaScript"/>

<br/><br/>

![Django](https://img.shields.io/badge/Django-5.0-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Celery](https://img.shields.io/badge/Celery-Async%20Tasks-brightgreen?style=for-the-badge)
![Redis](https://img.shields.io/badge/Redis-Queue-red?style=for-the-badge&logo=redis)
![HTMX](https://img.shields.io/badge/HTMX-Dynamic%20UI-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

# 📌 Overview

SimplifIQ Lead Automation is a fully automated lead management and business audit platform built using Django, Celery, Redis, and intelligent web scraping workflows.

The system captures lead information, enriches company data by scraping public business websites, generates professional PDF audit reports, and automatically emails them to prospects — all without manual intervention.

This project demonstrates:

- Backend automation workflows
- Async task processing using Celery
- Real-world web scraping pipelines
- Automated PDF generation
- Email automation systems
- Dynamic frontend updates using HTMX
- Production-ready Django architecture

---

# ✨ Features

## 📝 Smart Lead Intake
- Professional lead capture form
- Real-time validation
- Company and contact information handling
- Responsive frontend UI

---

## 🌐 Company Data Enrichment
- Website scraping and analysis
- Metadata extraction
- Heading/content extraction
- Navigation analysis
- Business insight collection

---

## 📄 Automated PDF Report Generation
- Professional multi-page audit reports
- Dynamic report sections
- Styled layouts using ReportLab
- Business recommendations and summaries

---

## 📧 Automated Email Delivery
- Automatically sends reports to leads
- Attachment handling
- SMTP email integration
- Customizable templates

---

## ⚡ Async Background Processing
- Celery task queue integration
- Redis broker support
- Non-blocking workflow execution
- Scalable backend architecture

---

## 🔄 Real-Time UI Updates
- HTMX-powered frontend updates
- Smooth status tracking
- No page refresh required

---

## 🗄️ Database Management
- SQLite for development
- Easy PostgreSQL migration support
- Lead tracking and persistence

---

# 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Django 5 |
| Frontend | HTML, CSS, JavaScript, HTMX |
| Task Queue | Celery |
| Broker | Redis |
| Database | SQLite |
| PDF Generation | ReportLab |
| Web Scraping | BeautifulSoup4, Requests |
| Email Service | SMTP / Gmail |
| Environment Management | Python Dotenv |

---

# 🧠 Workflow Architecture

```text
Lead Form Submission
        ↓
Store Lead in Database
        ↓
Celery Background Task Triggered
        ↓
Website & Company Data Scraping
        ↓
Business Audit Processing
        ↓
Professional PDF Generation
        ↓
Automated Email Delivery
        ↓
Frontend Status Update
```

---

# 📂 Project Structure

```text
simplifiq-automation/
│
├── lead_automation/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   └── wsgi.py
│
├── leads/                    # Main application
│   ├── migrations/
│   ├── services/
│   │   ├── enricher.py
│   │   ├── report_generator.py
│   │   ├── email_service.py
│   │   └── scraper.py
│   │
│   ├── templates/
│   ├── static/
│   ├── tasks.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── media/reports/            # Generated reports
├── static/
├── requirements.txt
├── manage.py
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/simplifiq-automation.git

cd simplifiq-automation
```

---

## 2️⃣ Create Virtual Environment

### macOS/Linux

```bash
python3.11 -m venv .venv

source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create `.env`

```env
# Django
DJANGO_SECRET_KEY=your-secret-key

# Email Configuration
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

---

## 5️⃣ Run Database Migrations

```bash
python manage.py migrate
```

---

# ▶️ Running the Project

## Terminal 1 — Start Redis

```bash
redis-server
```

---

## Terminal 2 — Start Celery Worker

```bash
celery -A lead_automation worker -l info --pool=solo
```

---

## Terminal 3 — Run Django Server

```bash
python manage.py runserver
```

---

# 🌍 Open in Browser

```text
http://127.0.0.1:8000
```

---

# 📦 Core Functionalities

## 🔍 Web Scraping Engine

The platform intelligently scrapes:

- Website titles
- Meta descriptions
- H1/H2 headings
- Navigation links
- Website paragraphs
- Business information

Using:

```python
requests
BeautifulSoup4
```

---

## 📄 PDF Report Generator

Professional reports are generated dynamically using:

```python
ReportLab
```

Features include:

- Styled typography
- Structured layouts
- Business recommendations
- Audit summaries
- Automated formatting

---

## ⚡ Celery Background Tasks

Heavy operations like:

- Scraping
- PDF generation
- Email sending

run asynchronously using:

```python
Celery + Redis
```

This keeps the application responsive and scalable.

---

# 🔐 Environment Variables

| Variable | Description |
|---|---|
| DJANGO_SECRET_KEY | Django security key |
| EMAIL_HOST_USER | Gmail email address |
| EMAIL_HOST_PASSWORD | Gmail app password |
| DEFAULT_FROM_EMAIL | Sender email |

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- Django backend architecture
- Celery task queues
- Redis integration
- Web scraping pipelines
- PDF automation
- SMTP email systems
- Async workflows
- HTMX dynamic updates
- Production-ready project structuring

---

# 🚀 Future Improvements

- PostgreSQL integration
- Docker deployment
- Admin analytics dashboard
- AI-powered business recommendations
- User authentication
- CRM integrations
- Cloud deployment
- REST APIs

---

# 👨‍💻 Author

## Sahil Patil

Backend Developer • Automation Enthusiast • ML Aspirant

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

### ⭐ If you liked this project, consider giving it a star ⭐

</div>