## 🏆 Scoreboard

A Django REST API for managing user profiles, game points, ranks, and activity logs.
Users can register, earn points, level up through ranks, and view leaderboard statistics.

## 🚀 Features

User registration with automatic game tag generation

Points submission and leaderboard ranking

Automatic rank assignment based on total points

Full activity logging (rank ups, point additions, etc.)

RESTful API built with Django REST Framework

## 🧠 Tech Stack

Backend: Python, Django, Django REST Framework

Database: PostgreSQL (or SQLite for development)

Auth: Django built-in authentication

Other: Signals, Serializers, API Views

## ⚙️ Installation
git clone https://github.com/NickDust/scoreboard.git
cd scoreboard
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

👨‍💻 Author

Niccolò Stella
📍 Łódź, Poland

Made with ❤️ while learning Django REST Framework.