# SMS Notification Feature - Setup Guide

## Overview

The Automatic Classroom and Seat Allocation System now includes SMS notification capability to send pre-exam alerts to students 45 minutes before their exam.

## Features

✅ **Automatic SMS Sending** - Send SMS to all allocated students with one click
✅ **Rich Message Content** - Includes student name, subject, exam time, room/bench details
✅ **Error Handling** - Gracefully handles invalid phone numbers, API failures, and missing data
✅ **Logging System** - Complete audit trail of all SMS operations in `logs/sms_notifications.log`
✅ **No Breaking Changes** - Fully optional feature, doesn't affect existing system

## Prerequisites

### 1. Twilio Account Setup

1. **Create a Twilio Account**
   - Go to https://www.twilio.com/
   - Sign up for a free trial account
   - Verify your email and phone number

2. **Get Your Credentials**
   - After login, go to the Twilio Console
   - Note your **Account SID** and **Auth Token** (keep these safe!)
   - Get a **Twilio Phone Number** (free trial includes one)

### 2. Python Package

The Twilio package is already installed:
```bash
pip install twilio
```

## Configuration

### Method 1: Environment Variables (Recommended for Production)

Set environment variables before running the app:

**On Windows (PowerShell):**
```powershell
$env:TWILIO_ACCOUNT_SID = "your_account_sid_here"
$env:TWILIO_AUTH_TOKEN = "your_auth_token_here"
$env:TWILIO_PHONE_NUMBER = "+1234567890"
python app.py
```

**On Windows (Command Prompt):**
```cmd
set TWILIO_ACCOUNT_SID=your_account_sid_here
set TWILIO_AUTH_TOKEN=your_auth_token_here
set TWILIO_PHONE_NUMBER=+1234567890
python app.py
```

**On Mac/Linux:**
```bash
export TWILIO_ACCOUNT_SID='your_account_sid_here'
export TWILIO_AUTH_TOKEN='your_auth_token_here'
export TWILIO_PHONE_NUMBER='+1234567890'
python app.py
```

### Method 2: Direct Configuration (Development Only)

Edit `app.py` lines 31-33:

```python
TWILIO_ACCOUNT_SID = 'AC1234567890abcdef'  # Your Account SID
TWILIO_AUTH_TOKEN = 'your_auth_token'     # Your Auth Token
TWILIO_PHONE_NUMBER = '+14155552671'      # Your Twilio Number
```

⚠️ **WARNING**: Never commit credentials to version control!

### Method 3: Configuration File (Development)

Create a `.env` file in the project root:

```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
```

Then install python-dotenv:
```bash
pip install python-dotenv
```

## Student Data Format

To use SMS notifications, include a **Phone Number** column in your student upload CSV:

### CSV Format Example

```csv
Register Number,Candidate Name,Department,Year,Phone Number
REG001,Ram Kumar,CSE,1,9876543210
REG002,Priya Singh,CSE,1,9123456789
REG003,Akshay Patel,ECE,1,8765432109
REG004,Neha Sharma,ECE,1,9988776655
```

### Supported Column Names

Any of these will be recognized as phone number column:
- `Phone Number`
- `Phone`
- `Mobile`
- `Mobile Number`
- `Contact`
- `Contact Number`
- `phone_number`

### Phone Number Format

- Accepts: `9876543210`, `+919876543210`, `+1 987 654 3210`
- Automatically cleans separators (spaces, dashes, parentheses)
- Invalid numbers are skipped with warning logged

## Using SMS Notifications

### Step-by-Step Guide

1. **Configure Exam**
   - Login as Admin
   - Select "On-Campus Exam"
   - Fill in exam details (date, time, classrooms, etc.)

2. **Upload Exam Schedule** (Optional)
   - Click "Upload Exam Schedule" button
   - Upload CSV with subject details

3. **Upload Students**
   - Include phone numbers in Candidate Data CSV
   - Upload the file

4. **Generate Allocations**
   - Click "Allocate Seats"
   - System generates seating arrangement

5. **Send SMS Notifications**
   - Go to "On-Campus Exam Dashboard"
   - Click "Send SMS Notifications" button (purple button with mobile icon)
   - Wait for confirmation message

### What Students Receive

Each student receives an SMS like:

```
Hi Ram Kumar,
Your exam (Data Structures) starts at 10:30.
Room: 5, Bench: 12.
Please arrive early.
```

## Logging & Monitoring

All SMS operations are logged to `logs/sms_notifications.log`:

### Check Logs

**View recent SMS activity:**
```bash
tail -f logs/sms_notifications.log
```

**Search for specific student:**
```bash
grep "9876543210" logs/sms_notifications.log
```

### Log Format

Each entry contains:
- Timestamp
- Log level (INFO, ERROR, WARNING)
- Operation details
- Student phone number
- Twilio Message SID (for tracking)

### Example Log Entries

✅ Success:
```
2026-03-19 10:45:23 - INFO - SMS sent successfully to 9876543210 (SID: SM1234567890abcdef)
```

❌ Failure:
```
2026-03-19 10:45:24 - ERROR - Failed to send SMS to 9876543210: Invalid phone number
```

⚠️ Warning:
```
2026-03-19 10:45:25 - WARNING - Empty phone number for student Ram Kumar
```

## API Response

When you click "Send SMS Notifications", the system returns:

### Success Response
```json
{
  "success": 250,
  "failed": 5,
  "skipped": 65,
  "total": 320,
  "errors": ["REG142: Invalid phone number", "REG256: API timeout"]
}
```

### What Each Field Means

- **success**: SMS sent successfully
- **failed**: SMS sending failed (check logs for details)
- **skipped**: No phone number provided for student
- **total**: Total students allocated
- **errors**: First 5 errors encountered

## Troubleshooting

### Issue: "Twilio credentials not configured"

**Solution**: Set environment variables before running app
```powershell
$env:TWILIO_ACCOUNT_SID = "AC..."
$env:TWILIO_AUTH_TOKEN = "..."
$env:TWILIO_PHONE_NUMBER = "+1..."
```

### Issue: "SMS sending failed: Invalid parameter"

**Solution**: Check Twilio phone number format - must include country code
```
❌ Wrong: 1234567890, 987-654-3210
✅ Correct: +14155552671, +919876543210
```

### Issue: "No students allocated yet"

**Solution**: Complete allocation process first:
1. Upload exam configuration
2. Upload student data
3. Click "Allocate Seats"

### Issue: Some students not receiving SMS

**Possible causes:**
1. **Empty phone number** - Check student data CSV
2. **Invalid format** - Phone numbers cleaned automatically, but extreme formats may fail
3. **Trial account limitations** - Free Twilio trial can only send to verified numbers
4. **API failure** - Check logs for detailed error messages

### Issue: SMS logged but not received

**Likely cause**: Twilio free trial only sends SMS to verified numbers
- Add recipient phone to verified callers list in Twilio Console
- Or upgrade to paid account for unrestricted sending

## Security Best Practices

1. **Never commit credentials** - Use environment variables
2. **Keep tokens secure** - Treat like passwords
3. **Check logs regularly** - Monitor for suspicious activity
4. **Use HTTPS** - Deploy on secure connection only
5. **Verify phone numbers** - Validate format before allocation

## Limits & Constraints

### Twilio Free Trial
- Limited to verified numbers only
- Lower throughput
- Sufficient for testing and demo

### Production Deployment
- Upgrade to paid Twilio account for unlimited SMS
- Typical cost: ~$0.01 per SMS
- 320 students ≈ $3.20 per exam cycle

### System Limits
- SMS sends up to 1000 per minute
- Logs rotate at 10MB to prevent disk fill
- Max 10 backup log files kept

## Sample Workflow

```
Admin Login
    ↓
Configure Exam (date: 2026-04-15, time: 10:00)
    ↓
Upload Exam Schedule (subjects, timing)
    ↓
Upload Students (with phone numbers) → 320 students
    ↓
Generate Allocation (automatic seating)
    ↓
View Results & Verify
    ↓
[45 minutes before exam]
Send SMS Notifications
    ↓
✅ 285 SMS sent
⚠️  25 failed (invalid numbers)
⏭️ 10 skipped (no phone)
    ↓
Students receive alerts with room/bench details
```

## Performance Metrics

- **SMS per second**: ~10-20 (depending on API)
- **Typical batch time**: 320 students ≈ 20-30 seconds
- **Log file growth**: ~1KB per SMS sent

## Demo Account Credentials (For Testing)

If you need a test Twilio account:
- Twilio offers $15 free trial credit
- Free trial includes 1 trial phone number
- Add test numbers in Console to receive SMS

## FAQ

**Q: Can I customize the SMS message?**
A: Yes! Edit the message format in `send_sms_notification()` function in app.py (line ~95)

**Q: What if student has no phone number?**
A: That student is skipped with a warning logged. No error thrown.

**Q: Can I schedule SMS for specific time?**
A: Current implementation sends immediately. For scheduled SMS, use Twilio's scheduled API or implement background scheduler.

**Q: How do I test SMS without sending to real numbers?**
A: Use Twilio test credentials or add phone to verified numbers in trial account.

**Q: Is SMS cost included in the system?**
A: No, SMS costs are separate and only apply when using paid Twilio account.

## Support & Documentation

- **Twilio Docs**: https://www.twilio.com/docs/sms
- **Python SDK**: https://github.com/twilio/twilio-python
- **Common Issues**: https://www.twilio.com/docs/sms/faq

## Version Information

- **Feature Added**: Yes (SMS Notification v1.0)
- **Last Updated**: 2026-03-19
- **Compatible With**: Python 3.10+, Flask 3.1.3+, Twilio 8.0+

---

**Always keep credentials secure and never share them publicly!**
