# SMS Notifications - Quick Reference

## ⚡ Pre-Exam SMS Alert System

Send automated SMS notifications to students 45 minutes before their exam.

---

## 🚀 Quick Start

### 1️⃣ Before First Use (One-Time Setup)

```powershell
# Set Twilio credentials (Windows PowerShell)
$env:TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:TWILIO_AUTH_TOKEN = "your_auth_token"
$env:TWILIO_PHONE_NUMBER = "+1234567890"

# Start Flask app
python app.py
```

👉 Get credentials from: https://www.twilio.com/console

---

### 2️⃣ Prepare Student Data

Include a **Phone Number** column in your CSV:

```csv
Register Number,Candidate Name,Department,Year,Phone Number
REG001,Ram Kumar,CSE,1,9876543210
REG002,Priya Singh,CSE,1,9123456789
```

✅ Format: `9876543210` or `+919876543210`

---

### 3️⃣ Send SMS

**In Admin Dashboard:**

1. Login as Admin
2. Choose "On-Campus Exam"
3. Configure exam (date, time, rooms)
4. Upload students (with phone column)
5. Click **"Send SMS Notifications"** button
6. Wait for confirmation message

---

## 📱 What Students Receive

```
Hi Ram Kumar,
Your exam (Data Structures) starts at 10:30.
Room: 5, Bench: 12.
Please arrive early.
```

---

## 📊 Results Display

After clicking "Send SMS Notifications":

```
✅ SMS Sent: 285 successful
❌ 25 failed (check logs)
⏭️  10 skipped (no phone number)
```

---

## 📝 Check Logs

```bash
# View SMS logs
tail -f logs/sms_notifications.log

# Search for phone number
grep "9876543210" logs/sms_notifications.log

# Find errors
grep "ERROR" logs/sms_notifications.log
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Credentials not configured" | Set environment variables (see setup) |
| "Some students not receiving" | Use verified numbers (free trial limitation) |
| SMS shows failed | Check phone format (+country_code) |
| Button not showing | Ensure allocations are complete |
| No logs created | Check write permissions on `logs/` folder |

---

## 📞 Phone Column Names

Any of these will be recognized:
- ✅ Phone Number
- ✅ Phone
- ✅ Mobile
- ✅ Contact
- ✅ phone_number
- ✅ contact_number

---

## 💡 Pro Tips

1. **Test First** - Use `sample_students_with_phones.csv` to test
2. **Verify Numbers** - Ensure format: +Country_CodeNumber
3. **Check Logs** - Always review `logs/sms_notifications.log` after sending
4. **Upgrade Account** - Free trial limited to verified numbers only
5. **Schedule Early** - Send 45+ minutes before exam

---

## ⚠️ Important

- 🔐 Keep TWILIO_AUTH_TOKEN secret
- 📱 Valid phone format: +91XXXXXXXXX0 (with country code)
- 💰 Production costs ~$0.01 per SMS
- 📊 Free trial: $15 credit (test before production)

---

## 📎 Quick References

- **Setup Guide**: `SMS_SETUP_GUIDE.md`
- **Test Data**: `sample_students_with_phones.csv`
- **Feature Summary**: `SMS_FEATURE_SUMMARY.md`

---

**Need help?**
1. Check `SMS_SETUP_GUIDE.md` for detailed instructions
2. Review logs in `logs/sms_notifications.log`
3. Check Twilio dashboard for account status
