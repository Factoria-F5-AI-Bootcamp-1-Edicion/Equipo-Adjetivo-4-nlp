# -- coding: utf-8 --
## pip install textblob
## python -m textblob.download_corpora
# ******************************
import requests
import json
import time
from textblob import TextBlob
from ia import *
#   * leer variables *   #
import os
from dotenv import load_dotenv
# ******************************
load_dotenv()
yt = os.getenv('KEY_YT')

data = requests.get("https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies&moderationStatus=published&videoId=lF3RKuiFpn8&key="+yt)
    
json = data.json() 

def analisis(dato, user,video):
    sensibilidad = 0.0
    resul = TextBlob(dato)
    #traducion=  resul.translate(from_lang="es", to="en")
    analysis = resul.correct()
    #print('\n',analysis)
    #print('\n',analysis.sentiment.polarity)
    #print('\n\n Etiquetas Clave:\n',analysis.tags)
    # Version Alfa 0.01
    if analysis.sentiment.polarity <= sensibilidad :   
        return f"\n{video} \n*User: * {user} * \n\nComentario: {analysis} "


def mensajes():
    x = range(20)
    for n in x:
        dato =json['items'][n]['snippet']['topLevelComment']['snippet']['textDisplay']
        user = json['items'][n]['snippet']['topLevelComment']['snippet']['authorDisplayName']
        video = json['items'][n]['snippet']['topLevelComment']['snippet']['authorProfileImageUrl']
        if dato == "":
            break
        else:
            return f"\n{video} \n*User: * {user} * \n\nComentario: {dato} - {prediceToxico(dato)}"
