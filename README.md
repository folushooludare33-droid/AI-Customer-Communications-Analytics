# AI Customer Communications Analytics Platform

An end-to-end AI-powered customer communications analytics platform built with Python, SQLAlchemy, SQLite, and Power BI.

The platform generates realistic customer emails, analyzes them using an AI pipeline, stores the enriched data in a database, exports it to CSV, and visualizes business insights through an interactive Power BI dashboard.

---

## Features

- Synthetic customer email generation
- AI-powered email analysis
  - Category classification
  - Department routing
  - Priority classification
  - Sentiment analysis
  - Automatic summarization
  - Draft reply generation
- SQLite database using SQLAlchemy ORM
- CSV export
- Interactive Power BI dashboard
- Clean Architecture
- Modular, scalable design

---

## Tech Stack

- Python 3.12
- SQLAlchemy 2.x
- SQLite
- Power BI
- Dataclasses
- Logging
- Object-Oriented Programming

---

## Project Workflow

```text
Synthetic Email Generator
        │
        ▼
AI Pipeline
        │
        ▼
SQLite Database
        │
        ▼
CSV Export
        │
        ▼
Power BI Dashboard
        │
        ▼
Business Insights
```

---

## Project Structure

```text
AI-Customer-Communications-Analytics/

app/
│
├── ai/
├── analytics/
├── config/
├── database/
├── demo_data/
├── email_sources/
├── exporters/
├── models/
├── pipeline/
├── services/
└── utils/

assets/
docs/
powerbi/
scripts/
tests/

data/
├── database/
├── exports/
├── logs/
└── sample_data/

main.py
requirements.txt
README.md
```

---

## Dashboard

The Power BI dashboard includes:

- Total Emails
- High Priority Emails
- Negative Sentiment Emails
- Open Cases
- Email Categories
- Department Workload
- Product Issue Trends
- Priority Distribution
- Sentiment Distribution
- Email Trends Over Time
- Interactive Filters

---

## Getting Started

Clone the repository.

```bash
git clone <repository-url>
```

Create and activate a virtual environment.

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python main.py
```

The application will:

- Generate 500 synthetic customer emails
- Analyze each email using the AI pipeline
- Store results in SQLite
- Export a CSV dataset
- Prepare the data for Power BI

---

## Repository Highlights

- Production-style project structure
- SOLID design principles
- Separation of concerns
- Modular AI pipeline
- ORM-based persistence
- Recruiter-friendly architecture
- End-to-end analytics workflow

---

## Future Improvements

- Gmail API integration
- OpenAI API integration
- REST API
- Docker support
- CI/CD pipeline
- Cloud deployment
- Automated testing

---

## License

MIT License