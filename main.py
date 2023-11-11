import os, random, re, logging          
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler, filters

#Basic logging funktion in the file log_file.log
logging.basicConfig(
    filename='log_file.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#get all images inside of the folder "Images"
file_list = os.listdir("Images")

async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function sends a random image from the 'Images' directory to the user.
    """
    logging.info("New Message:")
    logging.info(update.message.chat_id)

    try:
        photo_filename = random.choice(file_list)
        photo_path = os.path.join("Images", photo_filename)

        with open(photo_path, 'rb') as photo_file:
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_file)
    except Exception:
        logging.info("ERROR: " + photo_path)
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function sends a message to the user with information about the bot.
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="DemoImageBot says:\nThis text is shown when the command /about is sent."
    )
if __name__ == '__main__':
    # Create the Telegram bot application using the provided bot token
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
    application = ApplicationBuilder().token('YOUR_TELEGRAM_BOT_TOKEN').build()

    # Define the message handler for the 'message' event
    # Define keywords on which the bot will sen replies
    image_handler = MessageHandler(filters.Regex(re.compile(r'(Photo|Image)', re.IGNORECASE)), send_image)

    # Define the message handler for the 'command' event
    start_handler = CommandHandler('start', send_image)
    about_handler = CommandHandler('about', about)

    application.add_handler(image_handler)
    application.add_handler(start_handler)
    application.add_handler(about_handler)

    print("Bot is running...")
    application.run_polling()
