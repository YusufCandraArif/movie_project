# 🎬 Movie App – Django Web Application

A simple Django-based Movie App that lists movie data with a detail view and a JavaScript-powered search bar. Movie data is loaded from a `movies.json` file.

---

## 📁 Features

- 📜 Load movie data from a JSON file
- 🗂️ Movie listing and detail pages
- 🔍 JavaScript search bar to filter movies by name

---

## 🧰 Tech Stack

- Python 3.10+
- Django 4+
- SQLite3
- HTML + JS (Vanilla)
- Docker (optional)

---

## 🔧 Manual Installation (Without Docker)

### ✅ 1. Clone the project

```bash
cd movie-app
```

### ✅ 2. Create virtual environment & activate
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### ✅ 3. Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ 4. Run migrations

```bash
python manage.py migrate
```

### ✅ 5. Start the development server

```bash
python manage.py runserver
```
Visit: http://localhost:8000


🐳 Docker Installation
### ✅ 1. Build Docker image

```bash
docker build -t movie-app .
```

### ✅ 2. Run the container

```bash
docker run -d -p 8000:8000 movie-app
```

Visit: http://localhost:8000