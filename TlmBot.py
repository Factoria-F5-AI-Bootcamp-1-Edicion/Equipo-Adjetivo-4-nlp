# -*- coding: utf-8 -*-
# se añade @BotFather en telegran
# se le manda el comando: /start
# se le manda el comando: /newbot

import telebot
import time
#from ia import prediceToxico
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle

# ---------- Cosas a descargar para que ntlk funcione correctamente en Inglés----------
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
#--------------------------------------------------------------------------------------

ruta_modelo = './modelito.pkl'
loaded_model = pickle.load(open(ruta_modelo, 'rb'))

# Creamos una función con la limpieza de datos
def limpiaTexto(texto):
   lemmatize=nltk.WordNetLemmatizer()
   # Eliminamos espacios blancos
   texto.replace(u'\xa0', u' ')
   texto.strip()
   #Comprobar los caracteres para ver si están en la puntuación
   nopunc = [char for char in texto if char not in string.punctuation]
   # Vuelve a unir los caracteres para formar la cadena.
   nopunc = ''.join(nopunc)
   # Lemmatizar las palabras
   nopunc = [lemmatize.lemmatize(word) for word in nopunc.split()]
   # Vuelve a unir los caracteres para formar la cadena.
   nopunc = ' '.join(nopunc)
   # Ahora sólo hay que eliminar las palabras de parada
   return [word.lower() for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# estamos entrenando otro tfidf, se debe usar el de entrenamiento
# utilizamos solo bow o tfidf

def preparaTexto(texto):
   input = [f"{texto}"] 
   ruta_transformer = './transformer.pkl'
   #ruta_transformer = './models/tfidftransformer.pkl'
   loaded_transformer = pickle.load(open(ruta_transformer, 'rb'))
   text_bow = loaded_transformer.transform(input)
   return text_bow

# Función para predicción de toxicidad
def prediceToxico(texto):
   prediccion = loaded_model.predict(preparaTexto(texto))
   print(prediccion)
   

# NlpYoutubebot 
bot = telebot.TeleBot("")

# Comandos.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "Hi")
        print(message, "Hi" )

# Echo
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    time.sleep(3)
    print(message.text)
    print(prediceToxico(message.text))
    
    if message.text.find("Ayuda") >= 0:
        bot.reply_to(message, "12346")
    else:
        bot.reply_to(message,'...' )

bot.polling()