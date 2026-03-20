# Quick Start Guide - 5 Minutes to Working System

## 🚀 Get Started in 5 Minutes

### Step 1: Run the App
```bash
python app.py
```
✅ Open http://127.0.0.1:5000

### Step 2: Admin Login
- Username: `admin`
- Password: `admin123`
- Click button → Campus Selection

### Step 3: Click "Configure On-Campus"
Fill in:
- College Name: `My College`
- Classrooms: `10`
- Seats per Classroom: `50`
- Click "Save & Continue"

### Step 4: Upload Students
- Option A: Drag & drop `sample_students.csv`
- Option B: Click and select file
- Click "Upload & Continue"

### Step 5: View Results
- **Table View**: See all allocations with search
- **Grid View**: See visual seating layout
- **Export**: Download as Excel

## 📋 File Format (if creating your own)

**Excel or CSV with 3 columns:**

| Register Number | Candidate Name | Department |
|---|---|---|
| 21CS001 | Student Name | CS |
| 21IT002 | Another Name | IT |

**That's it! 🎉**

---

## 🎯 Key Features

| Feature | Where | How to Use |
|---|---|---|
| 🔍 Search | Table View | Type register number, click Search |
| 📊 Statistics | Top of page | See total students & capacity |
| 🎨 Color Grid | Grid View | Click "Grid View" button |
| 📥 Export | Top of page | Click "Export" to download Excel |
| 🏠 Home | Any page | Click browser back to go to menu |

---

## ❌ Troubleshooting

| Problem | Solution |
|---|---|
| Port 5000 in use | Close other Flask apps or change port in app.py line 37 |
| Import error | Run `pip install -r requirements.txt` |
| File not upload | Check column names: Register Number, Candidate Name, Department |
| No data showing | Check that CSV/Excel has actual data rows |

---

## 🧪 Test Data

Pre-made: `sample_students.csv` (60 students, 6 departments) ✓ Ready to use!

---

## 📱 Access Points

| View | URL |
|---|---|
| Home | http://127.0.0.1:5000/ |
| Configuration | http://127.0.0.1:5000/oncampus-config |
| Upload | http://127.0.0.1:5000/candidate-upload |
| Seating | http://127.0.0.1:5000/view-seating |
| Grid | http://127.0.0.1:5000/classroom-grid |

---

**Need help? See README.md for full documentation**
