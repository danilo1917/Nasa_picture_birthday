import telebot
import requests
import json
import ast

API_KEY = "5120220635:AAGIQ02_zWBvT2O6kudCcKLg2sYU7MbG2FY"
bot = telebot.TeleBot(API_KEY)

def retorna_foto(mensagem):
	data = mensagem.text
	nasa_api_key = "soLrRU1KzdE6hR5xVUXZL2yK39QWEhBQAz2nLDts"
	url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}&date={data}"
	try:
		response = requests.get(url)
		response = ast.literal_eval(response.text)
		print(response)
		bot.send_message(mensagem.chat.id, response['title'] +" "+response["date"])
		bot.send_photo(mensagem.chat.id, photo = response['hdurl'])
		bot.send_message(mensagem.chat.id, response["explanation"])
		bot.send_message(mensagem.chat.id, "Clique em /foto_aniversario para uma nova consulta.=)")
		
	except :
		bot.send_message(mensagem.chat.id, response['msg']+". Por favor /restart")


@bot.message_handler(commands = ["foto_aniversario"])
def foto(mensagem):
	send = bot.send_message(mensagem.chat.id, "Digite a data do seu aniversário no formato YYYY-MM-DD, sabendo que a primeira foto foi tirada em 1995-06-16")
	bot.register_next_step_handler(send, retorna_foto)


def verificar(mensagem):
    return True

@bot.message_handler(func = verificar)
def comandos(mensagem):
    texto = """ 
    Escolha uma opção:
    /foto_aniversario Retorna a Foto da Nasa no dia
    Qualquer comando além desses não vai funcionar.
    """
    bot.reply_to(mensagem, texto)
    

bot.polling()
