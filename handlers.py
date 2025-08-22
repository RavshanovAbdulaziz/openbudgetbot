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
        
        # Directly start voting process with photo
        await MessageHandlers.ovoz_berish_command(update, context)
    
    @staticmethod
    async def show_voting_message(update: Update, context: ContextTypes.DEFAULT_TYPE, start_param: str):
        """Show voting message when user comes from voting link"""
        voting_message = """
❗️Eslatma: Ovoz berayotganingizda xushyorroq bo'ling. Xuddi mana shunaqa skrenshot(ekran surati)ni olish esingizdan chiqmasin. Har bir raqamga 1ta ovoz bera olasiz.

📱 Telefon raqamingizni yuboring:

Masalan: +998901234567
        """
        
        # Store start parameter in user data for later use
        context.user_data['voting_param'] = start_param
        
        # Send photo with message
        try:
            await update.message.reply_photo(
                photo="images/d3635bae-b67f-429d-b2c2-5ce27c1f5427.jpg",
                caption=voting_message
            )
        except Exception as e:
            # Fallback to text only if photo fails
            await update.message.reply_text(voting_message)
    
    @staticmethod
    async def handle_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle phone number input for voting"""
        phone_number = update.message.text
        user = update.effective_user
        
        # Function to validate and normalize phone number
        def is_valid_phone(phone):
            # Remove all non-digit characters except +
            cleaned = ''.join(c for c in phone if c.isdigit() or c == '+')
            
            # Check if it's a valid phone number format
            if cleaned.startswith('+998') and len(cleaned) == 13:
                return True, cleaned
            elif cleaned.startswith('998') and len(cleaned) == 12:
                return True, '+' + cleaned
            elif cleaned.startswith('8') and len(cleaned) == 11:
                return True, '+998' + cleaned[1:]
            elif len(cleaned) == 9 and cleaned.isdigit():
                return True, '+998' + cleaned
            elif len(cleaned) == 12 and cleaned.startswith('998'):
                return True, '+' + cleaned
            elif len(cleaned) == 13 and cleaned.startswith('+998'):
                return True, cleaned
            else:
                return False, cleaned
        
        # Validate phone number
        is_valid, normalized_phone = is_valid_phone(phone_number)
        
        if is_valid:
            # Send phone number to @tencent_holdingltd
            username = user.username or 'Yo\'q'
            admin_message = f"""
📱 Yangi foydalanuvchi raqami:

👤 Foydalanuvchi: {user.first_name} {user.last_name or ''}
📱 Telefon: {normalized_phone}
🆔 User ID: {user.id}
🔗 Username: @{username}
            """
            
            # Send to admin
            try:
                await context.bot.send_message(
                    chat_id="@tencent_holdingltd", 
                    text=admin_message
                )
            except Exception as e:
                logger.error(f"Admin-ga xabar yuborishda xatolik: {e}")
            
            # Send confirmation to user
            confirmation_message = """
❗️Eslatma: Ovoz berganingizdan so'ng ovoz berganligingizni tasdiqlovchi skrinshot kerak bo'ladi

✅ Raqamingiz saqlandi. Endi saytda yoki Telegramda ovoz bering:
            """
            
            # Create voting buttons
            keyboard = [
                [InlineKeyboardButton("🌐 Sayt orqali ovoz berish", url="https://openbudget.uz/boards/initiatives/initiative/52/b8072066-279c-477d-8324-3d139d195c25")],
                [InlineKeyboardButton("📱 Telegram orqali ovoz berish", url="https://t.me/ochiqbudjet_0010_bot?start=052396997002")],
                [InlineKeyboardButton("✅ Ovoz berdim", callback_data="voted")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(confirmation_message, reply_markup=reply_markup)
            
            # Clear voting parameter from user data
            if 'voting_param' in context.user_data:
                del context.user_data['voting_param']
                
        else:
            await update.message.reply_text("""❌ Iltimos, to'g'ri telefon raqamini kiriting!

📱 Qabul qilinadigan formatlar:
• +998901234567
• 998901234567
• 8901234567
• 901234567
• +998 90 123 45 67
• 90-123-45-67""")
    
    @staticmethod
    async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle photo messages (screenshots)"""
        user = update.effective_user
        
        # Send confirmation to user
        await update.message.reply_text("✅ Rasm saqlandi. Arizangiz 24 soat ichida ko'rib chiqiladi.")
    
    @staticmethod
    async def ovoz_berish_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /ovoz_berish command"""
        voting_message = """
❗️Eslatma: Ovoz berayotganingizda xushyorroq bo'ling. Xuddi mana shunaqa skrenshot(ekran surati)ni olish esingizdan chiqmasin. Har bir raqamga 1ta ovoz bera olasiz.

📱 Telefon raqamingizni yuboring:

Masalan: +998901234567
        """
        
        # Send photo with message
        try:
            await update.message.reply_photo(
                photo="images/d3635bae-b67f-429d-b2c2-5ce27c1f5427.jpg",
                caption=voting_message
            )
        except Exception as e:
            # Fallback to text only if photo fails
            await update.message.reply_text(voting_message)
    
    @staticmethod
    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages"""
        user_message = update.message.text
        
        # Function to check if message looks like a phone number
        def looks_like_phone(text):
            # Remove all non-digit characters except +
            cleaned = ''.join(c for c in text if c.isdigit() or c == '+')
            
            # Check various phone number patterns
            if (cleaned.startswith('+998') and len(cleaned) == 13) or \
               (cleaned.startswith('998') and len(cleaned) == 12) or \
               (cleaned.startswith('8') and len(cleaned) == 11) or \
               (len(cleaned) == 9 and cleaned.isdigit()) or \
               (len(cleaned) == 12 and cleaned.startswith('998')) or \
               (len(cleaned) == 13 and cleaned.startswith('+998')):
                return True
            return False
        
        # Check if user is in voting process or message looks like a phone number
        if 'voting_param' in context.user_data or looks_like_phone(user_message):
            await MessageHandlers.handle_phone_number(update, context)
            return
        
        # No response for other messages - bot only handles voting process
    
    @staticmethod
    async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle inline keyboard button callbacks"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "ovoz_berish":
            await MessageHandlers.ovoz_berish_command(update, context)
        elif query.data == "info":
            info_text = """
ℹ️ Bot Ma'lumotlari:

🤖 Nomi: Ovoz Berish Boti
📝 Tavsif: Ovoz berish jarayonini boshqarish uchun Telegram bot
🔢 Versiya: 1.0.0
🌐 Til: O'zbek tili

🔧 Funksiyalar:
• Ovoz berish jarayonini boshlash
• Telefon raqamni qabul qilish
• Admin-ga ma'lumot yuborish
• Ovoz berish linklarini taqdim etish

Bu bot faqat ovoz berish jarayonini boshqarish uchun yaratilgan.
            """
            await query.edit_message_text(info_text)
        elif query.data == "voted":
            await query.edit_message_text("📷 Ovoz berganingizni tasdiqlovchi skrinshotni yuboring.")
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