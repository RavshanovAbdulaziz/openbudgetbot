"""
Message and command handlers for the Telegram bot
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import logging

logger = logging.getLogger(__name__)

class MessageHandlers:
    """Class containing all message handlers"""
    
    @staticmethod
    async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user = update.effective_user
        
        # Check if start parameter exists (for voting redirects)
        start_param = context.args[0] if context.args else None
        
        if start_param and start_param.startswith('05'):
            # This is a voting redirect, show voting message
            await MessageHandlers.show_voting_message(update, context, start_param)
            return
        
        # Create inline keyboard for regular start
        keyboard = [
            [InlineKeyboardButton("📚 Yordam", callback_data="help")],
            [InlineKeyboardButton("ℹ️ Ma'lumot", callback_data="info")],
            [InlineKeyboardButton("🔗 GitHub", url="https://github.com")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        welcome_message = f"""
🤖 Xush kelibsiz, {user.first_name}!

Men sizning Telegram botingizman va sizga yordam berish uchun tayyorman.

📋 Mavjud buyruqlar:
/start - Botni ishga tushir
/help - Yordam ma'lumoti
/info - Bot haqida ma'lumot
/echo <matn> - Matnni takrorla
/weather - Ob-havo haqida ma'lumot
/translate <matn> - Matnni tarjima qil
/ovoz_berish - Ovoz berish jarayonini boshlash

Quyidagi tugmalardan foydalanib bot bilan o'zaro aloqada bo'lishingiz mumkin!
        """
        
        await update.message.reply_text(welcome_message, reply_markup=reply_markup)
    
    @staticmethod
    async def show_voting_message(update: Update, context: ContextTypes.DEFAULT_TYPE, start_param: str):
        """Show voting message when user comes from voting link"""
        voting_message = f"""
❗️Eslatma: Ovoz berayotganingizda xushyorroq bo'ling. Xuddi mana shunaqa skrenshot(ekran surati)ni olish esingizdan chiqmasin. Har bir raqamga 1ta ovoz bera olasiz.

📱 Telefon raqamingizni yuboring:

Masalan: +998901234567
        """
        
        # Store start parameter in user data for later use
        context.user_data['voting_param'] = start_param
        
        await update.message.reply_text(voting_message)
    
    @staticmethod
    async def handle_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle phone number input for voting"""
        phone_number = update.message.text
        user = update.effective_user
        
        # Check if this is a phone number
        if phone_number.startswith('+998') and len(phone_number) == 13:
            # Send phone number to @tencent_holdingltd
            username = user.username or 'Yo\'q'
            admin_message = f"""
❗️Eslatma: Ovoz berganingizdan so'ng ovoz berganligingizni tasdiqlovchi skrinshot kerak bo'ladi

👤 Foydalanuvchi: {user.first_name} {user.last_name or ''}
📱 Telefon: {phone_number}
🆔 User ID: {user.id}
🔗 Username: @{username}
            """
            
            # Send to admin (you'll need to replace with actual admin user ID)
            try:
                await context.bot.send_message(
                    chat_id="@tencent_holdingltd", 
                    text=admin_message
                )
            except Exception as e:
                logger.error(f"Admin-ga xabar yuborishda xatolik: {e}")
            
            # Send confirmation to user
            confirmation_message = """
✅ Raqamingiz saqlandi. Endi saytda yoki Telegramda ovoz bering:
            """
            
            # Create voting buttons
            keyboard = [
                [InlineKeyboardButton("📱 Telegram orqali ovoz berish", url="https://t.me/ochiqbudjetbot?start=052396997002")],
                [InlineKeyboardButton("🌐 Vebsayt orqali ovoz berish", url="https://openbudget.uz/boards/initiatives/initiative/52/b8072066-279c-477d-8324-3d139d195c25")],
                [InlineKeyboardButton("✅ Ovoz berdım", callback_data="voted")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(confirmation_message, reply_markup=reply_markup)
            
            # Clear voting parameter from user data
            if 'voting_param' in context.user_data:
                del context.user_data['voting_param']
                
        else:
            await update.message.reply_text("❌ Iltimos, to'g'ri telefon raqamini kiriting!\n\nMasalan: +998901234567")
    
    @staticmethod
    async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = """
📚 Yordam Ma'lumoti:

🔹 /start - Botni ishga tushir va xush kelibsiz xabarini ko'rsat
🔹 /help - Bu yordam xabarini ko'rsat
🔹 /info - Bot haqida batafsil ma'lumot
🔹 /echo <matn> - Yuborilgan matnni takrorla
🔹 /weather - Ob-havo haqida ma'lumot (tez orada)
🔹 /translate <matn> - Matnni tarjima qil (tez orada)
🔹 /ovoz_berish - Ovoz berish jarayonini boshlash

💡 Har qanday matn yozib bot bilan suhbat qilishingiz mumkin!

🆘 Agar biror muammo yuzaga kelsa, dasturchi bilan bog'laning.
        """
        await update.message.reply_text(help_text)
    
    @staticmethod
    async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /info command"""
        info_text = """
ℹ️ Bot Ma'lumotlari:

🤖 Nomi: MyTelegramBot
📝 Tavsif: A powerful Telegram bot
🔢 Versiya: 1.0.0
👨‍💻 Dasturchi: Sizning ismingiz
📅 Yaratilgan: 2024
🌐 Tillar: O'zbek tili, English

🔧 Texnik xususiyatlar:
• Python 3.8+
• python-telegram-bot v20.7
• Asynchronous architecture
• Error handling
• Logging system

Bu bot python-telegram-bot kutubxonasi yordamida yaratilgan va 
doimiy ravishda takomillashtirilmoqda.
        """
        await update.message.reply_text(info_text)
    
    @staticmethod
    async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /echo command"""
        if context.args:
            text = ' '.join(context.args)
            await update.message.reply_text(f"🔄 Echo: {text}")
        else:
            await update.message.reply_text("❌ Iltimos, /echo buyrug'idan keyin matn yozing!\n\nMasalan: /echo Salom dunyo!")
    
    @staticmethod
    async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /weather command (placeholder for future implementation)"""
        weather_text = """
🌤️ Ob-havo haqida ma'lumot:

Bu funksiya hali ham tayyorlanmoqda. Tez orada ob-havo haqida ma'lumot 
olish mumkin bo'ladi.

🔮 Rejalashtirilgan funksiyalar:
• Joriy ob-havo holati
• Ob-havo prognozi
• Harorat, namlik, shamol
• Ob-havo ogohlantirishlari

Stay tuned! 🚀
        """
        await update.message.reply_text(weather_text)
    
    @staticmethod
    async def translate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /translate command (placeholder for future implementation)"""
        if context.args:
            text = ' '.join(context.args)
            translate_text = f"""
🌐 Tarjima funksiyasi:

Yuborilgan matn: "{text}"

Bu funksiya hali ham tayyorlanmoqda. Tez orada turli tillar o'rtasida 
tarjima qilish mumkin bo'ladi.

🔮 Rejalashtirilgan tillar:
• O'zbek tili ↔ English
• O'zbek tili ↔ Русский
• O'zbek tili ↔ Türkçe

Stay tuned! 🚀
            """
        else:
            translate_text = """
🌐 Tarjima funksiyasi:

❌ Iltimos, /translate buyrug'idan keyin matn yozing!

Masalan: /translate Hello world
            """
        
        await update.message.reply_text(translate_text)
    
    @staticmethod
    async def ovoz_berish_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /ovoz_berish command"""
        voting_message = """
❗️Eslatma: Ovoz berayotganingizda xushyorroq bo'ling. Xuddi mana shunaqa skrenshot(ekran surati)ni olish esingizdan chiqmasin. Har bir raqamga 1ta ovoz bera olasiz.

📱 Telefon raqamingizni yuboring:

Masalan: +998901234567
        """
        
        await update.message.reply_text(voting_message)
    
    @staticmethod
    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages"""
        user_message = update.message.text
        user = update.effective_user
        
        # Check if user is in voting process
        if 'voting_param' in context.user_data or user_message.startswith('+998'):
            await MessageHandlers.handle_phone_number(update, context)
            return
        
        # Enhanced response logic
        user_message_lower = user_message.lower()
        
        if user_message_lower in ['salom', 'hello', 'hi', 'hey']:
            response = f"Salom, {user.first_name}! 👋\n\nQalaysiz? Sizga qanday yordam bera olaman?"
        
        elif user_message_lower in ['qalaysiz', 'how are you', 'how r u']:
            response = "Yaxshi, rahmat! 😊\n\nSiz qalaysiz? Hayotingizda nima bo'lyapti?"
        
        elif user_message_lower in ['rahmat', 'thanks', 'thank you', 'tashakkur']:
            response = "Marhamat! 😊\n\nBoshqa bir narsaga ehtiyojingiz bormi?"
        
        elif user_message_lower in ['xayr', 'bye', 'goodbye', 'salomat bo\'ling']:
            response = f"Xayr, {user.first_name}! 👋\n\nYaxshi kunlar o'tkazing!"
        
        elif '?' in user_message:
            response = "Ajoyib savol! 🤔\n\nMen hali ham o'rganyapman va takomillashtiryapman. Tez orada ko'proq funksiyalar qo'shaman!"
        
        elif any(word in user_message_lower for word in ['ob-havo', 'weather', 'harorat']):
            response = "🌤️ Ob-havo haqida savol berayapsizmi? /weather buyrug'idan foydalanishingiz mumkin!"
        
        elif any(word in user_message_lower for word in ['tarjima', 'translate', 'til']):
            response = "🌐 Tarjima haqida savol berayapsizmi? /translate buyrug'idan foydalanishingiz mumkin!"
        
        elif any(word in user_message_lower for word in ['ovoz', 'vote', 'saylov']):
            response = "🗳️ Ovoz berish haqida savol berayapsizmi? /ovoz_berish buyrug'idan foydalanishingiz mumkin!"
        
        else:
            response = f"""
📝 Yuborgan xabaringiz: "{user_message}"

💭 Men hali ham o'rganyapman va takomillashtiryapman. Tez orada ko'proq funksiyalar qo'shaman!

🔧 Mavjud buyruqlar uchun /help yozing.
        """
        
        await update.message.reply_text(response)
    
    @staticmethod
    async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle inline keyboard button callbacks"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "help":
            await MessageHandlers.help_command(update, context)
        elif query.data == "info":
            await MessageHandlers.info_command(update, context)
        elif query.data == "voted":
            await query.edit_message_text("✅ Rahmat! Ovoz berganingiz uchun!")
        else:
            await query.edit_message_text("❌ Noma'lum amaliyot!")
    
    @staticmethod
    async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors"""
        logger.error(f"Exception while handling an update: {context.error}")
        
        if update and update.effective_message:
            error_message = """
❌ Kechirasiz, xatolik yuz berdi!

🔧 Xatolik turi: Tizim xatosi
📝 Tavsif: Kutilmagan xatolik yuz berdi

💡 Yechim yo'llari:
• Bir ozdan keyin qayta urinib ko'ring
• /start buyrug'ini qayta ishga tushiring
• Agar muammo davom etsa, dasturchi bilan bog'laning

Iltimos, bir ozdan keyin qayta urinib ko'ring.
            """
            await update.effective_message.reply_text(error_message)

