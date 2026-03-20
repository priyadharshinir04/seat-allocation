# 🚀 Render Deployment Quick Checklist

## ✅ Pre-Deployment (Already Done)

- [x] Created **Procfile** - Tells Render how to run your app with gunicorn
- [x] Created **.render/build.sh** - Setup script for dependencies
- [x] Updated **requirements.txt** - Added gunicorn, twilio, Pillow
- [x] Updated **app.py** - 
  - ✓ Added PORT environment variable support
  - ✓ Logging now uses /tmp (compatible with Render)
  - ✓ Debug mode disabled in production

## 📋 Next Steps (Manual - Takes ~2 minutes)

### 1. Create GitHub Repo
```bash
cd "c:\Users\Priyadharshini\OneDrive\Documents\Desktop\seat allotment1"
git init
git add .
git commit -m "Ready for Render deployment"
git remote add origin https://github.com/YOUR_USERNAME/seat-allocation.git
git push -u origin main
```

### 2. Deploy on Render (Portal)
1. Go to **https://render.com** → Sign up (free account)
2. Click **"New +"** → **"Web Service"**
3. Connect GitHub repository
4. Configure:
   - **Name:** seat-allocation
   - **Environment:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free

### 3. Set Secrets (Optional - Only if using Twilio SMS)
In Render Dashboard → Your Service → Settings → Environment:

```
TWILIO_ACCOUNT_SID=your_sid_here
TWILIO_AUTH_TOKEN=your_token_here
TWILIO_PHONE_NUMBER=+1234567890
SMS_DEMO_MODE=True
```

## 🔗 Result
- Your app will be live at: **https://seat-allocation.onrender.com** (Render assigns the URL)
- Automatic HTTPS
- Free tier is enough for classroom use

## 📊 Free Tier Details

| Feature | Limit |
|---------|-------|
| **Compute** | Shared CPU, 512 MB RAM |
| **Uptime** | 24/7 (wakes up from inactivity in 30 sec) |
| **File Storage** | Temporary (uploads cleared on restart) |
| **Bandwidth** | Unlimited |
| **Cost** | FREE forever |

## ⚠️ Important Notes

1. **Cold Starts:** App sleeps after 15 min of inactivity. First request takes 30 sec. This is normal.
2. **Uploads:** Files are temporary. For persistent storage, you'd need to upgrade or use AWS S3.
3. **SMS:** Requires valid Twilio account. Trial accounts only work with verified numbers.
4. **Admin Access:** Update default credentials in your code before sharing.

## 🆘 Troubleshooting

**"gunicorn not found"?**
→ Error in build. Make sure requirements.txt is pushed.

**App crashes on startup?**
→ Check Render logs for Python errors.

**Cold start too slow?**
→ Normal for free tier. Consider upgrading for always-on instances.

See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for detailed guide.
