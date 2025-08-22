# 🤖 Telegram Bot v2

Bu layihə güclü və genişləndirilə bilən Telegram bot mühitidir.

## 🌟 Xüsusiyyətlər

- **Modular struktur** - Kod təşkili və genişləndirmə asanlığı
- **Asynchronous architecture** - Yüksək performans
- **Inline keyboards** - İnteraktiv istifadəçi interfeysi
- **Error handling** - Xətaların idarə edilməsi
- **Logging system** - Sistem logları
- **Multi-language support** - Çoxdilli dəstək (Azərbaycan dili, English)

## 📋 Tələblər

- Python 3.8+
- pip (Python package manager)

## 🚀 Quraşdırma

### 1. Layihəni klonlayın
```bash
git clone <repository-url>
cd botv2
```

### 2. Virtual environment yaradın (tövsiyə olunur)
```bash
python -m venv venv

# Windows üçün
venv\Scripts\activate

# Linux/Mac üçün
source venv/bin/activate
```

### 3. Asılılıqları quraşdırın
```bash
pip install -r requirements.txt
```

### 4. Telegram Bot Token əldə edin
1. Telegram-da [@BotFather](https://t.me/botfather) ilə əlaqə saxlayın
2. `/newbot` əmrini göndərin
3. Bot üçün ad və username təyin edin
4. Bot token-ı kopyalayın

### 5. Environment faylını yaradın
```bash
# .env faylını yaradın
cp env_example.txt .env
```

`.env` faylını redaktə edin və bot token-ını əlavə edin:
```env
TELEGRAM_BOT_TOKEN=your_actual_bot_token_here
```

## 🎯 İstifadə

### Əsas botu işə salın
```bash
python bot.py
```

### Təkmilləşdirilmiş botu işə salın
```bash
python bot_enhanced.py
```

## 📚 Mövcud əmrlər

| Əmr | Təsvir |
|-----|---------|
| `/start` | Botu başlat və xoş gəldiniz mesajını göstər |
| `/help` | Kömək məlumatını göstər |
| `/info` | Bot haqqında ətraflı məlumat |
| `/echo <mətn>` | Göndərilən mətni təkrarla |
| `/weather` | Hava haqqında məlumat (tezliklə) |
| `/translate <mətn>` | Mətni tərcümə et (tezliklə) |

## 🏗️ Layihə strukturu

```
botv2/
├── bot.py                 # Əsas bot faylı
├── bot_enhanced.py        # Təkmilləşdirilmiş bot
├── handlers.py            # Mesaj və əmr işləyiciləri
├── config.py              # Konfiqurasiya faylı
├── requirements.txt       # Python asılılıqları
├── env_example.txt        # Environment dəyişənləri nümunəsi
└── README.md             # Bu fayl
```

## 🔧 Konfiqurasiya

`config.py` faylında bot parametrlərini dəyişə bilərsiniz:

- Bot adı və təsviri
- Logging səviyyəsi
- Database konfiqurasiyası
- Webhook URL (production üçün)

## 🚀 Genişləndirmə

### Yeni əmr əlavə etmək

1. `handlers.py` faylında yeni funksiya yaradın:
```python
@staticmethod
async def new_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /new command"""
    await update.message.reply_text("Yeni əmr!")
```

2. `bot_enhanced.py` faylında handler-ı əlavə edin:
```python
self.application.add_handler(CommandHandler("new", MessageHandlers.new_command))
```

### Yeni funksionallıq əlavə etmək

- `handlers.py` faylında yeni class-lar yaradın
- API inteqrasiyaları üçün ayrı modullar əlavə edin
- Database inteqrasiyası üçün models əlavə edin

## 🐛 Problemlərin həlli

### Bot işləmir
1. `.env` faylında token düzgün təyin edilibmi?
2. Virtual environment aktivdir?
3. Bütün asılılıqlar quraşdırılıb?

### Import xətası
```bash
pip install -r requirements.txt
```

### Token xətası
1. @BotFather-dan yeni token əldə edin
2. `.env` faylında token-ı yeniləyin

## 📝 Loglar

Bot işləyərkən console-da logları görə bilərsiniz. Log səviyyəsini `config.py` faylında dəyişə bilərsiniz.

## 🤝 Töhfə

1. Layihəni fork edin
2. Feature branch yaradın (`git checkout -b feature/amazing-feature`)
3. Dəyişiklikləri commit edin (`git commit -m 'Add amazing feature'`)
4. Branch-i push edin (`git push origin feature/amazing-feature`)
5. Pull Request yaradın

## 📄 Lisenziya

Bu layihə MIT lisenziyası altında yayımlanır.

## 📞 Əlaqə

Hər hansı sual və ya təklif üçün:
- GitHub Issues istifadə edin
- Email: your-email@example.com

---

# 🤖 Telegram Bot v2 (English)

This project is a powerful and extensible Telegram bot environment.

## 🌟 Features

- **Modular structure** - Easy code organization and extension
- **Asynchronous architecture** - High performance
- **Inline keyboards** - Interactive user interface
- **Error handling** - Comprehensive error management
- **Logging system** - System logs
- **Multi-language support** - Azerbaijani and English support

## 📋 Requirements

- Python 3.8+
- pip (Python package manager)

## 🚀 Installation

### 1. Clone the project
```bash
git clone <repository-url>
cd botv2
```

### 2. Create virtual environment (recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get Telegram Bot Token
1. Contact [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` command
3. Set name and username for your bot
4. Copy the bot token

### 5. Create environment file
```bash
# Create .env file
cp env_example.txt .env
```

Edit `.env` file and add your bot token:
```env
TELEGRAM_BOT_TOKEN=your_actual_bot_token_here
```

## 🎯 Usage

### Run basic bot
```bash
python bot.py
```

### Run enhanced bot
```bash
python bot_enhanced.py
```

## 📚 Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and show welcome message |
| `/help` | Show help information |
| `/info` | Show detailed bot information |
| `/echo <text>` | Echo the sent text |
| `/weather` | Weather information (coming soon) |
| `/translate <text>` | Translate text (coming soon) |

## 🏗️ Project Structure

```
botv2/
├── bot.py                 # Main bot file
├── bot_enhanced.py        # Enhanced bot
├── handlers.py            # Message and command handlers
├── config.py              # Configuration file
├── requirements.txt       # Python dependencies
├── env_example.txt        # Environment variables example
└── README.md             # This file
```

## 🔧 Configuration

You can modify bot parameters in `config.py`:

- Bot name and description
- Logging level
- Database configuration
- Webhook URL (for production)

## 🚀 Extension

### Adding new commands

1. Create new function in `handlers.py`:
```python
@staticmethod
async def new_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /new command"""
    await update.message.reply_text("New command!")
```

2. Add handler in `bot_enhanced.py`:
```python
self.application.add_handler(CommandHandler("new", MessageHandlers.new_command))
```

### Adding new functionality

- Create new classes in `handlers.py`
- Add separate modules for API integrations
- Add models for database integration

## 🐛 Troubleshooting

### Bot not working
1. Is token correctly set in `.env` file?
2. Is virtual environment active?
3. Are all dependencies installed?

### Import error
```bash
pip install -r requirements.txt
```

### Token error
1. Get new token from @BotFather
2. Update token in `.env` file

## 📝 Logs

You can see logs in console while bot is running. You can change log level in `config.py`.

## 🤝 Contributing

1. Fork the project
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push branch (`git push origin feature/amazing-feature`)
5. Create Pull Request

## 📄 License

This project is licensed under MIT License.

## 📞 Contact

For any questions or suggestions:
- Use GitHub Issues
- Email: your-email@example.com

