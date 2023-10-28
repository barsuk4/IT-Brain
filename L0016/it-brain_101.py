from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Updater
import sqlite3

# Ініціалізація бази даних
def init_db():
    connection = sqlite3.connect("finances.db")
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        type TEXT,
        category TEXT,
        amount REAL,
        date TEXT
    )
    ''')
    
    connection.commit()
    connection.close()

# Додати транзакцію
def add_transaction(type_, category, amount):
    connection = sqlite3.connect("finances.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, date('now'))", (type_, category, amount))

    connection.commit()
    connection.close()

# Основні команди бота
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Вітаємо в фінансовому боті! Ви можете додавати або переглядати свої транзакції.')

def add_expense(update: Update, context: CallbackContext) -> None:
    try:
        category = context.args[0]
        amount = float(context.args[1])
        add_transaction('expense', category, amount)
        update.message.reply_text(f'Витрату {amount} у категорії {category} додано.')
    except (IndexError, ValueError):
        update.message.reply_text('Використовуйте: /add_expense <категорія> <сума>')

def categories(update: Update, context: CallbackContext) -> None:
    categories = ['житло', 'їжа', 'транспорт', 'розваги', 'інше']
    update.message.reply_text('\n'.join(categories))

# ... Тут повинні бути інші обробники команд

def main() -> None:
    init_db()
    TOKEN = 'YOUR_TELEGRAM_TOKEN'
    # Вставте свій TOKEN від @BotFather
    # bot = Bot(token=TOKEN)
    # updater = Updater(bot=bot)
    
    
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("add_expense", add_expense, pass_args=True))
    dp.add_handler(CommandHandler("categories", categories))
    # ... Додайте інші команди

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
