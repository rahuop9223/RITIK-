from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = "8524089850:AAHR65Ha6gvEs_0wOM6PC4oWnSmYaodAtEM"
# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! मैं rahubotzzowner हूँ 🤖\nकुछ भी लिखो, मैं जवाब दूँगा!"
    )
# हर message पर auto-reply
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    reply = f"आपने लिखा: {user_text}\n\nमैं एक Auto Reply Bot हूँ!"
    await update.message.reply_text(reply)
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
print("Bot running...")
app.run_polling()
