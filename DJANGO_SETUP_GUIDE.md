# Django Project Setup Guide

## 1. Create Virtual Environment

```bash
# Make sure no (base) appears - if it does: conda deactivate
conda deactivate   # ← do this first!
python3 -m venv venv
source venv/bin/activate
which python # verify it points to venv/bin/python
```

## 2. Install Django

```bash
pip install django python-decouple
```

## 3. Create Project

```bash
django-admin startproject project_name .
```

## 4. Create App.

```bash
python manage.py startapp app_name
```

## 5. Test the Server

```bash
python manage.py runserver
```

## 6. Setup .gitignore

Copy from this project or create with:

- venv/, .venv/
- db.sqlite3
- .env, .env.\*
- **pycache**/
- .DS_Store

## 7. Secure SECRET_KEY

In settings.py:

```python
from decouple import config
SECRET_KEY = config('SECRET_KEY', default='django-insecure-local-dev-key')
```

Create `.env`:

```
SECRET_KEY=your-actual-secret-key-from-settings
```

Create `.env.example`:

```
SECRET_KEY=your-secret-key-here
```

## 8. Finalize

```bash
python manage.py migrate
pip freeze > requirements.txt
python manage.py runserver  # test it works
git add .
git commit -m "Initial Django setup"
git push origin main
```

## Common Issues

- If `(base)` appears: run `conda deactivate`
- If django-admin not found: check venv is activated
- If SECRET_KEY error: check `.env` file exists and settings.py imports config

## Daily Workflow (Working on Existing Project)

```bash
# Navigate to project
cd /path/to/project

# Activate virtual environment
source venv/bin/activate

# Run development server
python manage.py runserver
```

To stop the server: `CONTROL-C`
To deactivate venv: `deactivate`
