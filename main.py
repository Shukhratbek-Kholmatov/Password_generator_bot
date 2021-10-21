import telebot
from button_maker import make_button
from generate_function import generate
from config import token
bot=telebot.TeleBot(token,parse_mode="MARKDOWN")
@bot.message_handler(commands=["start"])
def start(message):
    main_button=make_button("main_button")
    user=message.from_user
    bot.send_message(message.chat.id,f"Assalomu alaykum *{format(user.first_name)}.*\nParol darajasini tanlang.",reply_markup=main_button)
@bot.message_handler(content_types=["text"]) 
def text(message):
    mid=message.chat.id
    msg=message.text
    main_button=make_button("main_button")
    button1=make_button("button1")
    button2=make_button("button2") 
    button3=make_button("button3")
    if msg=="🔒Sodda":
            with open(f"user_info/{mid}.txt","w") as file:
                file.write("Sodda")
            bot.send_message(message.chat.id,f"Parol uzunligini kiriting:",reply_markup=button1)
        
    elif msg=="🔒O'rta":
            with open(f"user_info/{mid}.txt","w") as file:
                file.write("O'rta")
            bot.send_message(message.chat.id,f"Parol uzunligini kiriting:",reply_markup=button2)
        
    elif msg=="🔒Murakkab":
            with open(f"user_info/{mid}.txt","w") as file:
                file.write("Murakkab")
            bot.send_message(message.chat.id,f"Parol uzunligini kiriting:",reply_markup=button3) 
    elif msg!="🔒Sodda" and msg!="🔒O'rta" and msg!="🔒Murakkab":
        try:
            with open(f"user_info/{mid}.txt","r") as detect:
                read=detect.readlines()
                if "Sodda" in read:
                    text=int(msg)
                    response=generate("easy",text)
                    bot.send_message(mid,response,reply_markup=button1)
                elif "O'rta" in read:
                    text=int(msg)
                    response=generate("middle",text)
                    bot.send_message(mid,response,reply_markup=button2)
                elif "Murakkab" in read:
                    text=int(msg)
                    response=generate("strong",text)
                    bot.send_message(mid,response,reply_markup=button3)
                else:
                        bot.send_message(mid,"Parol darajasini tanlang",reply_markup=main_button)
                        
                        
        except:
            bot.send_message(mid,"Parol darajasini tanlang",reply_markup=main_button)
            

bot.polling(none_stop=True)    