# 🧩 MVT — Django Sample Project

A beginner-friendly Django project that demonstrates the **MVT (Model – View – Template)** architecture in Django.  
This project includes sample apps, views, templates, routing, and admin functionality to help understand Django fundamentals practically.

---

## 📌 About the Project

This project is designed for learning how Django works internally using the **MVT architecture**:

- **Model** → Handles database structure
- **View** → Contains application logic
- **Template** → Manages frontend/UI rendering

It is a simple and clean project suitable for:
- Django beginners
- College mini projects
- Python web development practice
- Understanding Django routing and templates

---

# 🏗️ Project Structure

```bash
MVT/
│
├── Project/            # Main Django project files (settings, urls, wsgi)
├── Myapp/              # Main application (views, models, templates)
├── Admin/              # Admin customization/demo app
├── db.sqlite3          # SQLite database
├── manage.py           # Django management script
└── README.md
```

---

# 🚀 Features

✅ Demonstrates Django MVT architecture  
✅ Simple and clean project structure  
✅ URL routing examples  
✅ Template rendering using views  
✅ SQLite database integration  
✅ Django admin panel support  
✅ Beginner-friendly codebase  
✅ Easy setup and execution  

---

# 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Backend Programming |
| Django | Web Framework |
| SQLite | Database |
| HTML/CSS | Frontend Templates |

---

# 📋 Requirements

Before running the project, make sure you have:

- Python 3.8+
- pip
- Virtual Environment (recommended)

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sujanprasad/MVT.git
cd MVT
```

---

## 2️⃣ Create Virtual Environment

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Django

```bash
pip install django
```

---

## 4️⃣ Run Database Migrations

```bash
python manage.py migrate
```

---

## 5️⃣ Start the Development Server

```bash
python manage.py runserver
```

---

# 🌐 Access the Project

### Home Page
```text
http://127.0.0.1:8000/
```

### Admin Panel
```text
http://127.0.0.1:8000/admin/
```

---

# 🔑 Create Admin User (Optional)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Then login using your credentials.

---

# 📘 Understanding the MVT Flow

```text
User Request
     ↓
URLs (urls.py)
     ↓
Views (views.py)
     ↓
Models (models.py)
     ↓
Templates (HTML files)
     ↓
Response to User
```

---

# 📂 Useful Django Commands

## Run Server
```bash
python manage.py runserver
```

## Create Migrations
```bash
python manage.py makemigrations
```

## Apply Migrations
```bash
python manage.py migrate
```

## Create Superuser
```bash
python manage.py createsuperuser
```

---

# 🎯 Learning Outcomes

By exploring this project, you will learn:

- Django project structure
- URL routing
- Template rendering
- Database migrations
- Admin panel usage
- Basic CRUD workflow
- MVT architecture implementation

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

# 👨‍💻 Author

## Sujan Prasad

Computer Science & Information Technology Student  
Passionate about Python, Django, Web Development & Open Source

---

# 📜 License

This project is open-source 
