# Schools Air Quality Monitoring System

A Django web application for monitoring and analyzing air quality data at schools, developed using Test-Driven Development (TDD) methodology.

## Project Overview

This application allows users to:
- Track air quality readings from multiple schools
- Store pollution monitoring data
- Calculate and display average air quality metrics
- Visualize trends and patterns in school air quality

## Technology Stack

- **Framework:** Django 5.2.8
- **Language:** Python 3.13.0
- **Database:** SQLite (development)
- **Testing:** Django's built-in test framework
- **Development Approach:** Test-Driven Development (TDD)

## Database Architecture

### Current Implementation
- **Database:** SQLite3
- **Rationale:** Simplicity for development and assessment
- All CRUD operations for schools and air quality readings
- Supports Django ORM queries for statistics

### Future Scalability Plan
- **Planned Migration:** PostgreSQL with TimescaleDB extension
- **Benefits:**
  - Optimized for time-series pollution data
  - Automatic data partitioning by time
  - Fast aggregation queries (hourly/daily averages)
  - Production-ready scalability
- **Implementation:** Change database backend in settings.py (5 lines)
- **Timeline:** Post-MSP3 submission enhancement

## Air Quality Data Sources

### Current Implementation (MSP3)
- **API:** OpenAQ (Open Air Quality)
- **Endpoint:** https://api.openaq.org/v2/
- **Coverage:** Global air quality measurements
- **Rationale:** 
  - Proof of concept with worldwide applicability
  - No API key required
  - Simple integration for TDD development
  - Assessors can test with any location

### Planned Migration (Final Project)
- **Primary Source:** London Air Quality Network (LAQN)
- **API:** https://www.londonair.org.uk/LondonAir/API/
- **Benefits:**
  - Official UK government monitoring data
  - Operated by King's College London & Imperial College
  - Real monitoring stations (not interpolated)
  - Hourly granular data for London
  - Used for regulatory compliance reporting
- **Fallback:** OpenAQ for schools outside London
- **Implementation:** Swap API endpoint in fetch command (15 lines of code)
- **Timeline:** Post-MSP3 enhancement for final project

### Data Accuracy Considerations

**OpenAQ (Current):**
- Aggregates from multiple sources globally
- May include interpolated values between stations
- Good for proof-of-concept and broad coverage

**LAQN (Planned):**
- Direct measurements from calibrated equipment
- No interpolation - actual readings from specific sites
- Higher accuracy for London-based schools
- Official data trusted by researchers and policymakers

**Why Both?**
- LAQN for London schools (maximum accuracy)
- OpenAQ for schools outside London (broad coverage)
- Demonstrates adaptable architecture

## Test-Driven Development Approach

This project follows **TDD principles** throughout development:

### TDD Workflow

1. **Write a failing test** - Define expected behavior before implementation
2. **Run tests** - Confirm the test fails (Red)
3. **Write minimal code** - Implement just enough to pass the test
4. **Run tests again** - Confirm the test passes (Green)
5. **Refactor** - Improve code while keeping tests green
6. **Repeat** - Continue cycle for each feature

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for monitoring app only
python manage.py test monitoring

# Run specific test file
python manage.py test monitoring.tests.test_models

# Run with verbose output
python manage.py test --verbosity=2
```

### Test Coverage

Tests are organized in the `monitoring/tests/` directory:

```
monitoring/tests/
├── __init__.py
├── test_models.py          # School and AirQualityReading model tests
├── test_views.py           # View logic and template rendering tests
├── test_calculations.py    # Data analysis and averaging tests
└── test_forms.py           # Form validation tests
```

### Git Commit History

The commit history demonstrates TDD workflow:
- Test commits precede implementation commits
- Format: "Add test for [feature]" followed by "Implement [feature]"
- Each feature developed test-first

Example commit sequence:
```
✅ Add test for School model with name and location fields
✅ Implement School model
✅ Add test for AirQualityReading model relationships
✅ Implement AirQualityReading model
✅ Add test for calculate_average_pollution method
✅ Implement average pollution calculation
```

## Installation & Setup

### Prerequisites

- Python 3.13+
- Git
- pip

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Schools_AirQuality_MSP3
   ```

2. **Create virtual environment**
   ```bash
   conda deactivate  # if using conda
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
Schools_AirQuality_MSP3/
├── monitoring/                 # Main application
│   ├── migrations/            # Database migrations
│   ├── tests/                 # TDD test suite
│   ├── models.py              # Data models
│   ├── views.py               # View logic
│   ├── forms.py               # Form definitions
│   └── urls.py                # URL routing
├── schools_airquality_MSP3/   # Project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   └── wsgi.py                # WSGI configuration
├── static/                    # Static files (CSS, JS)
├── templates/                 # HTML templates
├── venv/                      # Virtual environment (not in git)
├── db.sqlite3                 # Database (not in git)
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Development Workflow

### Daily Development

```bash
# Navigate to project
cd /Users/GK/Documents/vscode-projects/Schools_AirQuality_MSP3

# Activate virtual environment
conda deactivate              # if (base) appears
source venv/bin/activate

# Verify correct Python
which python                  # should show venv/bin/python

# Run tests before making changes
python manage.py test

# Make changes following TDD cycle

# Run tests again
python manage.py test

# Run development server
python manage.py runserver
```

### Adding a New Feature (TDD Process)

1. **Write the test first**
   ```python
   # monitoring/tests/test_models.py
   def test_school_has_name(self):
       school = School(name="Test School")
       self.assertEqual(school.name, "Test School")
   ```

2. **Run test (should fail)**
   ```bash
   python manage.py test monitoring.tests.test_models
   ```

3. **Write minimal implementation**
   ```python
   # monitoring/models.py
   class School(models.Model):
       name = models.CharField(max_length=200)
   ```

4. **Run test (should pass)**
   ```bash
   python manage.py test monitoring.tests.test_models
   ```

5. **Commit with clear message**
   ```bash
   git add .
   git commit -m "Add test for School model name field"
   git commit -m "Implement School model with name field"
   ```

## Testing Documentation

### Why TDD for This Project?

- **Data Accuracy:** Air quality calculations must be precise and reliable
- **Safety:** Tests prevent regressions when adding features
- **Documentation:** Tests demonstrate how models and views should behave
- **Confidence:** Comprehensive tests ensure data integrity
- **Learning:** Demonstrates professional development practices

### Test Examples

See `monitoring/tests/` for examples of:
- Model validation tests
- Calculation accuracy tests
- View response tests
- Form validation tests
- Database query tests

## Features (Planned)

- [ ] School registration and management
- [ ] Air quality data entry
- [ ] Average pollution calculations
- [ ] Data visualization (charts/graphs)
- [ ] Historical data comparison
- [ ] Export data to CSV
- [ ] User authentication
- [ ] Admin dashboard

## Contributing

This is a student project following TDD methodology. All contributions must include tests.

## License

Educational project - [Add license if required]

## Author

GK - Code Institute MSP3 Project

## Acknowledgments

- Code Institute for project requirements
- Django documentation and community
- TDD methodology resources

---

**Note to Assessors:** This project demonstrates TDD principles throughout. Please review:
1. Git commit history showing test-first development
2. Test coverage in `monitoring/tests/`
3. Test output: `python manage.py test monitoring --verbosity=2`