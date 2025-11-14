# Early Years Schools Pollution Monitor (MSP3)

A Django-based web application that monitors and visualizes real-time air quality data for early years schools in London. This interactive map displays PM10 and NO2 pollution levels using data from the OpenAQ API.

![Project Screenshot](docs/screenshots/map-desktop.png)

**Live Demo:** [Add your deployed link here]

---

## 📖 Table of Contents

- [About](#about)
- [Features](#features)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [User Stories](#user-stories)
- [Design & Wireframes](#design--wireframes)
- [Testing](#testing)
- [Known Limitations](#known-limitations)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)
- [License](#license)

---

## About

This is a **prototype application** developed as part of Code Institute's MSP3 (Milestone Project 3) to demonstrate backend development with Django/Python, RESTful API integration, database design, and interactive data visualization.

### Project Purpose

Air quality significantly impacts children's health and development. This application provides parents, school administrators, and researchers with accessible, real-time information about pollution levels at early years schools in London.

### Project Goals

- ✅ Monitor real-time air quality (PM10 and NO2) at early years schools
- ✅ Provide accessible, visual data through an interactive map
- ✅ Demonstrate full-stack development skills with Django/Python
- ✅ Follow Test-Driven Development (TDD) practices
- ✅ Create a foundation for future production system

### Future Development

This prototype serves as a foundation for a more comprehensive system that will include:

- Migration to **PostgreSQL** and **TimescaleDB** for time-series data
- Integration with **London Air Quality Network (LAQN)** for more localized data
- Historical data analysis and trend visualization
- Statistical analysis and predictive modeling
- Email alert system for poor air quality events
- Expanded school coverage across Greater London

---

## ✨ Features

### Current Implementation (v1.0)

- 🗺️ **Interactive Map** - Leaflet.js-powered map centered on London/Camberwell
- **6 Schools** - Early years schools in Camberwell/Peckham area
- **Color-Coded Markers** - Visual indicators based on UK Air Quality Index
  - 🟢 Good (Dark Green)
  - 🟠 Moderate (Orange)
  - 🟠 Poor (Orange-Red)
  - 🔴 Very Poor (Dark Red)
- **School Search** - Autocomplete dropdown to find schools quickly
- **Detailed Popups** - Click markers to see specific PM10 and NO2 levels
- **Responsive Design** - Works on desktop, tablet, and mobile devices
- ⏱**Data Freshness** - Only displays readings from the last 7 days
- **Real-time Data** - Live pollution readings from OpenAQ API

### Air Quality Standards (UK Index)

**PM10 Levels:**

- Good: 0-20 µg/m³
- Moderate: 21-40 µg/m³
- Poor: 41-50 µg/m³
- Very Poor: 50+ µg/m³

**NO2 Levels:**

- Good: 0-40 µg/m³
- Moderate: 41-100 µg/m³
- Poor: 101-200 µg/m³
- Very Poor: 200+ µg/m³

---

## 📸 Screenshots

### Desktop View

![Desktop Map View](docs/screenshots/desktop.png)
_Interactive map showing color-coded school markers and detailed popup_

### Mobile View

![Mobile Map View](docs/screenshots/mobile.png)
_Responsive design optimized for mobile devices_

### School Detail Popup

![School Popup](docs/screenshots/popup.png)
_Detailed air quality information with color-coded status indicators_

---

## 🛠️ Technologies Used

### Backend

- **Python 3.12** - Programming language
- **Django 5.1.3** - Web framework
- **SQLite3** - Database (development/prototype)
- **Requests** - HTTP library for API calls

### Frontend

- **HTML5/CSS3** - Structure and styling
- **JavaScript (ES6)** - Interactive functionality
- **Leaflet.js 1.9.4** - Interactive mapping library
- **OpenStreetMap** - Map tiles and data

### APIs & Data Sources

- **OpenAQ API** - Real-time air quality data
- **Attribution**: Data provided by OpenAQ platform

### Development Tools

- **Git/GitHub** - Version control
- **VS Code** - IDE
- **Chrome DevTools** - Testing and debugging
- **Python unittest** - Test framework
- **Figma** - Wireframing and UI design

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Local Development Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Schools_AirQuality_MSP3.git
   cd Schools_AirQuality_MSP3
   ```

2. **Create virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up database**

   ```bash
   python manage.py migrate
   ```

5. **Load initial school data**

   ```bash
   python manage.py shell
   # Run the school creation script (see docs/setup.md)
   ```

6. **Fetch air quality data**

   ```bash
   python manage.py shell
   # Run the OpenAQ data fetch script (see docs/api_usage.md)
   ```

7. **Run development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   Open browser to `http://127.0.0.1:8000/`

---

## Usage

### Viewing Air Quality Data

1. **Browse the Map** - Pan and zoom to explore the area
2. **Click School Markers** - View detailed pollution information
3. **Use Search** - Type school name in the search box to quickly locate
4. **Check Color Coding** - Marker colors indicate overall air quality status

### Understanding the Data

- **Overall Status**: Based on the worst pollutant (PM10 or NO2)
- **Individual Readings**: Each pollutant shown with its own status
- **Data Age**: Only readings from the last 7 days are displayed

---

## User Stories

This project follows Agile methodology with user stories developed for each feature. User stories guided the development process and were implemented using Test-Driven Development (TDD) where applicable.

### User Personas

**Parents & Guardians**

- Monitor air quality near their child's school
- Understand if pollution levels are safe
- Access information easily on mobile devices

**School Administrators**

- Track pollution levels over time
- Compare air quality with nearby schools
- Receive clear visual indicators

**Environmental Health Researchers**

- Access reliable, real-time pollution data
- Identify schools in high-pollution areas
- Analyze trends across multiple locations

**Developers & Maintainers**

- Write clean, maintainable code
- Implement comprehensive testing
- Follow Django best practices

### Implementation Status

**MSP3 v1.0 (Prototype):** 14/20 user stories complete ✅

- ✅ Core features: Map, search, real-time data, responsive design
- ⬜ Future features: Automated updates, historical charts, alerts

**[📄 View Complete User Stories with Acceptance Criteria & Tasks →](User_Stories.md)**

---

## Design & Wireframes

Wireframes were created in Figma to plan the user interface and user experience before development. The wireframes include three key views: desktop map, mobile responsive layout, and popup detail.

**[📄 View All Wireframes (PDF - 3 Frames)](docs/wireframes/wireframes.pdf)**

### Wireframe Contents

**Frame 1: Desktop Map View (1920 x 1080)**

- Full-screen interactive map with OpenStreetMap tiles
- Search box positioned top-right with autocomplete dropdown
- Zoom controls in top-left corner
- Color-coded school markers (green/orange/red based on air quality)
- Sample popup showing detailed air quality data
- Professional gradient header with project title

**Frame 2: Mobile Responsive View (393 x 852)**

- Full-width search bar optimized for touch interaction
- Compact header to maximize map viewing area
- Repositioned zoom controls for thumb accessibility
- Touch-friendly marker sizes
- Vertical stacked layout for small screens

**Frame 3: Popup Detail View**

- School name and full address
- Overall air quality status with color-coded header
- Individual PM10 reading with status indicator
- Individual NO2 reading with status indicator
- Clean, scannable information hierarchy

### Design Evolution

**Changes from wireframe to final implementation:**

- ✅ Removed legend box (information moved to popups for cleaner UI)
- ✅ Changed bright yellow to orange for better contrast on white map background
- ✅ Added gradient header (#0078a8 to #005f87) for professional appearance
- ✅ Enhanced popup styling with color-coded sections and gray backgrounds
- ✅ Improved mobile spacing to prevent UI element overlap
- ✅ Increased marker sizes for better touch targeting on mobile devices

---

## 🧪 Testing

### Test-Driven Development (TDD)

This project follows TDD principles with comprehensive unit tests for backend functionality.

**Run all tests:**

```bash
python manage.py test
```

**Run specific test:**

```bash
python manage.py test monitoring.tests.SchoolModelTest
```

### Test Coverage

| Component               | Tests          | Status      |
| ----------------------- | -------------- | ----------- |
| School Model            | 5 unit tests   | ✅ Passing  |
| AirQualityReading Model | 7 unit tests   | ✅ Passing  |
| Statistical Methods     | 8 unit tests   | ✅ Passing  |
| Map View                | Manual testing | ✅ Verified |
| Search Functionality    | Manual testing | ✅ Verified |
| Responsive Design       | Manual testing | ✅ Verified |

**Total Automated Tests:** 20 passing ✅  
**Manual Testing:** All features tested on desktop, tablet (768px), mobile (320px) ✅

### Manual Testing Checklist

- [x] Map loads correctly
- [x] All 6 schools display as markers
- [x] Markers show correct colors based on pollution levels
- [x] Search box autocomplete works
- [x] Clicking markers opens popups with correct data
- [x] Mobile responsive design works (320px, 768px, 1024px)
- [x] Attribution links work
- [x] Data freshness filter (7 days) working

---

## Current School Coverage

**6 Schools in Camberwell/Peckham Area:**

1. Lyndhurst Primary School
2. Brunswick Park Primary School
3. Bellenden Primary School
4. The Grove Nursery School
5. Dog Kennel Hill Primary School
6. Bessemer Grange Primary School

All schools located within ~1.5km of Camberwell air quality monitoring stations.

---

## Data Sources & Attribution

- **Air Quality Data**: [OpenAQ](https://openaq.org) - Open-source air quality data platform
- **Map Tiles**: [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors
- **Mapping Library**: [Leaflet.js](https://leafletjs.com)

### Data Limitations

- Data freshness: Only readings from last 7 days are displayed
- Coverage: Limited to areas with OpenAQ monitoring stations
- Update frequency: Dependent on OpenAQ data availability
- This is a **prototype** - not for critical decision-making

---

## Known Limitations (MSP3 Prototype)

- **Manual Data Refresh** - Requires running Django shell script to fetch new data
- **SQLite Database** - Not suitable for production (will migrate to PostgreSQL)
- **Limited Coverage** - Only 6 schools in Camberwell (prototype scope)
- **No Historical Visualization** - Statistical methods exist but not displayed in UI
- **No Automated Updates** - Data fetching not scheduled (will add cron jobs)
- **Basic Error Logging** - No monitoring dashboard (Phase 2)

---

## Future Enhancements (Phase 2)

### Database & Infrastructure

- [ ] Migrate to PostgreSQL
- [ ] Implement TimescaleDB for time-series data
- [ ] Set up automated backups
- [ ] Deploy to cloud platform

### Data Collection

- [ ] Integrate with London Air Quality Network (LAQN)
- [ ] Create Django management command for automation
- [ ] Set up cron job for automatic updates
- [ ] Email notifications for data fetch failures

### Analytics & Visualization

- [ ] Add statistics panel to popups (7-day averages, peaks)
- [ ] Create interactive charts (Chart.js) for historical trends
- [ ] Heatmap visualization
- [ ] Comparison tools between schools

### User Features

- [ ] Email alerts for poor air quality
- [ ] User accounts and favorites
- [ ] Export data as CSV/PDF
- [ ] Share functionality

### Expansion

- [ ] Add 50+ schools across London
- [ ] Multiple cities support
- [ ] Additional pollutants (SO2, O3, CO)
- [ ] Public API for researchers

**[View Detailed Phase 2 Plans →](User_Stories.md#future-enhancements-phase-2---production-version)**

---

## Credits & Acknowledgments

**Development & Mentorship:**

- **Victor Miklovich** - Mentor, for invaluable guidance and support
- **Code Institute** - Project guidance and curriculum

**Data & Tools:**

- **OpenAQ** - Free, open-source air quality data
- **OpenStreetMap Contributors** - Map data
- **Leaflet.js** - Mapping library
- **Django Community** - Excellent documentation and support
- **GitHub Copilot** - Development assistance and debugging support

---

## Author

**Gavin Kingcome**

- GitHub: [@gavinkingcome](https://github.com/yourusername)
- Project Link: [https://github.com/yourusername/Schools_AirQuality_MSP3](https://github.com/yourusername/Schools_AirQuality_MSP3)

---

**Note**: This is a prototype educational project. Air quality data should not be used for critical health or safety decisions. Always refer to official government sources for actionable air quality information.

---

_Last Updated: November 2025_  
_MSP3 - Code Institute Full Stack Software Development_
