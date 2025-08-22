#!/usr/bin/env python3
"""
Flask app wrapper for Telegram bot webhook handling
"""

import os
import logging
from flask import Flask, request, jsonify
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

# Initialize Flask app
app = Flask(__name__)

# Initialize bot application
bot_application = None

# API Configuration from environment variables
API_PREFIX = os.getenv('API_PREFIX', '')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID', '@tencent_holdingltd')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')
BOT_NAME = os.getenv('BOT_NAME', 'Ovoz Berish Boti')
BOT_VERSION = os.getenv('BOT_VERSION', '1.0.0')

def initialize_bot():
    """Initialize the Telegram bot application"""
    global bot_application
    
    try:
        bot_application = Application.builder().token(Config.TELEGRAM_BOT_TOKEN).build()
        
        # Command handlers
        bot_application.add_handler(CommandHandler("start", MessageHandlers.start_command))
        bot_application.add_handler(CommandHandler("help", MessageHandlers.help_command))
        bot_application.add_handler(CommandHandler("info", MessageHandlers.info_command))
        bot_application.add_handler(CommandHandler("echo", MessageHandlers.echo_command))
        bot_application.add_handler(CommandHandler("weather", MessageHandlers.weather_command))
        bot_application.add_handler(CommandHandler("translate", MessageHandlers.translate_command))
        bot_application.add_handler(CommandHandler("ovoz_berish", MessageHandlers.ovoz_berish_command))
        
        # Message handler for all text messages
        bot_application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, MessageHandlers.handle_message))
        
        # Callback query handler for inline keyboards
        bot_application.add_handler(CallbackQueryHandler(MessageHandlers.callback_query_handler))
        
        # Error handler
        bot_application.add_error_handler(MessageHandlers.error_handler)
        
        logger.info("Bot ilovasi muvaffaqiyatli ishga tushirildi")
        
    except Exception as e:
        logger.error(f"Bot ilovasini ishga tushirishda xatolik: {e}")
        raise

@app.route('/')
def health_check():
    """Health check endpoint for Railway"""
    return jsonify({
        "status": "sog'lom",
        "bot": os.getenv('BOT_NAME', 'Ovoz Berish Boti'),
        "version": os.getenv('BOT_VERSION', '1.0.0'),
        "status_code": 200,
        "xabar": "Bot muvaffaqiyatli ishlayapti",
        "environment": os.getenv('ENVIRONMENT', 'production')
    })

@app.route(f'{API_PREFIX}/webhook', methods=['POST'])
def webhook():
    """Handle incoming webhook requests from Telegram"""
    try:
        if bot_application is None:
            return jsonify({"xatolik": "Bot ishga tushirilmagan"}), 500
        
        # Get the update from Telegram
        update = Update.de_json(request.get_json(), bot_application.bot)
        
        # Process the update
        bot_application.process_update(update)
        
        return jsonify({"status": "ok"}), 200
        
    except Exception as e:
        logger.error(f"Webhook xatosi: {e}")
        return jsonify({"xatolik": str(e)}), 500

@app.route(f'{API_PREFIX}/setwebhook', methods=['GET'])
def set_webhook():
    """Set webhook URL for the bot"""
    try:
        if bot_application is None:
            return jsonify({"xatolik": "Bot ishga tushirilmagan"}), 500
        
        # Get Railway public URL
        railway_url = os.getenv('RAILWAY_PUBLIC_URL')
        if not railway_url:
            return jsonify({"xatolik": "RAILWAY_PUBLIC_URL o'rnatilmagan"}), 500
        
        webhook_url = f"{railway_url}{API_PREFIX}/webhook"
        
        # Set webhook
        success = bot_application.bot.set_webhook(url=webhook_url)
        
        if success:
            return jsonify({
                "status": "muvaffaqiyatli",
                "webhook_url": webhook_url,
                "xabar": "Webhook muvaffaqiyatli o'rnatildi"
            }), 200
        else:
            return jsonify({"xatolik": "Webhook o'rnatishda xatolik"}), 500
            
    except Exception as e:
        logger.error(f"Webhook o'rnatish xatosi: {e}")
        return jsonify({"xatolik": str(e)}), 500

@app.route(f'{API_PREFIX}/getwebhook', methods=['GET'])
def get_webhook():
    """Get current webhook info"""
    try:
        if bot_application is None:
            return jsonify({"xatolik": "Bot ishga tushirilmagan"}), 500
        
        webhook_info = bot_application.bot.get_webhook_info()
        return jsonify(webhook_info), 200
        
    except Exception as e:
        logger.error(f"Webhook ma'lumotini olish xatosi: {e}")
        return jsonify({"xatolik": str(e)}), 500

@app.route(f'{API_PREFIX}/deletewebhook', methods=['GET'])
def delete_webhook():
    """Delete webhook"""
    try:
        if bot_application is None:
            return jsonify({"xatolik": "Bot ishga tushirilmagan"}), 500
        
        success = bot_application.bot.delete_webhook()
        
        if success:
            return jsonify({
                "status": "muvaffaqiyatli",
                "xabar": "Webhook muvaffaqiyatli o'chirildi"
            }), 200
        else:
            return jsonify({"xatolik": "Webhook o'chirishda xatolik"}), 500
            
    except Exception as e:
        logger.error(f"Webhook o'chirish xatosi: {e}")
        return jsonify({"xatolik": str(e)}), 500

@app.route(f'{API_PREFIX}/status', methods=['GET'])
def bot_status():
    """Get bot status and information"""
    try:
        if bot_application is None:
            return jsonify({"xatolik": "Bot ishga tushirilmagan"}), 500
        
        bot_info = bot_application.bot.get_me()
        
        return jsonify({
            "status": "ishlayapti",
            "environment": ENVIRONMENT,
            "bot_ma'lumoti": {
                "id": bot_info.id,
                "nomi": bot_info.first_name,
                "username": bot_info.username,
                "guruhlarga_qo'shilishi_mumkin": bot_info.can_join_groups,
                "barcha_guruh_xabarlarini_o'qishi_mumkin": bot_info.can_read_all_group_messages,
                "inline_savollarni_qo'llab-quvvatlaydi": bot_info.supports_inline_queries
            },
            "webhook_ma'lumoti": bot_application.bot.get_webhook_info(),
            "api_prefix": API_PREFIX,
            "admin_chat_id": ADMIN_CHAT_ID
        }), 200
        
    except Exception as e:
        logger.error(f"Status xatosi: {e}")
        return jsonify({"xatolik": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"xatolik": "Endpoint topilmadi"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"xatolik": "Ichki server xatosi"}), 500

if __name__ == '__main__':
    try:
        # Validate configuration
        Config.validate()
        
        # Initialize bot
        initialize_bot()
        
        # Get port from environment (Railway sets this)
        port = int(os.getenv('PORT', 8000))
        
        # Run Flask app
        app.run(host='0.0.0.0', port=port, debug=False)
        
    except Exception as e:
        logger.error(f"Ilova ishga tushirishda xatolik: {e}")
        exit(1)

