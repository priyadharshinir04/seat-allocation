# Automatic Classroom and Seat Allocation System

A complete full-stack solution for managing on-campus and off-campus seat allocation for examinations using Flask, Pandas, Bootstrap, and JavaScript.

## 📋 Features

### Core Features
✅ **On-Campus Configuration** - Configure exam details with college name, classrooms, and seat capacity
✅ **Candidate Upload System** - Upload student data from Excel (.xlsx) or CSV files
✅ **Automatic Seat Allocation** - Smart algorithm for optimal seat distribution
✅ **Seating Display** - View allocated seats in table format with search functionality
✅ **Classroom Grid Visualization** - Visual representation of seating arrangement by room
✅ **Department Color Coding** - Different colors for different departments
✅ **Export to Excel** - Download seating arrangement as Excel file
✅ **High Performance** - Supports 1000+ students efficiently using Pandas

### Bonus Features
- 🔍 Search students by register number
- 📊 Statistical dashboard with allocation summary
- 🎨 Beautiful responsive UI with Bootstrap
- 💾 Session-based data storage
- 🛡️ Input validation and error handling

## 🏗️ Project Structure

```
seat allotment/
├── app.py                              # Flask application main file
├── requirements.txt                    # Python dependencies
├── sample_students.csv                 # Sample dataset for testing
├── uploads/                            # Directory for uploaded files
├── static/
│   ├── css/
│   │   └── styles.css                 # Main stylesheet
│   ├── js/                            # JavaScript files
│   └── img/                           # Images directory
└── templates/
    ├── index.html                     # Landing page
    ├── admin-login.html               # Admin login page
    ├── campus-selection.html          # Campus type selection
    ├── oncampus_config.html           # On-campus configuration page
    ├── upload.html                    # Candidate upload page
    ├── seating.html                   # Seating allocation results
    ├── classroom.html                 # Classroom grid visualization
    ├── oncampus_dashboard.html        # On-campus dashboard
    ├── offcampus_dashboard.html       # Off-campus dashboard
    └── student-allotment.html         # Student login page
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### Installation

1. **Clone or extract the project**
   ```bash
   cd "C:\Users\Priyadharshini\OneDrive\Documents\Desktop\seat allotment"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
python app.py
```

The application will start at: **http://127.0.0.1:5000**

## 📖 Usage Guide

### Step 1: Admin Login
- Navigate to the landing page
- Click "Admin Login"
- Default credentials:
  - Username: `admin`
  - Password: `admin123`

### Step 2: Select Campus Type
- On the "Campus Selection Dashboard"
- Click "Configure On-Campus" for on-campus events

### Step 3: Configure Exam Details (Step 1)
- **College Name**: Enter your institution name
- **Number of Classrooms**: Total number of examination halls
- **Seats per Classroom**: Student capacity per room
- Click "Save & Continue"

### Step 4: Upload Candidate Data (Step 2)
- Prepare your Excel/CSV file with columns:
  - `Register Number` - Student ID (required)
  - `Candidate Name` - Student name (required)
  - `Department` - Department code (required)
- Upload file via drag-and-drop or file browser
- System validates and removes duplicates automatically
- Click "Upload & Continue"

### Step 5: Automatic Seat Allocation (Step 3)
- System automatically shuffles students
- Allocates seats using formula:
  - Room Number = (Index ÷ Seats per Room) + 1
  - Seat Number = (Index mod Seats per Room) + 1
- Departments distributed randomly to prevent cheating

### Step 6: View Seating Results (Step 4)
- **Table View**: Detailed allocation with search capability
- **Statistics**: Total students, classrooms, capacity
- **Search**: Find students by register number
- **Export**: Download allocation as Excel file

### Step 7: Classroom Grid Visualization (Step 5)
- **Visual Layout**: See seats arranged by room
- **Color Coding**: Different colors for different departments
- **Department Legend**: Reference for color meanings
- **Room Statistics**: Students per room, empty seats

## 📊 Data Format

### Excel/CSV Template
| Register Number | Candidate Name | Department |
|---|---|---|
| 21CS001 | Aarav Kumar | CS |
| 21IT002 | Bhavana Singh | IT |
| 21EC003 | Chetan Sharma | EC |

**Column Requirements:**
- No empty cells in any required column
- Register Number must be unique
- Department code can be 2-4 characters
- All columns must be present in the file

## 🔧 Configuration

### Supported File Formats
- Excel: `.xlsx`, `.xls`
- CSV: `.csv`

### Seat Allocation Algorithm
```python
# For each student in shuffled list:
room_number = (index // seats_per_classroom) + 1
seat_number = (index % seats_per_classroom) + 1
```

### Department Color Assignments
- **CS/CSE**: Red (#FF6B6B)
- **IT/ISE**: Teal (#4ECDC4)
- **EC/ECE**: Blue (#45B7D1)
- **ME**: Light Salmon (#FFA07A)
- **CE/CV**: Mint Green (#98D8C8)
- **EE/EEE**: Yellow (#F7DC6F)
- **Other**: Gray (#BDC3C7)

## 🧪 Testing with Sample Data

A sample dataset is included: `sample_students.csv`

1. Login as admin (admin/admin123)
2. Select "Configure On-Campus"
3. Enter configuration:
   - College Name: Test College
   - Classrooms: 10
   - Seats per Classroom: 50
4. Upload `sample_students.csv`
5. View the seating arrangement

**Sample dataset includes 60 students from 6 departments.**

## 🔒 Authentication

### Admin Login
- Default Username: `admin`
- Default Password: `admin123`
- **Note**: Change credentials in production

### Student Login
- Register Number: Any valid register number from uploaded data
- Date of Birth: Any valid date (for testing)

## 📱 Responsive Design

The application is fully responsive:
- **Desktop**: Full layout with grid views
- **Tablet**: Optimized grid layout
- **Mobile**: Stacked layout for mobile screens

## ⚡ Performance

- **Handles 1000+ students**: Optimized using Pandas
- **Fast processing**: Vectorized operations for data cleaning
- **Efficient search**: O(n) complexity for student search
- **Minimum dependencies**: Only essential packages

## 🛠️ Dependencies

```
Flask==2.3.3           # Web framework
pandas==2.0.3          # Data processing
openpyxl==3.1.2        # Excel file handling
Werkzeug==2.3.7        # WSGI utilities
```

## 📝 API Endpoints

### Configuration Routes
- `GET /oncampus-config` - Configuration form page
- `POST /oncampus-config` - Save configuration
- `GET /candidate-upload` - Upload form page
- `POST /candidate-upload` - Process upload

### Allocation Routes
- `GET /allocate-seats` - Perform seat allocation
- `GET /view-seating` - View allocation results
- `GET /classroom-grid` - Classroom visualization
- `GET /search-student-api` - API for student search

### Export Routes
- `GET /export-seating` - Export to Excel

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pandas'"
**Solution**: Run `pip install pandas`

### Issue: "File not found" error on upload
**Solution**: Ensure file has correct column headers

### Issue: Port 5000 already in use
**Solution**: 
```bash
# Change port in app.py:
app.run(debug=True, port=5001)
```

### Issue: Session data not persisting
**Solution**: Ensure cookies are enabled in browser, clear browser cache

## 📈 Future Enhancements

- Database integration (SQLite/PostgreSQL)
- Student login to view their allocation
- Seat blocking for special needs students
- Real-time allocation updates
- Mobile app for seat verification
- Email notifications to students
- Collision detection for conflicting allocations
- Admin dashboard with analytics

## 📄 Sample Output

### Seating Table
```
Register Number | Name              | Department | Room | Seat
21CS001        | Aarav Kumar       | CS         | 1    | 1
21IT002        | Bhavana Singh     | IT         | 1    | 2
21EC003        | Chetan Sharma     | EC         | 1    | 3
```

### Classroom Grid (Room 1)
```
[21CS001]  [21IT002]  [21EC003]
  CS        IT         EC

[21ME001]  [21CE002]  [21EE003]
  ME        CE         EE
```

## 💡 Key Features Explained

### Smart Shuffling
Students are randomly shuffled before allocation to ensure fairness and prevent organized cheating patterns.

### Department Distribution
The algorithm naturally distributes students across rooms proportionally to department sizes.

### Efficient Allocation
Linear-time complexity ensures quick processing even for thousands of students.

### Validation
- Duplicate register numbers are removed
- Missing data is filtered out
- File format is validated
- Capacity limits are checked

## 🔐 Security Considerations

⚠️ **Development Mode Only**
Current implementation is for development/testing purposes.

### For Production:
- Implement proper authentication (JWT/OAuth)
- Use database instead of sessions
- Add role-based access control
- Encrypt sensitive data
- Implement rate limiting
- Add CSRF protection
- Use HTTPS only
- Sanitize all inputs

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Verify file format matches requirements
3. Ensure all dependencies are installed
4. Check browser console for errors

## 📄 License

This project is part of the College Seating System initiative.

---

**Last Updated**: March 18, 2026
**Version**: 1.0.0
#   s e a t - a l l o c a t i o n  
 