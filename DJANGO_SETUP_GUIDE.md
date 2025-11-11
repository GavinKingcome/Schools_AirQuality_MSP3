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
pip install --upgrade pip
pip install django
django-admin --version  # verify installation
```

## 3. Create Project

```bash
django-admin startproject schools_airquality_MSP3 .
```

Note: The `.` creates the project in the current directory

## 4. Setup .gitignore

Create `.gitignore` before first commit:

```bash
touch .gitignore
code .gitignore  # or nano .gitignore
```

Include:
- venv/, .venv/
- db.sqlite3
- .env, .env.*
- __pycache__/
- .DS_Store
- *.log

## 5. Initial Database Setup

```bash
python manage.py migrate
```

This creates the SQLite database with Django's built-in tables.

## 6. Test the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` - should see Django welcome page
Stop server: `CTRL + C`

## 7. First Commit

```bash
git add .
git commit -m "Initial Django project setup with venv and .gitignore"
git push origin main
```

---

## Next Steps (Not Done Yet)

### Create App

```bash
python manage.py startapp monitoring
```

Then add `'monitoring'` to `INSTALLED_APPS` in `settings.py`

### Secure SECRET_KEY (Optional - do later)

Install python-decouple:
```bash
pip install python-decouple
```

In settings.py:
```python
from decouple import config
SECRET_KEY = config('SECRET_KEY', default='django-insecure-local-dev-key')
```

Create `.env`:
```
SECRET_KEY=your-actual-secret-key-from-settings
```

### Create Superuser (for Django admin)

```bash
python manage.py createsuperuser
```

---

## Daily Workflow (Working on This Project)

```bash
# Navigate to project
cd /Users/GK/Documents/vscode-projects/Schools_AirQuality_MSP3

# Deactivate conda if (base) appears
conda deactivate

# Activate virtual environment
source venv/bin/activate

# Verify you're in venv
which python  # should show: .../Schools_AirQuality_MSP3/venv/bin/python

# Run development server
python manage.py runserver
```

To stop the server: `CTRL + C`
To deactivate venv: `deactivate`

## Common Issues

- If `(base)` appears: run `conda deactivate` before activating venv
- If django-admin not found: check venv is activated with `which python`
- If venv doesn't activate: make sure you're in the project directory
- If SECRET_KEY error (later): check `.env` file exists and settings.py imports config

## What's Been Done

✅ Virtual environment created  
✅ Django 5.2.8 installed  
✅ Project `schools_airquality_MSP3` created  
✅ `.gitignore` configured  
✅ Database migrated  
✅ Committed to GitHub  

## What's Next

⏳ Create monitoring app  
⏳ Create models (Schools, AirQualityData)  
⏳ Set up Django admin  
⏳ Create views and templates  