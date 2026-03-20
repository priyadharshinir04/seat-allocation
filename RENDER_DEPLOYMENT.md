# Deploying to Render.com (Free Tier)

## Step-by-Step Deployment Guide

### 1. Prepare Your Project
✅ Files already created:
- `Procfile` - Tells Render how to run your app
- `.render/build.sh` - Setup script

### 2. Update requirements.txt (ADD gunicorn)
Your current `requirements.txt` needs `gunicorn` for production:

```txt
Flask==2.3.3
pandas==2.0.3
openpyxl==3.1.2
Werkzeug==2.3.7
gunicorn==21.2.0
twilio==8.10.0
Pillow==10.0.0
```

### 3. Create a GitHub Repository
```bash
git init
git add .
git commit -m "Initial commit for Render deployment"
git remote add origin https://github.com/YOUR_USERNAME/seat-allocation.git
git branch -M main
git push -u origin main
```

### 4. Deploy on Render

1. Go to [render.com](https://render.com)
2. Click **"New +"** → Select **"Web Service"**
3. Connect your GitHub repository
4. Fill in the form:
   - **Name:** `seat-allocation` (or your preferred name)
   - **Environment:** `Python 3`
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** `Free`

5. Click **"Create Web Service"**

### 5. Set Environment Variables (IMPORTANT for Twilio SMS)

In Render dashboard:
1. Go to your service → **Settings** → **Environment**
2. Add these variables:

```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
SMS_DEMO_MODE=True
```

⚠️ **For SMS to work:** Set `SMS_DEMO_MODE=False` only after:
- Twilio Account is SID/Token verified
- Your phone numbers are added to verified list
- Twilio SMS is enabled for your region

### 6. Updates to app.py (Small Change Required)

The app uses `app.run()` which won't work on Render. Change the bottom of `app.py`:

**FROM:**
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**TO:**
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```

### 7. Create Logs Directory in /tmp (For Render)

Update your logging setup in `app.py`:

**FROM:**
```python
if not os.path.exists('logs'):
    os.makedirs('logs')
```

**TO:**
```python
import tempfile
log_dir = os.path.join(tempfile.gettempdir(), 'flask_logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
```

And update handler:
```python
RotatingFileHandler(os.path.join(log_dir, 'sms_notifications.log'), maxBytes=10485760, backupCount=10)
```

---

## Free Tier Limitations & Solutions

| Issue | Solution |
|-------|----------|
| **Cold starts (15 min inactivity)** | Normal - takes 30 sec to wake. Students won't notice |
| **No persistent file storage** | Uploads work during session; files cleared on restart |
| **Limited memory (512 MB)** | Your app is lightweight - no issues |
| **SMS costs** | Twilio trial = free SMS to verified numbers only |

---

## Monitoring Your Deployment

- **Render Dashboard:** View real-time logs and status
- **URL:** `https://seat-allocation.onrender.com` (auto-generated)
- **Custom Domain:** Available in paid plans

---

## Quick Troubleshooting

| Error | Fix |
|-------|-----|
| `gunicorn: command not found` | Run: `pip install gunicorn` locally, push to GitHub |
| `ModuleNotFoundError` | Add missing package to `requirements.txt` |
| `PORT environment variable` | Already handled in updated `app.py` |
| `SMS not sending` | Check `SMS_DEMO_MODE` and Twilio credentials |

---

## Next Steps After Deployment

1. ✅ Test the app at `https://your-service-name.onrender.com`
2. 📱 Verify SMS works (if configured)
3. 📤 Test file uploads (CSV processing)
4. 🔐 Update admin credentials from defaults

**Deployed!** Your seat allocation system is now live on Render. 🚀
