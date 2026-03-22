# Session-Based Persistence - Visual Workflow Guide

## Visual Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│              ADMIN LOGIN SESSION WORKFLOW                       │
└─────────────────────────────────────────────────────────────────┘

                         FRESH SESSION
                         LOGIN PAGE
                              │
                              ▼
                    ┌─────────────────┐
                    │   ADMIN LOGIN   │
                    │  (Credentials)  │
                    └────────┬────────┘
                             │
            ┌────────────────▼────────────────┐
            │  Session Created (Unique ID)    │
            │  All data set to empty/pending  │
            │  session['exam_config'] = {}    │
            │  session['students_data'] = []  │
            └────────────────┬────────────────┘
                             │
                  STEP 1: CONFIGURATION
                             │
            ┌────────────────▼────────────────┐
            │  Configure Exam Settings        │
            │  - College name                 │
            │  - Exam type                    │
            │  - Date, time, classrooms       │
            │                                 │
            │  [Save Configuration]           │
            └────────────────┬────────────────┘
                             │
         ┌───────────────────▼───────────────────┐
         │ SAVED TO SESSION:                     │
         │ session['exam_config'] = {            │
         │     college_name: "...",              │
         │     exam_type: "internal",            │
         │     num_classrooms: 5,                │
         │     seats_per_classroom: 40,          │
         │     total_seats: 200                  │
         │ }                                     │
         └───────────────────┬───────────────────┘
                             │
              STEP 2: EXAM SCHEDULE (OPTIONAL)
                             │
            ┌────────────────▼────────────────┐
            │  Upload Exam Schedule            │
            │  - CSV or Excel file             │
            │  - Subject codes, dates, times   │
            │                                  │
            │  [Upload File]                   │
            └────────────────┬────────────────┘
                             │
         ┌───────────────────▼───────────────────┐
         │ SAVED TO SESSION:                     │
         │ session['exam_schedules'] = [         │
         │     {subject_code, subject_name, ...},│
         │     ...                               │
         │ ]                                     │
         │ session['exam_schedule_count'] = 25   │
         └───────────────────┬───────────────────┘
                             │
              STEP 3: UPLOAD STUDENTS
                             │
            ┌────────────────▼────────────────┐
            │  Upload Student Data             │
            │  - CSV or Excel file             │
            │  - Register no, name, dept, year │
            │                                  │
            │  [Upload File]                   │
            └────────────────┬────────────────┘
                             │
         ┌───────────────────▼───────────────────┐
         │ SAVED TO SESSION:                     │
         │ session['students_data'] = [          │
         │     {reg_no, name, dept, year, ...},  │
         │     ...                               │
         │ ]                                     │
         │ session['students_count'] = 450       │
         └───────────────────┬───────────────────┘
                             │
              STEP 4: GENERATE ALLOCATION
                             │
            ┌────────────────▼────────────────┐
            │  Generate Seating Allocation    │
            │  - Read from session data       │
            │  - Perform allocation logic     │
            │  - Assign rooms, benches, seats │
            │                                 │
            │  [Allocate]                     │
            └────────────────┬────────────────┘
                             │
         ┌───────────────────▼───────────────────┐
         │ SAVED TO SESSION:                     │
         │ session['allocation_results'] = [     │
         │     {reg_no, room, bench, seat, ...}, │
         │     ...                               │
         │ ]                                     │
         └───────────────────┬───────────────────┘
                             │
            ┌────────────────▼────────────────┐
            │    DASHBOARD / VIEW RESULTS     │
            │                                 │
            │  Step 1: Config    ✓ Done       │
            │  Step 2: Schedule  ✓ 25         │
            │  Step 3: Students  ✓ 450        │
            │  Step 4: Allocate  ✓ 450        │
            └────────────────┬────────────────┘
                             │
          ADMIN CAN NOW:
             │
             ├─→ View Classroom Grid
             │   (Uses session['allocation_results'])
             │
             ├─→ View Allocation Results
             │   (Uses session['allocation_results'])
             │
             ├─→ Export as Excel
             │   (Uses session['allocation_results'])
             │
             ├─→ Export as PDF
             │   (Uses session['allocation_results'])
             │
             ├─→ Send SMS Notifications
             │   (Uses session['allocation_results'])
             │
             └─→ Navigate Dashboard
                 (All data persists in session!)
                             │
                             ▼
                    ┌─────────────────┐
                    │  LOGOUT BUTTON  │
                    │   (RED BUTTON)  │
                    └────────┬────────┘
                             │
         ┌───────────────────▼───────────────────┐
         │ SESSION CLEANUP:                      │
         │ - Remove exam_config                  │
         │ - Remove students_data                │
         │ - Remove allocation_results           │
         │ - Remove exam_schedules               │
         │ - Remove all counts                   │
         │ - session.modified = True             │
         │ - Data completely cleared             │
         └───────────────────┬───────────────────┘
                             │
                 Redirect to Login Page
                             │
                   NEXT ADMIN SEES:
                             │
                    Fresh Empty Session
                  All Steps Show "Pending"
                        (Cycle Repeats)
```

---

## Dashboard Status Evolution

### Initial State (Just Logged In)
```
╔════════════════════════════════════════╗
║   On-Campus Exam Dashboard             ║
╠════════════════════════════════════════╣
║                                        ║
║  Workflow Progress:                    ║
║                                        ║
║  Step 1: Config           ○ Pending    ║
║  Step 2: Exam Schedule    ○ Pending    ║
║  Step 3: Upload Students  ○ Pending    ║
║  Step 4: Allocate         ○ Pending    ║
║                                        ║
║  [Stats All at 0]                      ║
║                                        ║
╚════════════════════════════════════════╝
```

### After Configuration
```
╔════════════════════════════════════════╗
║   On-Campus Exam Dashboard             ║
╠════════════════════════════════════════╣
║                                        ║
║  Workflow Progress:                    ║
║                                        ║
║  Step 1: Config           ✓ Done       │◄── Config saved
║  Step 2: Exam Schedule    ○ Pending    ║
║  Step 3: Upload Students  ○ Pending    ║
║  Step 4: Allocate         ○ Pending    ║
║                                        ║
║  Classrooms: 5                         │
║  Seats per Classroom: 40               │
║                                        ║
╚════════════════════════════════════════╝
```

### After Upload Students
```
╔════════════════════════════════════════╗
║   On-Campus Exam Dashboard             ║
╠════════════════════════════════════════╣
║                                        ║
║  Workflow Progress:                    ║
║                                        ║
║  Step 1: Config           ✓ Done       ║
║  Step 2: Exam Schedule    ○ Pending    ║
║  Step 3: Upload Students  ✓ 450        │◄── Students saved
║  Step 4: Allocate         ○ Pending    ║
║                                        ║
║  Total Students: 450                   │
║  Uploaded: 450                         │
║                                        ║
╚════════════════════════════════════════╝
```

### After Allocation
```
╔════════════════════════════════════════╗
║   On-Campus Exam Dashboard             ║
╠════════════════════════════════════════╣
║                                        ║
║  Workflow Progress:                    ║
║                                        ║
║  Step 1: Config           ✓ Done       ║
║  Step 2: Exam Schedule    ○ Pending    ║
║  Step 3: Upload Students  ✓ 450        ║
║  Step 4: Allocate         ✓ 450        │◄── Allocation done
║                                        ║
║  Total Students: 450                   │
║  Allocated: 450                        │
║  Completion: 100%                      │
║                                        ║
╚════════════════════════════════════════╝
```

---

## Route Flow Map

```
┌─────────────────────┐
│   ADMIN LOGIN       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────────┐
│   Campus Selection                  │
│   (On-Campus or Off-Campus)         │
└──────────┬──────────────────────────┘
           │
           ├──────────────────────────┐
           │                          │
           ▼                          ▼
    ┌────────────────┐         ┌──────────────┐
    │  ON-CAMPUS     │         │  OFF-CAMPUS  │
    │  CONFIG        │         │  CONFIG      │
    └────────┬───────┘         └──────────────┘
             │
             ├─────→ session['exam_config']
             │
             ▼
    ┌─────────────────────┐
    │ Allocate Seats      │
    │ or                  │
    │ Exam Schedule       │
    │ or                  │
    │ Upload Students     │
    └─────────┬───────────┘
              │
              ├── session['exam_schedules']
              ├── session['students_data']
              │
              ▼
    ┌──────────────────────┐
    │ View Seating         │
    │ View Results         │
    │ Classroom Grid       │
    │ Export Excel         │
    │ Export PDF           │
    │ Send SMS             │
    └─────────┬────────────┘
              │
              └─→ session['allocation_results']
              └─→ session['exam_config']
              └─→ session['students_data']
              │
              ▼
    ┌──────────────────────┐
    │ On-Campus Dashboard  │
    │ (Status Display)     │
    └─────────┬────────────┘
              │
              ▼
         ┌─────────┐
         │ LOGOUT  │
         │ (CLEARS │
         │  ALL    │
         │ SESSION)
         └────┬────┘
              │
              ▼
         BACK TO LOGIN
```

---

## Data Persistence Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    FLASK SESSION                            │
│                   (Server-Side Memory)                      │
└─────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┼─────────────┐
                │             │             │
                ▼             ▼             ▼
        ┌───────────────┐ ┌───────────┐ ┌──────────────┐
        │   exam_config │ │  students │ │  allocation  │
        │               │ │   _data   │ │   _results   │
        │ {             │ │           │ │              │
        │  college_name │ │ [          │ │ [            │
        │  exam_type    │ │  {         │ │  {           │
        │  date         │ │   reg_no   │ │   reg_no     │
        │  rooms        │ │   name     │ │   room       │
        │  seats        │ │   dept     │ │   bench      │
        │ }             │ │  }         │ │   seat       │
        │               │ │ ]          │ │  }           │
        │               │ │           │ │ ]            │
        │               │ │           │ │              │
        └───┬───────────┘ └─────┬─────┘ └──────┬───────┘
            │                   │              │
            └─────────┬─────────┴──────────────┘
                      │
                AVAILABLE TO ALL ROUTES:
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   Dashboard    Classroom Grid   Export/SMS
   Shows        Display Seats    Use For
   Status       Search Students  Notifications
```

---

## Session Lifecycle

```
TIME AXIS →

╔═════════════════════════════════════════════════════════════════╗
║  SESSION SCOPE: From Login to Logout                           ║
╚═════════════════════════════════════════════════════════════════╝

    Login              Config            Upload           Allocate
      │                  │                  │                │
      ▼                  ▼                  ▼                ▼
    ┌──┐              ┌──────────┐       ┌──────────────┐  ┌────────┐
    │  │──session────→│exam_conf │      │students_data │  │results │
    │  │              │created   │      │created      │  │created │
    │  │              └──────────┘      └──────────────┘  └────────┘
    └──┘
      │
      └─────────────── Session Cookie Set ──────────────┬
                                                         │
                                        ────────────────┴─────────
                                        All Data Available Here
                                        Persist Across Pages
                                               │
                                        ┌──────▼──────┐
                                        │  Navigate   │
                                        │  Dashboard  │
                                        │  View Pages │
                                        │  Export     │
                                        └──────┬──────┘
                                               │
                                            Logout
                                               │
                                        ┌──────▼──────┐
                                        │   SESSION   │
                                        │  CLEARED    │
                                        │ All Keys    │
                                        │ Removed     │
                                        └──────┬──────┘
                                               │
                                        Redirect to
                                        Login Page

           ◄──────── SESSION LIFETIME ────────►
           
           Browser Session OR Configured Timeout
```

---

## Status Badge Legend

```
✓ DONE (Green Badge)
├─ Task completed successfully
├─ Data saved to session
├─ Can proceed to next step
└─ Click to review/edit

○ PENDING (Gray Badge)
├─ Task not yet started
├─ No data in session
├─ Waiting for user action
└─ Can proceed to do this step

[NUMBER] (Count Badge)
├─ Completes the task
├─ Shows data size (e.g., 450 students)
├─ Updated when data uploaded
└─ Helpful for verification
```

---

## Session Storage Pattern

```
Every Upload/Configuration Route:

RECEIVES DATA
    │
    ▼
VALIDATE DATA
    │
    ├─ If invalid ──→ REJECT, show error
    │
    ├─ If valid ──→ CONTINUE
    │
    ▼
STORE IN GLOBAL VARIABLE (for immediate use)
    │
    ├─ global variable = data
    │
    ▼
STORE IN SESSION (for persistence)
    │
    ├─ session['key_name'] = data
    ├─ session.modified = True
    │
    ▼
SHOW SUCCESS MESSAGE
    │
    └─→ Flash message to user


Every View/Export Route:

CHECK SESSION
    │
    ├─ If session has data ──→ USE IT (faster!)
    │
    ├─ If NO session data ──→ USE GLOBAL VARIABLE
    │
    ├─ If NEITHER exists ──→ ERROR or empty page
    │
    ▼
RETRIEVE ALL DEPENDENT DATA
    │
    ├─ session['allocation_results']
    ├─ session['exam_config']
    ├─ session['students_data']
    │
    ▼
DISPLAY/EXPORT/PROCESS
    │
    └─→ User sees data!
```

---

## Admin Workflow - Step by Step

```
┌──────────────────────────────────────────────────────────────┐
│ TYPICAL ADMIN WORKFLOW OVER 30 MINUTES                       │
└──────────────────────────────────────────────────────────────┘

Time │ Action                  │ Session State  │ User Sees
─────┼─────────────────────────┼────────────────┼────────────────
 0m  │ Login                   │ Empty/Fresh    │ Login Success
     │                         │ Redirected     │
─────┼─────────────────────────┼────────────────┼────────────────
 2m  │ Configure Exam          │ exam_config    │ ✓ Saved
     │                         │ stored         │
─────┼─────────────────────────┼────────────────┼────────────────
 5m  │ Navigate to Dashboard   │ exam_config    │ Status shows
     │                         │ available      │ Step 1: ✓ Done
─────┼─────────────────────────┼────────────────┼────────────────
 7m  │ Upload Student File     │ +students_data │ ✓ Uploaded
     │                         │ stored         │ 450 students
─────┼─────────────────────────┼────────────────┼────────────────
10m  │ Back to Dashboard       │ All persisted  │ Step 3: ✓ 450
     │ (refresh page)          │ Session intact │ (No re-upload!)
─────┼─────────────────────────┼────────────────┼────────────────
12m  │ Generate Seating        │ +allocation_   │ ✓ Allocated
     │                         │ results stored │ 450 students
─────┼─────────────────────────┼────────────────┼────────────────
15m  │ View Classroom Grid     │ allocation_    │ Shows grid with
     │                         │ results used   │ all students
─────┼─────────────────────────┼────────────────┼────────────────
18m  │ Go to Export Page       │ All data       │ Downloaded
     │ (Export as Excel)       │ available      │ Excel file
─────┼─────────────────────────┼────────────────┼────────────────
20m  │ Return to Dashboard     │ Session still  │ Step 4: ✓ 450
     │ (Click back)            │ intact!        │ (Data persists!)
─────┼─────────────────────────┼────────────────┼────────────────
25m  │ View another report     │ allocation_    │ Can search,
     │ (Search students)       │ results ready  │ filters work,
     │                         │ from session   │ all good
─────┼─────────────────────────┼────────────────┼────────────────
28m  │ Click LOGOUT            │ ALL CLEARED    │ Goodbye message
     │                         │ exam_config    │ Redirected to
     │                         │ students_data  │ login page
     │                         │ allocation_    │
     │                         │ results        │
     │                         │ ALL DELETED    │
─────┼─────────────────────────┼────────────────┼────────────────
30m  │ (Next Admin logs in)    │ Fresh/Empty    │ Fresh Dashboard
     │                         │ session        │ All steps pending
     │                         │ No old data    │ Starts fresh
```

---

## Color Coding Reference

```
🟢 GREEN
├─ Completed status
├─ ✓ checkmark
├─ Success messages
└─ "Done" badges

🔴 RED
├─ Logout button
├─ Error messages
├─ Danger actions
└─ Important alerts

⚫ GRAY
├─ Pending status
├─ ○ circle icon
├─ Inactive states
└─ "Pending" badges

🔵 BLUE
├─ Primary buttons
├─ Links
├─ Information
└─ Main actions
```

---

**This visual guide helps stakeholders understand the session-based persistence feature at a glance.**
