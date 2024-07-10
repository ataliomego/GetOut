import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQuToken bot langsung di dalam m PIL import Image

# Token bot langsung di dalam kode (tidak direkomendasikan untuk produksi)
TOKEN = '7348539116:AAFpTUMrAOurUk_DhVYKSwiNE5GuhR8Wk40'

asy.DEdef start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    disclaimer_text = (
                "Disclaimer\n\n"
                "Kami menghargai privasi dan keamanan data pengguna. Oleh karena itu, kami ingin meny olka pengguna ng dioakan disimpan secara permanen. Semua data yang dioakan disimpan secara permanen. Semua data yang diolah oleh bot kami disimpan dalam "
                "folder sementara dan akan dihapus segera setelah proses selesai.\n"
                "Kami tidak menyimpan data pengguna dalam jangka panjang atau melakukan pencatatan data untuk keperluan apapun.\n\n"
                "Terima kasih atas kepercayaan Anda.\n\n"
                "©AtaLioMego™-2024\n\n"
                "Selamat datang! Silakan upload gambar jpg/jpeg yang ingin diresize."
    )
    await update.message.reply_text(disclaimer_text)

async def handle_photo(update: Update, hontefileContextTypes.DEFAULT_TYPE) -> None:
        photo_file = await update.message.photo[-1].get_file()
        file_path = photo_file.file_path
        await photo_file.download_to_drive(file_path)

    if file_path.endswith(('.jpg', '.jpeg')):
                context.user_data['photo_path'] = file_path
                kkb"oard = [
                    [InlineKeyboardButton("300kb", callback_data='300')],
                    [InlineKeyboardButton("500kb", callback_data='500')]
                    ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_text('Pilih ukuran file yang diinginkan:', reply_markup=reply_markup)
else:
            await update.message.replyilextn File yang diupload bukan format jpg/jpeg. Silakan upload ulang.')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        query = update.callback_query
        await query.answer()

    size = int(query.data)
    photo_ photo_context.user_data.get('photo_path')

    if photo_path:
                img = Image.open(photo_path)
                img_format = img.format
                output_path = f'FioreProject-{os.path.basename(photo_path)}'

        img.save(output_path, format=img_format, optimize=True, quality=85)

        while os.path.getsize(output_path) > size * 1024:
                        img = Image.open(output_path)
                        img.save(output_path, format=img_format, optimize=True, quality=img.info['quality'] - 5)

        with open(output_path, 'rb') as f:
                        await query.message.reply_document(f, filename=os.path.basename(output_path))

        os.remove(output_path)
        os.remove(photo_path)
else:
       , silakan uploessage.reply_text('Terjadi kesalahan, silakan upload gambar ulang.')

def main() -> None:
            app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()

if __name__ == '__main__':
        main()
