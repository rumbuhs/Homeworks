import telebot
from telebot import types

bot = telebot.TeleBot('1409322116:AAGEKr23h8J-5jqddxwLeQiysUHBXsSD7ag')


@bot.message_handler(commands=['website'])
def open_website(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://career.softserveinc.com/uk-ua/it-academy"))
	bot.send_message(message.chat.id,
			"Гарний вибір, нажми на кнопку і обирай навчання відповідно до своїх знань",
			parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['insta'])
def instagram(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти в Інстаграм", url="https://www.instagram.com/softserve_career/?hl=uk"))
	bot.send_message(message.chat.id, "Нажми на кнопку нижче і погрузись в світ IT прямо зараз", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['facebook'])
def facebook(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Долучайся до групи у FB", url="https://www.facebook.com/SoftServeInc/?hc_ref=ARQ9f9osWH_tsNISuov4ll5KtWZwXJKnBasU6S_2xzGIZPTDCbBqr9D6qxi3RPl95TA&fref=nf&__tn__=kC-R"))
	bot.send_message(message.chat.id, "Долучайся до нашої групи у FB", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('Не знаю свого рівня')
	btn2 = types.KeyboardButton('Немає знань')
	btn3 = types.KeyboardButton('Базові знання')
	btn4 = types.KeyboardButton('Бракує практики')
	btn5 = types.KeyboardButton('Готовий до роботи')
	btn6 = types.KeyboardButton('Не заню англійської')
	markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
	send_mess = f"<b>Привіт {message.from_user.first_name} {message.from_user.last_name}</b>!\nВибери свій рівень знань Python:"
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

	if get_message_bot == "вибрати інший":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Не знаю свого рівня')
		btn2 = types.KeyboardButton('Немає знань')
		btn3 = types.KeyboardButton('Базові знання')
		btn4 = types.KeyboardButton('Бракує практики')
		btn5 = types.KeyboardButton('Готовий до роботи')
		btn6 = types.KeyboardButton('Бракує рівня англійської')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

		final_message = "Підівчив? \nВибери свій рівень знань Python:"
	elif get_message_bot == "не знаю свого рівня":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		markup.add(types.InlineKeyboardButton("вибрати інший", url="https://itproger.com/test/python"))
		final_message = "Щоб дізнатись свій рівень <a href='https://itproger.com/test/python'>itproger</a>\nпройди тест"
	elif get_message_bot == "немає знань":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		markup.add(types.InlineKeyboardButton("вибрати інший", url="https://itproger.com/test/python"))
		final_message = "Щоб отримати базові знання <a href='https://career.softserveinc.com/uk-ua/technology/course/python_core'>SoftServe</a>\nпройди курс"
	elif get_message_bot == "базові знання":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		markup.add(types.InlineKeyboardButton("вибрати інший", url="https://itproger.com/test/python"))
		final_message = "Конвертуй знання у вміння <a href='https://career.softserveinc.com/uk-ua/technology/course/python_online_marathon'>SoftServe</a>\nпід час інтенсивного онлайн-марафону з кодування на Python"
	elif get_message_bot == "бракує практики":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		markup.add(types.InlineKeyboardButton("вибрати інший", url="https://itproger.com/test/python"))
		final_message = "Отримуй перший досвід роботи <a href='https://career.softserveinc.com/uk-ua/technology/course/become_python_developer'>SoftServe</a>\nу глобальній ІТ-компанії"
	elif get_message_bot == "готовий до роботи":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		markup.add(types.InlineKeyboardButton("вибрати інший", url="https://itproger.com/test/python"))
		final_message = "Конвертуй знання у шанс! <a href='https://career.softserveinc.com/uk-ua/certification/63-python-integration/detail'>SoftServe</a>\nУспіхів!"
	elif get_message_bot == "бракує рівня англійської":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		markup.add(types.InlineKeyboardButton("вибрати інший", url="https://itproger.com/test/python"))
		final_message = "Дізнайся свій рівень англійської <a href='https://www.britishcouncil.org.ua/english/learn-online/test'>britishcouncil</a>\nтут"



	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Не знаю свого рівня')
		btn2 = types.KeyboardButton('Немає знань')
		btn3 = types.KeyboardButton('Базові знання')
		btn4 = types.KeyboardButton('Бракує практики')
		btn5 = types.KeyboardButton('Готовий до роботи')
		btn6 = types.KeyboardButton('Бракує рівня англійської')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
		final_message = "Щось пішло не так\nКраще нажми на одну з інтерактивних кнопок. \nА для пошуку нас у соцмережаш, введи наступні команди /website, /insta, /facebook"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True, interval=0)