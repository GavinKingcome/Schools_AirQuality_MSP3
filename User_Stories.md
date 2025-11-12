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
- System stores pollution readings for PM2.5 and NO2
- Each reading is linked to a specific school
- Each reading has a timestamp of when it was measured
- System can store unlimited historical readings
- Multiple pollutant types are supported independently

**Tasks:**
- [x] Create AirQualityReading model
- [x] Link readings to schools (ForeignKey relationship)
- [x] Add pollutant type field (PM2.5, NO2, etc.)
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
- Support multiple pollutant types (PM2.5, NO2)
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

## Epic 3: Real-Time Data Collection (PLANNED)

### US-5: Fetch Real-Time Air Quality Data from API
**As a** system administrator  
**I want to** automatically fetch real-time air quality data from OpenAQ API  
**So that** schools have up-to-date pollution readings without manual entry

**Acceptance Criteria:**
- System connects to OpenAQ API successfully
- Data is fetched for schools in the database
- PM2.5 and NO2 readings are stored correctly
- Readings include timestamp
- Failed API calls are handled gracefully
- Duplicate readings are not stored

**Tasks:**
- [ ] Research OpenAQ API endpoints
- [ ] Write tests for API connection (TDD)
- [ ] Write tests for data parsing
- [ ] Write tests for data storage
- [ ] Create Django management command
- [ ] Implement API integration
- [ ] Handle API errors and timeouts
- [ ] Add logging for monitoring

**Status:** 🔜 NEXT

---

## Epic 4: Interactive Map Visualization (PLANNED)

### US-2: View Schools on Interactive Map
**As a** parent  
**I want to** see all early years schools on an interactive map  
**So that** I can find schools near me and see their air quality levels

**Acceptance Criteria:**
- Map displays all registered schools
- Each school marker shows school name
- Clicking a marker shows current pollution level
- Map is centered on user's location (if available)
- Map uses OpenStreetMap

**Tasks:**
- [ ] Integrate Leaflet.js map library
- [ ] Create map view in Django
- [ ] Add school markers using latitude/longitude
- [ ] Create popup windows with school data
- [ ] Style map markers based on pollution levels

**Status:** 📋 PLANNED

---

## Test Coverage Summary

| User Story | Tests Written | Status |
|------------|---------------|--------|
| US-1: Register School | 5 tests | ✅ Complete |
| US-4: Store Readings | 7 tests | ✅ Complete |
| US-7: View Statistics | 8 tests | ✅ Complete |
| US-5: API Integration | 0 tests | 🔜 Next |
| US-2: Map Visualization | 0 tests | 📋 Planned |

**Total Tests:** 20 passing ✅

---

## Development Methodology

This project follows **Test-Driven Development (TDD)**:

1. ✅ Write User Story with acceptance criteria
2. ✅ Write failing tests first (RED phase)
3. ✅ Write code to make tests pass (GREEN phase)
4. ✅ Refactor and improve (REFACTOR phase)
5. ✅ Commit with User Story reference

All completed features have comprehensive automated tests.