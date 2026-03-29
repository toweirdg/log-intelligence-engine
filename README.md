# Log Intelligence Engine 🚀

AI-powered backend system to analyze logs, detect anomalies, and automate operational decisions.

---

## 🧠 Problem

Modern systems generate massive volumes of logs. Engineers often struggle to:

* Detect issues quickly
* Identify root causes
* Respond before downtime escalates

---

## 💡 Solution

This project provides a backend system that:

* Ingests logs via API
* Stores them in a structured database
* Processes them asynchronously (next phase)
* Uses AI to generate insights and decisions

---

## ⚙️ Current Features (Phase 1–2)

* ✅ FastAPI backend setup
* ✅ PostgreSQL integration
* ✅ Log ingestion API (`/logs`)
* ✅ Database persistence using SQLAlchemy

---

## 🏗️ Architecture (Current)

Client → FastAPI → PostgreSQL

---

## 🛠️ Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Git

---

## 🚧 Upcoming Features

* Async processing with Celery + Redis
* Log classification & anomaly detection
* AI-based root cause analysis
* Decision engine for automated actions

---

## ▶️ How to Run

```
uvicorn app.main:app --reload
```
---

## Environment Variables

Create a `.env` file in the root directory and configure the following:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/log_engine
OPENAI_API_KEY=your_api_key_here
REDIS_URL=redis://localhost:6379/0

## 📌 Author

Gulshan Kumar

