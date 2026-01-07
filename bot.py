from telegram import Update, Poll
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "PASTE_YOUR_TOKEN_HERE"

questions = [
    ("Paris Olympics 2024 ka official motto kya tha?",
     ["Games Wide Open", "Unity in Sports", "One World", "Together We Can"], 0),
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏅 Welcome to Paris Olympics Quiz Bot 🏅\n\n/quiz likho quiz start karne ke liye"
    )

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = random.choice(questions)
    await context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question=q[0],
        options=q[1],
        type=Poll.QUIZ,
        correct_option_id=q[2],
        is_anonymous=False
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quiz", quiz))

app.run_polling()
