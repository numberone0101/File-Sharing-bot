# (©)Codexbotz
# Recide by @Mafia_Tobatz
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Tentang Bot ini:\n\n • Owner: @{OWNER}\n • Channel: @{CHANNEL}\n • Group: @{GROUP}\n • Source Code: <a href='https://github.com/Zaen-ubot/File-Sharing'>Klik Disini</a></b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔅 ᴛᴜᴛᴜᴘ 🔅", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
