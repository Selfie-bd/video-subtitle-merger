from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Help(object):

    HELP_USER = "??"

    HELP_TEXT =" Ask Here @FlimRequest"

    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 About', callback_data='about'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    )
