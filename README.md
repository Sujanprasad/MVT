# MVT — Django Sample Project

A simple Django project demonstrating the MVT (Model–View–Template) architecture.
Includes example apps, views, templates, and basic admin usage for learning Django fundamentals.

# 📁 Project Structure
MVT/
├── Project/       # Django project (settings, urls, wsgi)
├── Myapp/         # Example Django app (views, templates, models)
├── Admin/         # Admin customization or additional demo app
├── db.sqlite3     # Example SQLite database
└── manage.py

# 🛠 Requirements

Python 3.8+

Django (install using pip install django)

Virtual environment recommended

# 🚀 How to Run
# Clone the repository
git clone https://github.com/Sujanprasad/MVT.git
cd MVT

# Create virtual environment
python -m venv .venv
 Activate it
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install Django
pip install django

# Run migrations (skip if db.sqlite3 already exists)
python manage.py migrate

# Start the server
python manage.py runserver


Open your browser at:
http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/

# 📘 Features

Clear example of Django MVT flow

Simple URL routing

Views rendering templates

Basic admin setup

SQLite database for quick testing

# 📄 Useful Commands
python manage.py runserver

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
