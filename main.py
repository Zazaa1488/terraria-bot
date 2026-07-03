from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "ВСТАВЬ_СЮДА_ТОКЕН"

DATA = {
    "warrior_pre": {
        "title": "⚔ Воин (Pre-Hardmode)",
        "image": "https://terraria.wiki.gg/images/thumb/Platinum_armor.png",
        "text": "🛡 Platinum/Gold Armor\n⚔ Night's Edge\n🧪 Ironskin\n👾 Eye of Cthulhu"
    }
}

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⚔ Воин", callback_data="warrior")]
    ])

def warrior_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Pre-Hardmode", callback_data="warrior_pre")],
        [InlineKeyboardButton("⬅ Назад", callback_data="home")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Terraria Guide Bot", reply_markup=main_menu())

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "home":
        await q.message.edit_text("🎮 Terraria Guide Bot", reply_markup=main_menu())

    elif q.data == "warrior":
        await q.message.edit_text("⚔ Воин", reply_markup=warrior_menu())

    elif q.data == "warrior_pre":
        item = DATA["warrior_pre"]
        await q.message.reply_photo(
            photo=item["image"],
            caption=f"{item['title']}\n\n{item['text']}",
            reply_markup=warrior_menu()
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
