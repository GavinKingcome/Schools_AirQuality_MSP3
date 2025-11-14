# User Stories

## Epic 1: School Management

### US-1: Register School with Location
**As a** school administrator  
**I want to** register my school with its name and location  
**So that** I can start tracking air quality data for my school

**Acceptance Criteria:**
- School must have a name
- School must have a location address
- School must have latitude/longitude coordinates for mapping
- School information is displayed correctly

**Tasks:**
- [x] Create School model with name field
- [x] Add location field to School model
- [x] Add latitude and longitude fields
- [x] Test school creation with all fields
- [x] Configure Django admin for school management

**Status:** ✅ COMPLETE

---

## Epic 2: Air Quality Data Management

### US-4: Store Air Quality Readings
**As a** system  
**I want to** store air quality measurements for each school  
**So that** I can track pollution levels over time (current and historical data)

**Acceptance Criteria:**
- System stores pollution readings for PM10 and NO2
- Each reading is linked to a specific school
- Each reading has a timestamp of when it was measured
- System can store unlimited historical readings
- Multiple pollutant types are supported independently

**Tasks:**
- [x] Create AirQualityReading model
- [x] Link readings to schools (ForeignKey relationship)
- [x] Add pollutant type field (PM10, NO2, etc.)
- [x] Add value field for pollution measurement
- [x] Add measured_at timestamp field
- [x] Test reading creation and storage
- [x] Configure Django admin for reading management

**Status:** ✅ COMPLETE

---

### US-7: View Pollution Statistics
**As a** parent or school administrator  
**I want to** view pollution statistics for my school  
**So that** I can understand current and historical air quality levels

**Acceptance Criteria:**
- Display latest (most recent) pollution reading
- Calculate and display average pollution over time
- Identify and display peak (highest) pollution reading
- Show when peak pollution occurred
- Support multiple pollutant types (PM10, NO2)
- Statistics update automatically when new data is added

**Tasks:**
- [x] Implement `get_latest_reading()` method
- [x] Implement `get_average_reading()` method
- [x] Implement `get_peak_reading()` method
- [x] Implement `get_peak_reading_detail()` method
- [x] Implement `get_top_readings()` method
- [x] Test all statistical methods with TDD
- [x] Test edge cases (no data, multiple pollutants)

**Status:** ✅ COMPLETE

---

## Epic 3: Real-Time Data Collection

### US-5: Fetch Real-Time Air Quality Data from API
**As a** system administrator  
**I want to** automatically fetch real-time air quality data from OpenAQ API  
**So that** schools have up-to-date pollution readings without manual entry

**Acceptance Criteria:**
- System connects to OpenAQ API successfully
- Data is fetched for schools in the database
- PM10 and NO2 readings are stored correctly
- Readings include timestamp
- Failed API calls are handled gracefully
- Duplicate readings are not stored
- Only fresh data (within 7 days) is displayed

**Tasks:**
- [x] Research OpenAQ API endpoints
- [x] Implement API connection with requests library
- [x] Parse JSON response from OpenAQ
- [x] Store PM10 and NO2 readings in database
- [x] Handle API errors and timeouts
- [x] Add rate limiting (1-second delay between requests)
- [x] Filter stale data (7-day freshness check)
- [x] Test API integration manually

**Status:** ✅ COMPLETE

---

## Epic 4: Interactive Map Visualization

### US-2: View Schools on Interactive Map
**As a** parent  
**I want to** see all early years schools on an interactive map  
**So that** I can find schools near me and see their air quality levels

**Acceptance Criteria:**
- Map displays all registered schools
- Each school marker shows school name
- Clicking a marker shows current pollution level (PM10 and NO2)
- Map is centered on London/Camberwell area
- Map uses OpenStreetMap tiles
- Markers are color-coded by air quality (Good/Moderate/Poor/Very Poor)
- Map is responsive on mobile devices

**Tasks:**
- [x] Integrate Leaflet.js map library
- [x] Create map view in Django
- [x] Add school markers using latitude/longitude
- [x] Create popup windows with school data
- [x] Style map markers based on pollution levels
- [x] Implement color coding (green/orange/red)
- [x] Add combined PM10 and NO2 air quality index
- [x] Make map responsive for mobile/tablet

**Status:** ✅ COMPLETE

---

## Epic 5: User Interface & Search

### US-6: Search for Schools
**As a** parent  
**I want to** search for schools by name  
**So that** I can quickly find air quality information for a specific school

**Acceptance Criteria:**
- Search box is visible on the map
- Autocomplete dropdown shows matching schools as I type
- Selecting a school zooms to its location
- Search works on both school name and address
- Search is responsive on mobile devices

**Tasks:**
- [x] Add search input box to map template
- [x] Implement autocomplete with HTML5 datalist
- [x] Add JavaScript search functionality
- [x] Highlight matching schools while typing
- [x] Zoom to selected school on exact match
- [x] Test search on mobile devices

**Status:** ✅ COMPLETE

---

## Epic 6: Data Visualization & UI Polish

### US-8: Display Air Quality with Clear Visual Indicators
**As a** parent or school administrator  
**I want to** see clear visual indicators of air quality levels  
**So that** I can quickly understand if pollution is safe or concerning

**Acceptance Criteria:**
- Markers use high-contrast colors visible on map
- Color coding follows UK Air Quality Index standards
- Popups show both overall air quality and individual pollutants
- Individual pollutants (PM10 and NO2) have their own status
- Design is clean and professional
- Mobile-friendly interface

**Tasks:**
- [x] Implement UK Air Quality Index color scheme
- [x] Use high-contrast colors (dark green, orange, red)
- [x] Create styled popups with color-coded headers
- [x] Show individual pollutant status in popups
- [x] Add responsive header with project title
- [x] Position UI elements to avoid overlap
- [x] Test on multiple screen sizes

**Status:** ✅ COMPLETE

---

## Test Coverage Summary

| User Story | Tests Written | Status |
|------------|---------------|--------|
| US-1: Register School | 5 tests | ✅ Complete |
| US-4: Store Readings | 7 tests | ✅ Complete |
| US-7: View Statistics | 8 tests | ✅ Complete |
| US-5: API Integration | Manual testing | ✅ Complete |
| US-2: Map Visualization | Manual testing | ✅ Complete |
| US-6: Search Functionality | Manual testing | ✅ Complete |
| US-8: Visual Indicators | Manual testing | ✅ Complete |

**Total Automated Tests:** 20 passing ✅  
**Manual Testing:** All features tested and verified ✅

---

## Development Methodology

This project follows **Test-Driven Development (TDD)** for backend models:

1. ✅ Write User Story with acceptance criteria
2. ✅ Write failing tests first (RED phase)
3. ✅ Write code to make tests pass (GREEN phase)
4. ✅ Refactor and improve (REFACTOR phase)
5. ✅ Commit with User Story reference

**Backend features** (models, database) have comprehensive automated tests.  
**Frontend features** (map, search, UI) have been thoroughly manually tested.

---

## Completed Features (MSP3 v1.0)

✅ **6 Schools Registered** - Camberwell/Peckham area  
✅ **Real-time API Integration** - OpenAQ data fetching  
✅ **Interactive Map** - Leaflet.js with OpenStreetMap  
✅ **Color-coded Markers** - UK Air Quality Index standards  
✅ **Autocomplete Search** - Find schools quickly  
✅ **Responsive Design** - Works on desktop, tablet, mobile  
✅ **Detailed Popups** - PM10 and NO2 levels with status  
✅ **Professional UI** - Gradient header, clean styling  

---

## Future Enhancements (Post-MSP3)

⬜ **PostgreSQL Migration** - Production-ready database  
⬜ **TimescaleDB Integration** - Time-series data optimization  
⬜ **LAQN Integration** - London Air Quality Network data  
⬜ **Historical Charts** - Pollution trends over time  
⬜ **Email Alerts** - Notifications for poor air quality  
⬜ **Automated Updates** - Cron jobs for data refresh  
⬜ **Expanded Coverage** - 50+ schools across London  
⬜ **Statistical Analysis** - Weekly/monthly averages  

---

## Prototype Status

This is a **working prototype** demonstrating:
- Django/Python backend development
- RESTful API integration
- Database modeling and queries
- Interactive data visualization
- Responsive web design
- Test-Driven Development practices

**Note:** This prototype uses SQLite and manual data refresh. Future versions will migrate to PostgreSQL with automated updates.

---

*Last Updated: November 2024*