# Session-Based Persistence Quick Reference

## What's New?

When the admin logs in and uploads/configures data, the system now remembers everything during the same login session. You no longer need to re-upload data if you navigate around the dashboard.

## Quick Start for Admins

### Before (Old Way)
```
Login → Configure Exam → Upload Students 
→ Navigate Away → Return to Dashboard 
→ Upload Students AGAIN (frustrated!)
```

### Now (New Way)
```
Login → Configure Exam → Upload Students 
→ Navigate Away → Return to Dashboard 
→ Data Still There! (happy!)
```

## Session Workflow

### Within Same Login Session
```
Admin Login
    ↓
Configure Exam (Step 1) → Saved in Session
    ↓
Upload Exam Schedule (Step 2) → Saved in Session
    ↓
Upload Students (Step 3) → Saved in Session
    ↓
Generate Allocation (Step 4) → Saved in Session
    ↓
Navigate Dashboard, View Results, Export
    → All Data Available from Session
    ↓
Click Logout → All Data Cleared
```

### Screenshot of Dashboard Status

```
On-Campus Exam Dashboard

Step 1: Config       ✓ Done
Step 2: Exam Schedule ✓ 25 subjects
Step 3: Upload Students ✓ 450 students
Step 4: Allocate      ✓ 450 allocated
```

## Where to Find the Logout Button

**Option 1: From On-Campus Dashboard**
- Click red "Logout" button in top-right header

**Option 2: From Configuration Page**
- Click red "Logout" button next to "Back" button

**Option 3: From Any Admin Page**
- Use browser's navigation to get to any admin page
- Logout button available from most pages

## How to Use

### Typical Workflow

1. **Login** as admin with credentials
2. **Configure Exam**
   - Enter college name
   - Select exam type (Internal or Semester)
   - Set exam date and time
   - Specify classrooms and capacity
   - Click "Save Configuration"
   - ✓ Step 1 now shows as "Done"

3. **Upload Exam Schedule** (Optional)
   - Click "Upload Exam Schedule"
   - Select CSV/Excel file
   - ✓ Step 2 shows count (e.g., "✓ 25 subjects")

4. **Upload Students**
   - Click "Upload Students" 
   - Select CSV/Excel file with student data
   - ✓ Step 3 shows count (e.g., "✓ 450 students")

5. **Generate Allocation**
   - Click "Allocate" or "Allocate Seats"
   - System generates seating arrangement
   - ✓ Step 4 shows count (e.g., "✓ 450 allocated")

6. **View & Export**
   - View Classroom Layout
   - View Allocation Results
   - Export as Excel
   - Export as PDF
   - Send SMS Notifications (Demo)

7. **Navigate Freely**
   - All data persists during session
   - Go to dashboard, classroom grid, results
   - Back button and navigation work smoothly

8. **When Done - Logout**
   - Click red "Logout" button
   - All session data cleared
   - Redirected to login page
   - Next admin gets fresh start

## Status Indicators Explained

### Dashboard Status Display

```
Step 1: Config          → ✓ Done         (Blue checkmark = complete)
Step 2: Exam Schedule   → ✓ 25          (Count = number of records)
Step 3: Upload Students → ✓ 450         (Count = number of students)
Step 4: Allocate        → ✓ 450         (Count = number allocated)
```

### Visual Cues

- **✓ Done** = Task completed (green badge)
- **✓ [Number]** = Task completed with count (green badge)
- **○ Pending** = Task not yet done (gray badge)

## Common Scenarios

### Scenario 1: Reviewing Before Allocation
```
1. Configure exam
2. Upload students
3. Go to dashboard (no need to re-upload!)
4. Review configuration
5. Check student count
6. Click "Allocate" button
7. View results immediately
```

### Scenario 2: Back-and-Forth Navigation
```
1. Upload students
2. Go to classroom layout
3. Search for a student
4. Go back to dashboard (data still there!)
5. Click classroom grid again
6. Scroll through all students
7. Everything still loaded!
```

### Scenario 3: Exporting Multiple Formats
```
1. Generate allocation
2. Export as Excel
3. Back to dashboard (data still there!)
4. Export as PDF
5. Export as CSV
6. Data available for all exports
```

### Scenario 4: Switching Admins
```
Admin A: Log in, configure, upload → Allocate → Logout
         (Session data cleared)
Admin B: Log in, sees empty dashboard
         (Previous admin's data not visible)
         Configure fresh exam
         Upload students
         Done!
```

## Key Features

✅ **No Re-Upload** - Upload once per session, use data anywhere

✅ **Visual Progress** - Dashboard shows exactly what's done

✅ **Logout Clears Everything** - Perfect security after session ends

✅ **Works Everywhere** - Navigate to any admin page, data persists

✅ **Fast Dashboard** - Opens quickly with cached session data

✅ **Safe for Multiple Users** - Each admin has isolated session

❌ **Data Lost After Logout** (As designed - clean state for next admin)

❌ **Data Doesn't Survive Browser Close** (For security)

❌ **Data Not Saved to Database** (Session only - restart resets)

## Tips & Tricks

### Tip 1: Keep Session Open
- Once you upload data, avoid closing the browser or logging out
- Leave the session open while you work
- Only logout when completely done for the session

### Tip 2: Check Status First
- Always check the workflow steps status
- Know what's been completed
- Prevents accidental re-uploads

### Tip 3: Use Logout for Clean Handoff
- When another admin needs to work, logout first
- Their login gets a completely fresh state
- No confusion from previous admin's data

### Tip 4: Export Before Close
- If you need to keep data, export to Excel/PDF
- Session data is temporary
- Exports are permanent files

### Tip 5: Clear Browser Cache if Issues
- If data seems stuck, clear browser cache
- Force refresh (Ctrl+F5 or Cmd+Shift+R)
- Session should reset with proper data

## Troubleshooting

### Q: I uploaded students but they disappeared!
**A:** You probably logged out or closed the browser. Upload again - you're in a fresh session.

### Q: Why can't I see my previous data?
**A:** Session data only persists during one login. After logout, it's gone (by design). Upload again.

### Q: The status shows pending but I did that step?
**A:** Try refreshing the page. The status should update. If not, that step data may not be in session.

### Q: Can I continue where I left off tomorrow?
**A:** No, session data is temporary. Save your allocation to Excel or PDF to keep records.

### Q: Two admins working at once - will data mix?
**A:** No! Each admin has separate session. Their data is completely isolated.

### Q: I logged out by accident, can I get my data back?
**A:** Session data is cleared immediately upon logout. You'll need to upload again.

## Technical Details

### What Gets Saved in Session
- Exam configuration (college name, dates, capacity)
- Student data (register number, name, department, year, phone)
- Exam schedule (subject codes, dates, times)
- Allocation results (seat assignments, room numbers)

### What Does NOT Get Saved
- Login credentials (handled separately)
- System settings
- PDF/Excel exports (saved to disk)
- Student portal data (separate system)

### Where's the Data Stored
- Flask Server-Side Session
- Signed cookies (cannot be tampered with)
- Lifetime: Duration of browser session
- Cleared on: Logout or browser close

### Security
- Data is encrypted with session secret key
- Each admin gets unique session ID
- Data never persists between sessions
- Logout immediately wipes all session data

## For Support

If you encounter issues:
1. Check this quick reference
2. Refresh the page (Ctrl+F5)
3. Clear browser cache
4. Contact IT support with:
   - What step you were on
   - Expected vs. actual behavior
   - Browser and device info

---

**Last Updated:** March 2026
**Feature Version:** 1.0 - Session Persistence
**Tested On:** Firefox, Chrome, Safari, Edge
