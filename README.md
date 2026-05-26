# 🏟️ Indoor Sports Management System

## Overview

A full-stack sports facility booking and management system built with Django (backend) and React (frontend). The platform enables seamless court/facility reservations with dynamic pricing, equipment rental workflows, and integrated Stripe payment processing. Developed by a 9-person Agile/Scrum team as part of a Software Engineering course project.

## Tech Stack

- **Frontend:** React, JavaScript, HTML5, CSS3
- **Backend:** Django, Python, Django REST Framework
- **Database:** PostgreSQL / SQLite
- **Payments:** Stripe REST API, OAuth 2.0
- **Authentication:** JWT / Session-based Auth
- **DevOps:** Git, Agile/Scrum (11 Branches, 54 Commits)
- **Other:** ASGI/WSGI server, WebSocket support

## Features

- 🏓 **Dynamic Booking Engine** — Reserve courts/facilities with peak and off-peak dynamic pricing
- 💳 **Stripe Payment Integration** — Secure REST API-based payment processing with OAuth 2.0
- 🎽 **Equipment Rental Workflows** — Browse, reserve, and manage sports equipment rentals
- 👤 **User Account Management** — Registration, login, profile management, and booking history
- 📊 **Admin Dashboard** — Financial reporting, booking oversight, and inventory management
- 🔔 **Real-time Updates** — WebSocket-powered live notifications via ASGI configuration

## How to Run

```bash
# Clone the repository
git clone https://github.com/Phoenixking-04/SE-Project.git
cd SE-Project/indoor_sports

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Add your STRIPE_SECRET_KEY, DATABASE_URL, SECRET_KEY

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

For frontend (if separate React app):
```bash
cd frontend
npm install
npm start
```

## Results / Outcomes

- ✅ Led a **9-person Agile/Scrum team** across multiple sprints with 54 commits and 11 feature branches
- ✅ Successfully integrated **Stripe REST API** for live payment processing with OAuth 2.0 security
- ✅ Delivered a fully functional **booking engine** with peak/off-peak dynamic pricing logic
- ✅ Implemented **admin financial reporting** dashboard for revenue and booking analytics
- ✅ Achieved **37 successful deployments** with CI/CD pipeline integration

---

> 🔗 **Developer:** [Kalyankumar Sandireddy](https://kalyankumar-sandireddy.online) | [LinkedIn](https://www.linkedin.com/in/kalyankumar-sandireddy-400681176)
