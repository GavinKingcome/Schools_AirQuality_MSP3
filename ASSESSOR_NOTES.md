# Notes for Assessor - MSP3 Project

## Live Deployment

**Heroku URL:** [https://msp3-schools-pollution-monitor-88e7f4d84e34.herokuapp.com/](https://msp3-schools-pollution-monitor-88e7f4d84e34.herokuapp.com/)

**GitHub Repository:** [https://github.com/GavinKingcome/Schools_AirQuality_MSP3](https://github.com/GavinKingcome/Schools_AirQuality_MSP3)

---

## Quick Start Guide

### Viewing the Application

1. **Open the live site** using the Heroku URL above
2. **Explore the map** - Pan and zoom around Camberwell/Peckham area
3. **Click school markers** - View detailed PM10 and NO2 readings
4. **Use search** - Type school name to quickly locate
5. **Test responsive design** - View on mobile/tablet/desktop

### Current Data

- **6 Schools** in Camberwell/Peckham area
- **12 Air Quality Readings** (PM10 and NO2 for each school)
- **Color-coded markers** based on UK Air Quality Index standards
- **Data freshness** - Only displays readings from last 7 days

---

## Testing the Application

### Manual Testing Checklist

- [x] Map loads correctly with all 6 schools displayed
- [x] School markers show correct colors (green/orange/red)
- [x] Click markers to open popups with pollution data
- [x] Search autocomplete works (try typing "Lyndhurst")
- [x] Responsive design works on mobile (320px), tablet (768px), desktop (1024px+)
- [x] All links and attributions work

### Running Automated Tests

**Local Testing:**

```bash
# Clone the repository
git clone https://github.com/GavinKingcome/Schools_AirQuality_MSP3.git
cd Schools_AirQuality_MSP3

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run tests (20 unit tests)
python manage.py test

# Start local server
python manage.py runserver
```

**Expected Test Results:**

- 20 unit tests should pass ✅
- Coverage: School model, AirQualityReading model, statistical methods

---

## Project Structure

```
Schools_AirQuality_MSP3/
├── monitoring/              # Main Django app
│   ├── models.py           # School & AirQualityReading models
│   ├── views.py            # Map view
│   ├── urls.py             # URL routing
│   ├── tests.py            # 20 unit tests
│   └── templates/          # HTML templates
├── static/                 # CSS, JavaScript, images
│   ├── css/style.css       # Custom styling
│   └── js/map.js           # Leaflet.js map logic
├── schools_airquality_MSP3/ # Django project settings
├── docs/                   # Documentation
│   ├── wireframes/         # Design wireframes (PDF)
│   └── screenshots/        # Application screenshots
├── README.md               # Main project documentation
├── User_Stories.md         # Detailed user stories with acceptance criteria
├── requirements.txt        # Python dependencies
├── Procfile               # Heroku deployment config
└── manage.py              # Django management script
```

---

## Key Features Demonstrated

### Backend Development

- **Django 5.2.8** - Modern Python web framework
- **PostgreSQL** - Production database (Heroku)
- **SQLite** - Development database
- **RESTful API Integration** - OpenAQ air quality data
- **Database Design** - School and AirQualityReading models with relationships
- **ORM Queries** - Complex filtering and aggregation

### Frontend Development

- **Leaflet.js** - Interactive mapping library
- **JavaScript ES6** - Modern syntax and features
- **Responsive CSS** - Mobile-first design
- **AJAX** - Asynchronous data loading
- **DOM Manipulation** - Dynamic content updates

### Testing

- **Unit Tests** - 20 automated tests covering models and logic
- **Test-Driven Development** - Tests written before implementation
- **Manual Testing** - Comprehensive cross-browser/device testing

### Deployment

- **Heroku Platform** - Cloud hosting
- **Gunicorn** - Production WSGI server
- **Whitenoise** - Static file serving
- **PostgreSQL** - Production database
- **Environment Variables** - Secure configuration

---

## User Stories Implementation

**14 of 20 user stories completed for MSP3 v1.0 prototype:**

✅ **Core Features (Implemented):**

- View interactive map of schools
- See color-coded air quality markers
- Click markers for detailed pollution data
- Search for schools by name
- View responsive design on all devices
- See real-time pollution levels
- Understand air quality status at a glance

⬜ **Future Enhancements (Phase 2):**

- Automated data updates (cron jobs)
- Historical data visualization (charts)
- Email alerts for poor air quality
- Additional schools across London
- User accounts and favorites
- Data export functionality

**[Full User Stories Document →](User_Stories.md)**

---

## Data Sources & Attribution

- **Air Quality Data:** OpenAQ Platform (https://openaq.org)
- **Map Tiles:** OpenStreetMap contributors
- **Mapping Library:** Leaflet.js
- **Air Quality Standards:** UK Department for Environment, Food & Rural Affairs (DEFRA)

---

## Known Limitations (Prototype v1.0)

This is a **prototype/proof-of-concept** for MSP3 assessment:

1. **Manual Data Refresh** - Requires running Django shell script to update data
2. **Limited Coverage** - Only 6 schools in Camberwell area (prototype scope)
3. **SQLite for Development** - Production uses PostgreSQL
4. **No Automated Updates** - Data fetching not scheduled (Phase 2 feature)
5. **Static Files Warning** - `/static` directory warning is cosmetic, app works correctly

**Note:** These limitations are documented in README.md as part of the development roadmap.

---

## Technologies Used

**Backend:**

- Python 3.12
- Django 5.2.8
- PostgreSQL (production)
- SQLite (development)
- Requests library

**Frontend:**

- HTML5/CSS3
- JavaScript ES6
- Leaflet.js 1.9.4
- OpenStreetMap tiles

**Deployment:**

- Heroku
- Gunicorn
- Whitenoise
- Git/GitHub

---

## Credits

- **Developer:** Gavin Kingcome
- **Mentor:** Victor Miklovich
- **Course:** Code Institute - Full Stack Software Development
- **Project:** MSP3 - Backend Development with Django/Python

---

## Assessment Criteria Coverage

### LO1: Design & Develop a Full-Stack Web Application

✅ Django-based application with PostgreSQL database
✅ RESTful API integration (OpenAQ)
✅ Interactive frontend with Leaflet.js
✅ Responsive design across devices

### LO2: Implement Data Model

✅ Two related models: School and AirQualityReading
✅ Foreign key relationships
✅ Database migrations
✅ CRUD operations

### LO3: Testing & Documentation

✅ 20 unit tests with TDD approach
✅ Comprehensive README.md
✅ User stories with acceptance criteria
✅ Wireframes and design documentation

### LO4: Deployment

✅ Deployed to Heroku
✅ PostgreSQL production database
✅ Environment-specific settings
✅ Static file serving configured

### LO5: Version Control

✅ Git repository with meaningful commits
✅ GitHub for code hosting
✅ Clear commit history showing development process

---

## Contact

**GitHub:** [@GavinKingcome](https://github.com/GavinKingcome)

**Project Repository:** [Schools_AirQuality_MSP3](https://github.com/GavinKingcome/Schools_AirQuality_MSP3)

---

**Thank you for assessing this project!** 🙏

_Last Updated: November 2025_
