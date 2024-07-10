from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from PIL import Image
import os

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    disclaimer_text = (
        "Disclaimer\n\n"
        "Kami menghargai privasi dan keamanan data pengguna. Oleh karena itu, kami ingin menyatakan bahwa semua data yang "
        "dimasukkan oleh pengguna tidak akan disimpan secara permanen. Semua data yang diolah oleh bot kami disimpan dalam "
        "folder sementara dan akan dihapus segera setelah proses selesai.\n"
        "Kami tidak menyimpan data pengguna dalam jangka panjang atau melakukan pencatatan data untuk keperluan apapun.\n\n"
        "Terima kasih atas kepercayaan Anda.\n\n"
        "©AtaLioMego™-2024\n\n"
        "Selamat datang! Silakan upload gambar jpg/jpeg yang ingin diresize."
    )
    update.message.reply_text(disclaimer_text)

def handle_photo(update: Update, context: CallbackContext) -> None:
    photo_file = update.message.photo[-1].get_file()
    file_path = photo_file.download()
    if file_path.endswith(('.jpg', '.jpeg')):
        context.user_data['photo_path'] = file_path
        keyboard = [
            [InlineKeyboardButton("300kb", callback_data='300')],
            [InlineKeyboardButton("500kb", callback_data='500')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Pilih ukuran file yang diinginkan:', reply_markup=reply_markup)
    else:
        update.message.reply_text('File yang diupload bukan format jpg/jpeg. Silakan upload ulang.')

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    size = int(query.data)
    photo_path = context.user_data.get('photo_path')

    if photo_path:
        img = Image.open(photo_path)
        img_format = img.format
        output_path = f'FioreProject-{os.path.basename(photo_path)}'
        
        img.save(output_path, format=img_format, optimize=True, quality=85)
        
        while os.path.getsize(output_path) > size * 1024:
            img = Image.open(output_path)
            img.save(output_path, format=img_format, optimize=True, quality=img.info['quality'] - 5)
        
        with open(output_path, 'rb') as f:
            query.message.reply_document(f, filename=os.path.basename(output_path))
        
        os.remove(output_path)
        os.remove(photo_path)
    else:
        query.message.reply_text('Terjadi kesalahan, silakan upload gambar ulang.')

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
