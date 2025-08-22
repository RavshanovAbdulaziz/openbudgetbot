import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Bot configuration class"""
    
    # Telegram Bot Token
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    # Webhook configuration
    WEBHOOK_URL = os.getenv('WEBHOOK_URL')
    
    # Database configuration
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot_database.db')
    
    # Logging configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Bot settings
    BOT_NAME = "Ovoz Berish Boti"
    BOT_DESCRIPTION = "Ovoz berish jarayonini boshqarish uchun Telegram bot"
    BOT_VERSION = "1.0.0"
    
    @classmethod
    def validate(cls):
        """Validate required configuration"""
        if not cls.TELEGRAM_BOT_TOKEN:
            raise ValueError("TELEGRAM_BOT_TOKEN is required in environment variables")
        return True

