# Testing Guide - Automatic Classroom and Seat Allocation System

## Quick Test Walkthrough

Follow these steps to test the complete on-campus seat allocation workflow.

## Test Scenario Configuration

### Test Setup 1: Small Class (10 students)
- College: "Test University - Small"
- Classrooms: 2
- Seats per Classroom: 10
- Total Capacity: 20 seats

**Test File**: Create a CSV with 10 students
```csv
Register Number,Candidate Name,Department
TEST001,Student One,CS
TEST002,Student Two,IT
TEST003,Student Three,EC
TEST004,Student Four,ME
TEST005,Student Five,CE
TEST006,Student Six,EE
TEST007,Student Seven,CS
TEST008,Student Eight,IT
TEST009,Student Nine,EC
TEST010,Student Ten,ME
```

### Test Setup 2: Large Class (100 students)
- College: "Test University - Large"
- Classrooms: 5
- Seats per Classroom: 25
- Total Capacity: 125 seats

Use `sample_students.csv` (contains 60 records).

### Test Setup 3: Full Capacity Test
- College: "Test University - Full"
- Classrooms: 10
- Seats per Classroom: 50
- Total Capacity: 500 seats

## Step-by-Step Testing

### Phase 1: Authentication (5 min)

#### Test 1.1: Admin Login
1. Open http://127.0.0.1:5000/
2. Click "Admin Login"
3. Enter: admin / admin123
4. **Expected**: Redirect to Campus Selection Dashboard
5. **Verify**: Page title shows "Campus Selection Dashboard"

#### Test 1.2: Valid/Invalid Login Attempts
1. Try wrong password
2. **Expected**: Error message "Invalid username or password!"
3. Try empty fields
4. **Expected**: Error message
5. Try correct credentials again
6. **Expected**: Successful login

---

### Phase 2: Configuration (10 min)

#### Test 2.1: On-Campus Configuration
1. Click "Configure On-Campus"
2. **Expected**: Redirect to ON-CAMPUS CONFIGURATION page
3. **Verify**: Step indicator shows "1" and title shows "Exam Configuration"

#### Test 2.2: Form Validation
1. Leave all fields empty, click "Save & Continue"
2. **Expected**: Error message displays
3. Enter College Name: "Test College"
4. Leave Classrooms empty
5. **Expected**: Error message
6. Enter negative number for Classrooms
7. **Expected**: Validation error or warning

#### Test 2.3: Valid Configuration
1. Enter:
   - College Name: "Test Model College"
   - Number of Classrooms: 10
   - Seats per Classroom: 50
2. Click "Save & Continue"
3. **Expected**: Success message "Configuration saved!"
4. **Verify**: Redirect to Upload Candidates page
5. **Verify**: Step indicator shows "2"
6. **Verify**: Config summary shows: "College: Test Model College"

---

### Phase 3: File Upload (15 min)

#### Test 3.1: Drag-and-Drop Upload
1. On Upload page, prepare a test CSV file
2. Drag CSV file to the drop area
3. **Expected**: File preview shows
4. Click "Upload & Continue"
5. **Expected**: Success message with record count

#### Test 3.2: File Browser Upload
1. Click on the drop area
2. **Expected**: File dialog opens
3. Select a CSV/Excel file
4. **Expected**: File name displayed
5. Click "Upload & Continue"
6. **Expected**: Processing animation, then success message

#### Test 3.3: File Validation - Wrong Format
1. Try uploading a PDF, DOC, or TXT file
2. **Expected**: Error message "Invalid file type"
3. **Verify**: Error shows allowed formats

#### Test 3.4: File Validation - Missing Columns
1. Create CSV with wrong headers:
   ```csv
   ID,Name,Dept
   ```
2. Upload
3. **Expected**: Error message showing missing columns
4. **Example**: "Missing columns: Register Number, Candidate Name"

#### Test 3.5: File Validation - Duplicate Records
1. Create CSV with duplicate register numbers:
   ```csv
   Register Number,Candidate Name,Department
   21CS001,Student A,CS
   21CS001,Student B,CS
   ```
2. Upload
3. **Expected**: System removes duplicates
4. **Verify**: Message shows correct count of valid records

#### Test 3.6: File Validation - Missing Values
1. Create CSV with empty cells:
   ```csv
   Register Number,Candidate Name,Department
   21CS001,Student A,CS
   21CS002,,IT
   ,Student C,EC
   ```
2. Upload
3. **Expected**: Rows with missing values removed
4. **Verify**: Only valid records counted (1 valid, 2 removed)

#### Test 3.7: Large File Upload (Performance Test)
1. Create CSV with 500+ records
2. Upload
3. **Expected**: Processes within 5 seconds
4. **Verify**: Success message with full count
5. **Verify**: No timeout errors

---

### Phase 4: Seat Allocation (5 min)

#### Test 4.1: Automatic Allocation
1. After successful upload, system auto-redirects or shows allocation summary
2. **Expected**: Seat allocation completes
3. **Verify**: Success message shows allocation count
4. **Example**: "Automatic seat allocation completed for 60 students!"

#### Test 4.2: Allocation Logic Verification
1. Navigate to /view-seating
2. **Expected**: Seating table displays
3. **Verify**: Each student has:
   - Register Number
   - Candidate Name
   - Department
   - Room Number (1 to N)
   - Seat Number (1 to seats_per_classroom)
4. **Check**: No duplicate register numbers
5. **Check**: Seat numbers don't exceed classroom capacity

#### Test 4.3: Allocation Formula
1. For each student, verify:
   - Total capacity = 10 classrooms × 50 seats = 500
   - Student #1: Room = (0 ÷ 50) + 1 = 1, Seat = (0 mod 50) + 1 = 1
   - Student #50: Room = (49 ÷ 50) + 1 = 1, Seat = (49 mod 50) + 1 = 50
   - Student #51: Room = (50 ÷ 50) + 1 = 2, Seat = (50 mod 50) + 1 = 1
2. **Verify**: Room transitions occur at correct points

---

### Phase 5: Viewing Results (20 min)

#### Test 5.1: Seating Table View
1. Navigate to /view-seating
2. **Expected**: Professional Bootstrap table displays
3. **Verify**: Columns: Register Number, Name, Department, Room, Seat
4. **Verify**: All rows display correctly
5. **Verify**: Table is sortable/scrollable

#### Test 5.2: Statistics Display
1. Verify stat boxes show:
   - Total Students Allocated
   - Total Classrooms
   - Seats per Classroom
   - Total Capacity
2. **Expected**: Numbers match configuration

#### Test 5.3: Search Functionality
1. Enter a valid register number in search box
2. Click "Search"
3. **Expected**: Table filters to show only that student
4. Search for non-existent register number
5. **Expected**: "No results found" message
6. Try search with partial number
7. **Expected**: No matches (exact match only)
8. Click "Clear Search"
9. **Expected**: All records display again

#### Test 5.4: Search Case Insensitivity
1. Search for student number in different cases
2. **Expected**: Should find student regardless of case
3. **Example**: "21cs001" should find "21CS001"

#### Test 5.5: Grid View Navigation
1. From seating table, click "Grid View" button
2. **Expected**: Redirect to classroom grid page
3. **Verify**: Step indicator shows "5"

---

### Phase 6: Classroom Grid Visualization (15 min)

#### Test 6.1: Grid Layout Display
1. On Classroom Grid page
2. **Expected**: Visual grid showing all classrooms
3. **Verify**: Each classroom section displays:
   - Room number header
   - Room statistics (students, empty seats, departments)
   - Seat grid layout

#### Test 6.2: Color-Coded Departments
1. Examine seat colors
2. **Verify**: Different departments have different colors:
   - CS = Red
   - IT = Teal
   - EC = Blue
   - ME = Light Salmon
   - CE = Mint Green
   - EE = Yellow
3. **Verify**: Legend displays all colors and their meanings

#### Test 6.3: Seat Information
1. Hover over specific seats
2. **Expected**: Tooltip shows:
   - Register number
   - Student name
   - Department
3. Click "Table View" from grid
4. **Expected**: Return to table view

#### Test 6.4: Empty Seats
1. If configuration has more seats than students
2. **Expected**: Empty seats shown in gray
3. **Verify**: Empty seat count matches statistics
4. Example: If 500 seats, 60 students → 440 empty seats

#### Test 6.5: Room Statistics
1. Verify each room shows:
   - Number of students
   - Number of empty seats
   - Number of departments represented
2. **Formula Check**: 
   - Students + Empty Seats = Seats per Classroom
3. Calculate across all rooms:
   - Total students should match configuration

#### Test 6.6: Department Distribution
1. Count students by department across all rooms
2. **Verify**: Departments distributed fairly across rooms
3. **Note**: Exact distribution depends on randomization

---

### Phase 7: Export Functionality (5 min)

#### Test 7.1: Excel Export
1. From seating table, click "Export" button
2. **Expected**: Excel file downloads
3. Open downloaded file
4. **Verify**: Columns match table display
5. **Verify**: Data matches displayed records
6. **Verify**: Formatting is clean and readable

#### Test 7.2: Export File Naming
1. Check downloaded file name
2. **Expected**: Format: `seating_arrangement_YYYYMMDD_HHMMSS.xlsx`
3. Example: `seating_arrangement_20260318_150530.xlsx`

#### Test 7.3: Excel Content Validation
1. Open exported Excel file
2. Verify:
   - Column headers present
   - Data properly aligned
   - No formula errors
   - File is readable and valid

---

## Edge Case Testing

### Test E.1: Exact Capacity Match
- Configuration: 5 classrooms, 10 seats each = 50 total
- Upload: Exactly 50 students
- **Expected**: All seats filled, 0 empty seats

### Test E.2: One Student
- Configuration: 2 classrooms, 10 seats each
- Upload: 1 student
- **Expected**: 
  - Student allocated to Room 1, Seat 1
  - Rest are empty

### Test E.3: Department With One Member
- Upload 10 students with 2 from CS, 3 from IT, 5 from EC
- **Expected**: All departments allocated across rooms

### Test E.4: Overflow Test
- Capacity: 100 seats
- Attempt upload: 150 students
- **Expected**: Error message "Not enough seats"

---

## Performance Testing

### Test P.1: 100 Students
1. Upload file with 100 students
2. Measure processing time
3. **Expected**: < 2 seconds

### Test P.2: 500 Students
1. Upload file with 500 students
2. Measure processing time
3. **Expected**: < 5 seconds

### Test P.3: 1000+ Students
1. Prepare Excel with 1000+ records
2. Upload
3. **Expected**: Processes efficiently
4. **Expected**: Grid view renders
5. **Expected**: Search functionality responsive

### Test P.4: Grid Rendering
1. With 1000 students across 20 rooms
2. Load grid view
3. **Expected**: Page renders within 3 seconds
4. **Expected**: Smooth scrolling
5. **Expected**: No browser lag

---

## Browser Compatibility Testing

Test on:
- ✅ Chrome/Edge (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)
- ✅ Mobile browsers (Responsive design)

---

## Error Recovery Testing

### Test R.1: Session Timeout
1. Leave page idle for extended period
2. Refresh page
3. **Expected**: Session preserved or user redirected to login

### Test R.2: Browser Back Button
1. Navigate through flow
2. Click back button multiple times
3. **Expected**: Navigation works correctly

### Test R.3: Page Refresh
1. At any step, refresh the page
2. **Expected**: Data preserved or graceful error
3. **Verify**: No data loss

---

## Checklist for Deployment

- [ ] All 7 phases tested successfully
- [ ] No JavaScript console errors
- [ ] Responsive design tested on mobile
- [ ] Export functionality working
- [ ] Search functionality working
- [ ] Grid visualization renders correctly
- [ ] All error messages appear correctly
- [ ] Performance acceptable for 1000+ students
- [ ] Database/file permissions set correctly
- [ ] Uploads folder has write permissions
- [ ] All templates rendering correctly
- [ ] Static files loading (CSS, JS)
- [ ] Flash messages displaying properly
- [ ] Redirect chains working
- [ ] Session storage working

---

## Test Results Template

```
Test Date: _______________
Tester: ___________________
Version: ___________________

Phase 1 - Authentication: ✅ ❌ ⚠️
Phase 2 - Configuration: ✅ ❌ ⚠️
Phase 3 - Upload: ✅ ❌ ⚠️
Phase 4 - Allocation: ✅ ❌ ⚠️
Phase 5 - Results View: ✅ ❌ ⚠️
Phase 6 - Grid View: ✅ ❌ ⚠️
Phase 7 - Export: ✅ ❌ ⚠️

Issues Found:
1. ___________________________
2. ___________________________
3. ___________________________

Notes:
_________________________________
_________________________________
```

---

For detailed API endpoint testing, see [API_TESTING.md](API_TESTING.md)
