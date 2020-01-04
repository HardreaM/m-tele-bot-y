import telebot
import pyowm


temp_list = []

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('/weather', '/help')

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id,
	 'Чтобы узнать погоду используйте команду /weather и следуйте инструкции')

@bot.message_handler(commands=['weather'])
def send_welcome(message):
	msg = bot.reply_to(message, "Здравствуйте, чтобы узнать погоду, укажите свой город.")
	bot.register_next_step_handler(msg, weather_forecast)


def weather_forecast(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = 'В городе ' + message.text + ' сейчас ' + w.get_detailed_status() + '\n'
    answer += 'Температура сейчас в районе ' + str(temp)

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop='true')
