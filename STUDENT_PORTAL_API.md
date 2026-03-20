# 🔌 Student Portal - API Reference

## Base URL
```
http://localhost:5000
```

---

## Authentication Routes

### 1. Student Login
**Endpoint:** `POST /student-login`

**Description:** Authenticate student and create session

**Request Body:**
```json
{
  "register_number": "AIDS1001",
  "year_or_dob": "2"
}
```

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| register_number | string | ✅ | Unique student identifier (case-insensitive) |
| year_or_dob | string | ✅ | Academic year (1-4) or date of birth |

**Example cURL:**
```bash
curl -X POST http://localhost:5000/student-login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "register_number=AIDS1001&year_or_dob=2"
```

**Success Response (Redirect):**
```
HTTP/1.1 302 Found
Location: http://localhost:5000/student-dashboard
Set-Cookie: session=...; Path=/; HttpOnly
Flash Message: "Welcome John Doe!"
```

**Error Response:**
```
HTTP/1.1 200 OK
Display: Login page with error message
Flash Message: "Invalid Register Number or Year. Please try again."
```

**Session Storage:**
```python
session['student_logged_in'] = True
session['student_register_number'] = 'AIDS1001'
session['student_name'] = 'John Doe'
session['student_year'] = '2'
session.modified = True
```

---

### 2. Student Logout
**Endpoint:** `GET /student-logout`

**Description:** Clear student session and logout

**Request Parameters:** None

**Example cURL:**
```bash
curl -X GET http://localhost:5000/student-logout \
  -H "Cookie: session=..."
```

**Response:**
```
HTTP/1.1 302 Found
Location: http://localhost:5000/student-login
Set-Cookie: session=; Path=/; Expires=...
Flash Message: "You have been logged out!"
```

**Session State After:**
```python
session.clear()  # All session data removed
```

---

## Dashboard Routes

### 3. Get Student Dashboard
**Endpoint:** `GET /student-dashboard`

**Description:** Display student seating allocation details

**Authentication:** ✅ Required (`session['student_logged_in']`)

**Request Headers:**
```
Cookie: session=... (automatically included by browser)
```

**Example cURL:**
```bash
curl -X GET http://localhost:5000/student-dashboard \
  -H "Cookie: session=..."
```

**Success Response:**
```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

[HTML Dashboard Page]
Template: student-dashboard.html
```

**Variables Passed to Template:**
```python
{
  'student': {
    'register_number': 'AIDS1001',
    'candidate_name': 'John Doe',
    'department': 'AIDS',
    'year': '2',
    'room_number': 5,
    'bench_number': 10,
    'seat_position': 'Left'  # Only for internal exams
  },
  'bench_mate': {
    'register_number': 'AIDS1002',
    'candidate_name': 'Jane Smith',
    'department': 'CSE',
    'year': '2',
    'room_number': 5,
    'bench_number': 10,
    'seat_position': 'Right'
  },
  'config': {
    'college_name': 'ABC Engineering College',
    'exam_type': 'internal',
    'num_classrooms': 10,
    'seats_per_classroom': 40
  }
}
```

**Error Response (Not Logged In):**
```
HTTP/1.1 302 Found
Location: http://localhost:5000/student-login
Flash Message: "Please login first!"
```

**Error Response (Allocation Not Found):**
```
HTTP/1.1 302 Found
Location: http://localhost:5000/student-login
Flash Message: "Seating allocation not found!"
```

---

## Document Generation Routes

### 4. Download Seating Slip (PDF)
**Endpoint:** `GET /student-download-slip`

**Description:** Generate and download seating slip as PDF

**Authentication:** ✅ Required (`session['student_logged_in']`)

**Request Headers:**
```
Cookie: session=... (automatically included)
Accept: application/pdf
```

**Example cURL:**
```bash
curl -X GET http://localhost:5000/student-download-slip \
  -H "Cookie: session=..." \
  -o seating_slip_AIDS1001_20260318.pdf
```

**Success Response:**
```
HTTP/1.1 200 OK
Content-Type: application/pdf
Content-Disposition: attachment; filename="seating_slip_AIDS1001_20260318.pdf"
Content-Length: 45230

[PDF Binary Data]
```

**PDF Content Includes:**
- QR Code with data: `REG:AIDS1001|ROOM:5|BENCH:10`
- Personal Information Table
- Seating Details Table
- Important Notes Box
- Timestamp of generation
- Professional styling and branding

**Download Filename Format:**
```
seating_slip_{REGISTER_NUMBER}_{YYYYMMDD}.pdf
```

**Error Response (Not Logged In):**
```
HTTP/1.1 302 Found
Location: http://localhost:5000/student-login
```

**Error Response (Data Not Found):**
```
HTTP/1.1 302 Found
Location: http://localhost:5000/student-dashboard
Flash Message: "Seating data not found!"
```

**Error Response (PDF Generation Failed):**
```
HTTP/1.1 302 Found
Location: http://localhost:5000/student-dashboard
Flash Message: "Error generating PDF: [error_message]"
```

---

## Session Routes

### 5. Get Current Session Info (Debug Only)
**Endpoint:** `GET /debug-session` (Optional - add for testing)

**Description:** Return current session data (development only)

**Example Response:**
```json
{
  "student_logged_in": true,
  "student_register_number": "AIDS1001",
  "student_name": "John Doe",
  "student_year": "2",
  "_fresh": true,
  "_permanent": false
}
```

---

## Error Responses (Standard)

### 401 Unauthorized
```
HTTP/1.1 401 Unauthorized
Location: /student-login
```

### 404 Not Found
```
HTTP/1.1 404 Not Found
Display: Error page
```

### 500 Internal Server Error
```
HTTP/1.1 500 Internal Server Error
Flash Message: "Error: [error_details]"
```

---

## HTTP Status Codes

| Code | Meaning | When Used |
|------|---------|-----------|
| 200 | OK | Dashboard loads successfully |
| 302 | Redirect | Login success, logout, auth required |
| 400 | Bad Request | Invalid form submission |
| 401 | Unauthorized | Session not found or invalid |
| 404 | Not Found | Route does not exist |
| 500 | Server Error | PDF generation failed, etc. |

---

## Request/Response Headers

### Common Request Headers
```
GET /student-dashboard HTTP/1.1
Host: localhost:5000
Cookie: session=eyJz...
User-Agent: Mozilla/5.0...
Accept: text/html, application/xhtml+xml
```

### Common Response Headers
```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 15432
Set-Cookie: session=...; Path=/; HttpOnly; SameSite=Lax
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
```

---

## Session Validation

### Session Requirements
```javascript
// Client must have valid session cookie containing:
{
  "student_logged_in": true,
  "student_register_number": "AIDS1001",
  "student_name": "John Doe"
}

// Checked on every protected route using:
if not session.get('student_logged_in'):
    redirect to /student-login
```

### Session Timeout (Production)
```python
PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
SESSION_COOKIE_SECURE = True  # HTTPS only
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
```

---

## Data Structures

### Student Allocation Object
```python
{
    'register_number': 'AIDS1001',      # str
    'candidate_name': 'John Doe',       # str
    'department': 'AIDS',                # str
    'year': '2',                         # str (1-4)
    'room_number': 5,                    # int
    'bench_number': 10,                  # int
    'seat_position': 'Left'              # str ('Left' or 'Right', internal exams only)
}
```

### Session Object
```python
{
    'student_logged_in': True,           # bool
    'student_register_number': 'AIDS1001', # str
    'student_name': 'John Doe',          # str
    'student_year': '2',                 # str
    'exam_config': {                     # dict (from admin config)
        'college_name': 'ABC College',
        'exam_type': 'internal',
        'num_classrooms': 10,
        'seats_per_classroom': 40
    }
}
```

### Exam Config Object
```python
{
    'college_name': 'ABC Engineering College',  # str
    'exam_type': 'internal',                    # str ('internal' or 'semester')
    'num_classrooms': 10,                       # int
    'seats_per_classroom': 40,                  # int (40 internal, 20 semester)
    'total_seats': 400                          # int
}
```

---

## Rate Limiting (Recommended)

### Suggested Rate Limits (Production)
```python
@limiter.limit("5 per minute")  # Login attempts
def student_login():
    ...

@limiter.limit("30 per minute")  # PDF downloads
def student_download_slip():
    ...
```

---

## Security Headers (Recommended)

### Add to Flask Response
```python
@app.after_request
def set_security_headers(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000'
    return response
```

---

## Testing with Postman

### 1. Login Test
```
POST http://localhost:5000/student-login
Headers: Content-Type: application/x-www-form-urlencoded
Body: register_number=AIDS1001&year_or_dob=2
Expect: 302 redirect to /student-dashboard
```

### 2. Dashboard Test
```
GET http://localhost:5000/student-dashboard
Headers: Cookie: session=... (from login response)
Expect: 200 with HTML dashboard
```

### 3. PDF Download Test
```
GET http://localhost:5000/student-download-slip
Headers: Cookie: session=... (from login response)
Expect: 200 with PDF attachment
```

### 4. Logout Test
```
GET http://localhost:5000/student-logout
Headers: Cookie: session=... (from login response)
Expect: 302 redirect to /student-login
```

---

## API Client Example (Python)

```python
import requests
from requests.adapters import HTTPAdapter

# Create session
session = requests.Session()
adapter = HTTPAdapter(max_retries=3)
session.mount('http://', adapter)

# Login
response = session.post(
    'http://localhost:5000/student-login',
    data={
        'register_number': 'AIDS1001',
        'year_or_dob': '2'
    }
)

# Get dashboard
if response.status_code == 302:
    response = session.get(
        'http://localhost:5000/student-dashboard',
        allow_redirects=True
    )
    print(response.text)  # HTML content

# Download PDF
response = session.get(
    'http://localhost:5000/student-download-slip'
)
if response.status_code == 200:
    with open('seating_slip.pdf', 'wb') as f:
        f.write(response.content)

# Logout
session.get('http://localhost:5000/student-logout')
```

---

## API Client Example (JavaScript/Fetch)

```javascript
// Login
const loginResponse = await fetch(
  'http://localhost:5000/student-login',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    credentials: 'include',
    body: new URLSearchParams({
      register_number: 'AIDS1001',
      year_or_dob: '2'
    })
  }
);

// Get Dashboard
const dashboardResponse = await fetch(
  'http://localhost:5000/student-dashboard',
  { credentials: 'include' }
);
const html = await dashboardResponse.text();
console.log(html);

// Download PDF
const pdfResponse = await fetch(
  'http://localhost:5000/student-download-slip',
  { credentials: 'include' }
);
const blob = await pdfResponse.blob();
const url = window.URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = 'seating_slip.pdf';
a.click();
```

---

## Webhook Events (Future Enhancement)

```python
# Recommended webhooks for future implementation:
WEBHOOKS = {
    'student.login': 'Triggered when student logs in',
    'student.view_allocation': 'Triggered when dashboard accessed',
    'student.download_slip': 'Triggered when PDF downloaded',
    'student.logout': 'Triggered when student logs out'
}
```

---

## Query Parameters (Future Enhancement)

```
/student-dashboard?ref=email  # Track source of traffic
/student-login?redirect=...   # Custom redirect URL
/student-download-slip?format=pdf&include_qr=true  # Options
```

---

**Last Updated:** March 18, 2026
**API Version:** 1.0.0
**Status:** ✅ Complete
