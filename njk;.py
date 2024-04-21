import telebot

bot = telebot.TeleBot('7082948748:AAHPPyUqaDdO6FO4ufzE9qWbrqJfu6GyWjc')


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = 'dataset/1.jpg'
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Курит')



bot.polling()