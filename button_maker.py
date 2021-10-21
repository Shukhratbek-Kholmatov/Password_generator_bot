from telebot import types
def make_button(button):
    if button=="main_button":
        button=types.ReplyKeyboardMarkup(selective=True,resize_keyboard=True)
        button.row("🔒Sodda","🔒O'rta")
        button.row("🔒Murakkab")
    elif button=="button1":
        button=types.ReplyKeyboardMarkup(selective=True,resize_keyboard=True)
        button.row("🔒Sodda▫️","🔒O'rta")
        button.row("🔒Murakkab")
    elif button=="button2":
        button=types.ReplyKeyboardMarkup(selective=True,resize_keyboard=True)
        button.row("🔒Sodda","🔒O'rta▫️")
        button.row("🔒Murakkab")
    elif button=="button3":
        button=types.ReplyKeyboardMarkup(selective=True,resize_keyboard=True)
        button.row("🔒Sodda","🔒O'rta")
        button.row("🔒Murakkab▫️")
    return button
        
        
        