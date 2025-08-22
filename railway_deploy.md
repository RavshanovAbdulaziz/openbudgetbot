# 🚂 Railway.app-ə Deploy Etmək

Bu sənəd Telegram botunuzu Railway.app-ə deploy etmək üçün addım-addım təlimatları təqdim edir.

## 📋 Tələblər

- GitHub-da layihə repository-si
- Railway.app hesabı
- Telegram Bot Token (@BotFather-dan)

## 🚀 Deploy Addımları

### 1. Railway.app-ə Daxil Olun

1. [Railway.app](https://railway.app) saytına daxil olun
2. GitHub hesabınızla giriş edin
3. "Start a New Project" düyməsinə basın

### 2. Layihəni Seçin

1. "Deploy from GitHub repo" seçin
2. GitHub repository-nizi seçin (`botv2`)
3. "Deploy Now" düyməsinə basın

### 3. Environment Dəyişənlərini Təyin Edin

Railway dashboard-da layihənizi açın və "Variables" bölməsinə keçin:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
LOG_LEVEL=INFO
```

**Vacib:** `TELEGRAM_BOT_TOKEN` dəyişəni mütləq təyin edilməlidir!

### 4. Deploy Etmə

1. "Deploy" düyməsinə basın
2. Railway avtomatik olaraq layihəni build və deploy edəcək
3. Deploy tamamlandıqdan sonra "View" düyməsinə basın

### 5. Webhook URL-ni Təyin Edin

1. Railway dashboard-da layihənizin URL-ni kopyalayın
2. Telegram-da @BotFather ilə əlaqə saxlayın
3. `/setwebhook` əmrini göndərin və URL-ni təyin edin:

```
/setwebhook https://your-railway-url.railway.app/webhook
```

**Və ya avtomatik olaraq:**

Railway URL-ni ziyarət edin: `https://your-railway-url.railway.app/setwebhook`

## 🔧 Railway Konfiqurasiyası

### Procfile
```
web: python app.py
```

### runtime.txt
```
python-3.11.7
```

### railway.json
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python app.py",
    "healthcheckPath": "/",
    "healthcheckTimeout": 300,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

## 🌐 Webhook Endpoint-ləri

Deploy edildikdən sonra aşağıdakı endpoint-lər mövcud olacaq:

- **`/`** - Health check (Railway üçün)
- **`/webhook`** - Telegram webhook endpoint-i
- **`/setwebhook`** - Webhook URL-ni avtomatik təyin et
- **`/getwebhook`** - Cari webhook məlumatını al
- **`/deletewebhook`** - Webhook-u sil
- **`/status`** - Bot status və məlumatları

## 📱 Bot Test Etmə

1. Telegram-da botunuzu tapın
2. `/start` əmrini göndərin
3. Bot cavab verməlidir

## 🐛 Problemlərin Həlli

### Bot Cavab Vermir

1. **Environment dəyişənlərini yoxlayın:**
   - `TELEGRAM_BOT_TOKEN` düzgün təyin edilibmi?
   - Railway dashboard-da dəyişənlər görünür?

2. **Logları yoxlayın:**
   - Railway dashboard-da "Logs" bölməsinə keçin
   - Xətaları tapın və həll edin

3. **Webhook URL-ni yoxlayın:**
   - BotFather-da webhook URL düzgün təyin edilibmi?
   - Railway URL düzgündürmü?

4. **Webhook status yoxlayın:**
   - `/status` endpoint-ini ziyarət edin
   - Webhook məlumatlarını yoxlayın

### Deploy Xətası

1. **Requirements faylını yoxlayın:**
   - `requirements.txt` düzgün formatda?
   - Bütün asılılıqlar mövcud?

2. **Python versiyasını yoxlayın:**
   - `runtime.txt` faylında düzgün versiya?
   - Railway bu versiyanı dəstəkləyir?

## 🔄 Yenidən Deploy

Kod dəyişikliklərindən sonra:

1. GitHub-a dəyişiklikləri push edin
2. Railway avtomatik olaraq yenidən deploy edəcək
3. Və ya manual olaraq "Deploy" düyməsinə basın

## 📊 Monitoring

Railway dashboard-da:

- **Logs:** Real-time logları izləyin
- **Metrics:** CPU, RAM istifadəsini izləyin
- **Deployments:** Deploy tarixçəsini görün

## 💰 Qiymətləndirmə

- **Free Tier:** Ayda 500 saat
- **Pro Plan:** $5/ay (daha çox resurslar)

## 🔗 Faydalı Linklər

- [Railway Documentation](https://docs.railway.app/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/)

## 📞 Dəstək

Əgər problem yaranırsa:

1. Railway Logs-ı yoxlayın
2. GitHub Issues yaradın
3. Railway Discord server-inə qoşulun

---

# 🚂 Deploy to Railway.app (English)

This document provides step-by-step instructions for deploying your Telegram bot to Railway.app.

## 📋 Requirements

- GitHub repository
- Railway.app account
- Telegram Bot Token (from @BotFather)

## 🚀 Deployment Steps

### 1. Access Railway.app

1. Go to [Railway.app](https://railway.app)
2. Sign in with your GitHub account
3. Click "Start a New Project"

### 2. Select Project

1. Choose "Deploy from GitHub repo"
2. Select your GitHub repository (`botv2`)
3. Click "Deploy Now"

### 3. Set Environment Variables

In Railway dashboard, go to "Variables" section:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
LOG_LEVEL=INFO
```

**Important:** `TELEGRAM_BOT_TOKEN` variable must be set!

### 4. Deploy

1. Click "Deploy" button
2. Railway will automatically build and deploy your project
3. After deployment, click "View" button

### 5. Set Webhook URL

1. Copy your Railway project URL from dashboard
2. Contact @BotFather on Telegram
3. Send `/setwebhook` command and set the URL:

```
/setwebhook https://your-railway-url.railway.app/webhook
```

**Or automatically:**

Visit Railway URL: `https://your-railway-url.railway.app/setwebhook`

## 🔧 Railway Configuration

### Procfile
```
web: python app.py
```

### runtime.txt
```
python-3.11.7
```

### railway.json
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python app.py",
    "healthcheckPath": "/",
    "healthcheckTimeout": 300,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

## 🌐 Webhook Endpoints

After deployment, the following endpoints will be available:

- **`/`** - Health check (for Railway)
- **`/webhook`** - Telegram webhook endpoint
- **`/setwebhook`** - Automatically set webhook URL
- **`/getwebhook`** - Get current webhook info
- **`/deletewebhook`** - Delete webhook
- **`/status`** - Bot status and information

## 📱 Test Your Bot

1. Find your bot on Telegram
2. Send `/start` command
3. Bot should respond

## 🐛 Troubleshooting

### Bot Not Responding

1. **Check environment variables:**
   - Is `TELEGRAM_BOT_TOKEN` set correctly?
   - Are variables visible in Railway dashboard?

2. **Check logs:**
   - Go to "Logs" section in Railway dashboard
   - Find and fix errors

3. **Check webhook URL:**
   - Is webhook URL set correctly in BotFather?
   - Is Railway URL correct?

4. **Check webhook status:**
   - Visit `/status` endpoint
   - Check webhook information

### Deployment Error

1. **Check requirements file:**
   - Is `requirements.txt` in correct format?
   - Are all dependencies available?

2. **Check Python version:**
   - Is correct version in `runtime.txt`?
   - Does Railway support this version?

## 🔄 Redeploy

After code changes:

1. Push changes to GitHub
2. Railway will automatically redeploy
3. Or manually click "Deploy" button

## 📊 Monitoring

In Railway dashboard:

- **Logs:** Monitor real-time logs
- **Metrics:** Monitor CPU, RAM usage
- **Deployments:** View deployment history

## 💰 Pricing

- **Free Tier:** 500 hours/month
- **Pro Plan:** $5/month (more resources)

## 🔗 Useful Links

- [Railway Documentation](https://docs.railway.app/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/)

## 📞 Support

If you encounter problems:

1. Check Railway Logs
2. Create GitHub Issues
3. Join Railway Discord server
