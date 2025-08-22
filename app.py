#!/usr/bin/env python3
"""
Simple Telegram bot for voting functionality
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from config import Config
from handlers import MessageHandlers

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, Config.LOG_LEVEL)
)
logger = logging.getLogger(__name__)

def main():
    """Main function to run the bot"""
    try:
        # Create bot application
        bot_application = Application.builder().token(Config.TELEGRAM_BOT_TOKEN).build()
        
        # Command handlers
        bot_application.add_handler(CommandHandler("start", MessageHandlers.start_command))
        bot_application.add_handler(CommandHandler("ovoz_berish", MessageHandlers.ovoz_berish_command))
        
        # Message handler for all text messages
        bot_application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, MessageHandlers.handle_message))
        
        # Photo handler for screenshots
        bot_application.add_handler(MessageHandler(filters.PHOTO, MessageHandlers.handle_photo))
        
        # Callback query handler for inline keyboards
        bot_application.add_handler(CallbackQueryHandler(MessageHandlers.callback_query_handler))
        
        # Error handler
        bot_application.add_error_handler(MessageHandlers.error_handler)
        
        logger.info("Bot ilovasi muvaffaqiyatli ishga tushirildi")
        
        # Start polling
        bot_application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"Bot ishga tushirishda xatolik: {e}")
        raise

if __name__ == '__main__':
    try:
        # Validate configuration
        Config.validate()
        
        # Run the bot
        main()
        
    except Exception as e:
        logger.error(f"Ilova ishga tushirishda xatolik: {e}")
        exit(1)

