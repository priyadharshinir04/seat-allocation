# 🎓 Student Portal - Quick Start Guide

## 📦 Installation & Setup

### Step 1: Install Dependencies
```bash
pip install qrcode[pil]
pip install reportlab
```

### Step 2: Verify Installation
```bash
python -c "import app; print('✓ Flask app ready')"
```

### Step 3: Start Flask Server
```bash
python app.py
```

Server will run on: **http://localhost:5000**

---

## 🚀 First-Time Setup

### For Admin: Create Student Allocations
1. Go to **http://localhost:5000**
2. Click **Admin Login**
3. Login with: `admin` / `admin123`
4. Navigate to **Campus Selection → On-Campus**
5. Configure exam details (College name, exam type, etc.)
6. Upload student CSV/Excel file
7. Click **Generate Seating Arrangement**
8. Verify allocations are created

### Student Data Required
Minimum columns in uploaded file:
- **Register Number** (e.g., AIDS1001)
- **Candidate Name** (e.g., John Doe)
- **Department** (e.g., AIDS, CSE, EEE)
- **Year** (e.g., 1, 2, 3, 4)

**Sample CSV Format:**
```csv
Register Number,Candidate Name,Department,Year
AIDS1001,John Doe,AIDS,2
AIDS1002,Jane Smith,AIDS,3
CSE2001,Bob Johnson,CSE,1
CSE2002,Alice Brown,CSE,2
```

---

## 🎯 Testing the Student Portal

### Test Case 1: Valid Student Login

#### Steps:
1. Open **http://localhost:5000/student-login**
2. Enter:
   - **Register Number:** `AIDS1001`
   - **Year:** `2`
3. Click **Login to Dashboard**

#### Expected Result:
✅ Dashboard loads showing:
- Student name and details
- Seat allocation (Room, Bench, Position)
- Seating visualization
- Download button enabled

---

### Test Case 2: Invalid Credentials

#### Steps:
1. Open **http://localhost:5000/student-login**
2. Enter:
   - **Register Number:** `INVALID999`
   - **Year:** `1`
3. Click **Login to Dashboard**

#### Expected Result:
❌ Error message displays:
- "Invalid Register Number or Year. Please try again."
- Login form clears
- Stays on login page

---

### Test Case 3: Download Seating Slip

#### Steps:
1. ✅ Login with valid credentials
2. Dashboard loads
3. Click **Download Seating Slip (PDF)** button
4. PDF downloads automatically (check Downloads folder)

#### Expected Result:
📄 PDF file created with:
- Filename: `seating_slip_AIDS1001_20260318.pdf`
- College name and student details
- QR code for verification
- Room, bench, and seat information
- Important exam instructions

---

### Test Case 4: Print Hall Ticket

#### Steps:
1. ✅ Login with valid credentials
2. Click **Print Ticket** button
3. Print preview opens
4. Print or save as PDF

#### Expected Result:
🖨️ Print-optimized layout shows:
- Clean formatting for paper
- All essential details visible
- No buttons or navigation elements

---

### Test Case 5: Logout

#### Steps:
1. ✅ Login with valid credentials
2. Click **Logout** button (top right)

#### Expected Result:
✅ Session cleared:
- Redirects to login page
- Message displays: "You have been logged out!"
- All session data cleared
- Clicking back doesn't show dashboard

---

### Test Case 6: Session Protection

#### Steps:
1. Without logging in, navigate to:
   - `http://localhost:5000/student-dashboard`
   - `http://localhost:5000/student-download-slip`

#### Expected Result:
🔒 Protected routes:
- Redirects to `/student-login`
- Message: "Please login first!"
- Cannot access dashboard without authentication

---

### Test Case 7: Internal Exam - View Bench Mate

#### Steps:
1. ✅ Login with internal exam student
   - Use student allocated in internal exam mode
2. Dashboard loads
3. Scroll to "Your Seating Position" section
4. Check "Your Bench Mate" card

#### Expected Result:
👥 Bench mate information shows:
- Different student on same bench
- All their details (Name, Dept, Year)
- Department diversity indicator
- Exam conduct rules reminder

---

### Test Case 8: Semester Exam - Single Seat

#### Steps:
1. ✅ Login with semester exam student
   - Use student allocated in semester exam mode
2. Dashboard loads
3. Scroll to "Your Seating Position" section

#### Expected Result:
🪑 Single seat display:
- Only shows your seat
- No bench mate card
- Visualization shows: "[You (Single Seat)]"
- Seating details show no position attribute

---

## 👥 Sample Test Credentials

Use these to test (after uploading sample data):

| Register Number | Year | Expected Seat | Exam Type |
|---|---|---|---|
| AIDS1001 | 1 | Room 1, Bench 1 | Internal/Semester |
| AIDS1002 | 2 | Room 1, Bench 2 | Internal/Semester |
| CSE2001 | 3 | Room 2, Bench 5 | Internal/Semester |
| EEE1001 | 4 | Room 3, Bench 10 | Internal/Semester |

---

## 🎨 UI Features Tour

### Login Page
- ✨ Clean card-based design
- 🎓 Student icon header
- 📝 Input fields with placeholders
- ℹ️ "What You Can Do" feature list
- 🔙 Back to home link

### Dashboard
- 📊 4-section layout:
  1. **Header:** Welcome message + logout
  2. **Action Buttons:** Download and print
  3. **Information Cards:** Personal & exam details
  4. **Visualization:** Bench layout + bench mate

### Key Badges & Highlights
- **Green Badge:** Department (AIDS, CSE, etc.)
- **Blue Badge:** Exam Type (Internal/Semester)
- **Green Highlight:** Your seat in visualization
- **Blue Box:** Bench mate information

---

## 📱 Mobile Testing

### Test on Mobile Device:
1. Use phone/tablet to access: `http://[YOUR_IP]:5000/student-login`
   - Replace YOUR_IP with your computer's IP (check `ipconfig` command)
2. Or use browser DevTools (F12 → Toggle Device Toolbar)

### Check Mobile Features:
✅ Login form stacks vertically
✅ Cards display single column
✅ Buttons are full width
✅ Text is readable (min 16px font)
✅ Touch targets are 44px minimum

---

## 🔍 Verification Checklist

After implementing, verify:

### Backend Routes
- [ ] `/student-login` - GET/POST working
- [ ] `/student-dashboard` - GET with session check
- [ ] `/student-logout` - GET clears session
- [ ] `/student-download-slip` - GET generates PDF

### Frontend Templates
- [ ] `student-login.html` - Renders correctly
- [ ] `student-dashboard.html` - Shows all sections
- [ ] Form validation works (client-side)
- [ ] Error messages display
- [ ] Success messages display

### Features
- [ ] Login authentication works
- [ ] Session storage functional
- [ ] Dashboard displays correct data
- [ ] PDF generation works
- [ ] QR code generates in PDF
- [ ] Bench mate card shows for internal exams
- [ ] Mobile responsive layout works
- [ ] Print styling works
- [ ] Logout clears session

### Security
- [ ] Cannot access dashboard without login
- [ ] Cannot view other student's data
- [ ] Session expires after logout
- [ ] Invalid credentials rejected
- [ ] No errors in browser console (except intentional)

---

## 🐛 Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'qrcode'"
**Solution:**
```bash
pip install qrcode[pil]
```

### Issue: PDF downloads with wrong filename
**Solution:**
- Check `datetime` import in app.py
- Verify `strftime('%Y%m%d')` format

### Issue: Bench mate not showing
**Solution:**
- Verify student is in internal exam allocation
- Check `seat_position` field exists in data
- Confirm allocation data is loaded

### Issue: Dashboard shows "Seating Not Allocated Yet"
**Solution:**
- Student may not be in allocation results
- Admin needs to generate allocations first
- Check student's register number matches exactly

### Issue: Login fails even with correct credentials
**Solution:**
- Check register number is uppercase (case-sensitive)
- Verify year is single digit (1-4)
- Check student exists in allocation_results
- Look at Flask console for error messages

### Issue: PDF generation is slow
**Solution:**
- QR code generation takes time
- Normal is 500-800ms
- For large batches, consider async processing

---

## 📊 Expected Output

### Login Success
```
✓ Welcome John Doe!
Redirects to → /student-dashboard
```

### Dashboard Display
```
Student Dashboard
Welcome, John Doe

[Download Seating Slip (PDF)] [Print Ticket]

┌─────────────────────────┬──────────────────────┐
│ Personal Information    │ Exam Information     │
├─────────────────────────┼──────────────────────┤
│ Register: AIDS1001      │ Exam: Internal Exam  │
│ Name: John Doe          │ Room: 5              │
│ Dept: [AIDS] (badge)    │ Bench: 10            │
│ Year: Year 2            │ Position: Left       │
└─────────────────────────┴──────────────────────┘

Your Seating Position
→ Bench 10 in Room 5 ←
[You (Left)] | [Other Student (Right)]

Your Bench Mate
👥 Name: Jane Smith
   Dept: CSE, Year 2
```

### PDF Output
```
=================================
        COLLEGE NAME
    SEAT ALLOCATION SLIP
=================================

[QR CODE]

┌──────────────┬──────────────┐
│ Field        │ Details      │
├──────────────┼──────────────┤
│ Reg Number   │ AIDS1001     │
│ Name         │ John Doe     │
│ Dept         │ AIDS         │
│ Year         │ 2            │
│ Exam Type    │ Internal     │
└──────────────┴──────────────┘

SEATING DETAILS
┌──────────────┬──────────────┐
│ Room         │ 5            │
│ Bench        │ 10           │
│ Position     │ Left         │
│ Issued       │ 18-03-2026   │
└──────────────┴──────────────┘

Important: Report 15 minutes early.
```

---

## 🔄 Integration Checklist

### ✅ No Conflicts with Admin Portal
- Student routes (`/student-*`) separate from admin (`/admin-*`)
- Uses same `allocation_results` data structure
- Session management isolated per user
- No database schema changes needed

### ✅ Ready for Production
- Error handling implemented
- Security checks in place
- Mobile responsive
- Performance optimized
- Documentation complete

---

## 📞 Troubleshooting Help

### Get Flask Debug Info
```bash
# In app.py, add before app.run():
app.logger.setLevel(logging.DEBUG)

# Watch the console for detailed error messages
python app.py  # Check console output
```

### Check Session Data
```python
# Add a debug route in app.py:
@app.route('/debug-session')
def debug_session():
    return jsonify(dict(session))

# Access: http://localhost:5000/debug-session
```

### Test Data Validation
```bash
# Use Python shell to test:
python
>>> from app import allocation_results
>>> print(len(allocation_results))  # Should show count
>>> print(allocation_results[0])  # Show first entry
```

---

## 🎉 Success Indicators

You'll know everything is working when:

✅ Students can login with valid credentials
✅ Dashboard shows correct seating information
✅ PDF downloads with student name and details
✅ QR code appears in PDF
✅ Bench mate information shows (internal exams)
✅ Logout clears session
✅ Cannot access dashboard without login
✅ Mobile view is responsive and usable
✅ Print preview shows proper formatting
✅ No error messages in browser console

---

**Happy Testing! 🚀**

For detailed documentation, see: [STUDENT_PORTAL.md](STUDENT_PORTAL.md)
