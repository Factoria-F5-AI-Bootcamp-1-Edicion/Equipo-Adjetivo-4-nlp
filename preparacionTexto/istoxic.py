import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
import pandas as pd
import re

# ---------- Cosas a descargar para que ntlk funcione correctamente en Inglés----------
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
#--------------------------------------------------------------------------------------

'''
Texto de entrada
'''
texto_analizar = "The Cat meowed"

'''
Rutas de archivos pickle
'''
ruta_modelo = './models/modelito.pickle'
#ATENCIÓN: Solo se usa un transformer, o Bow o TFIDF
ruta_transformer = './models/bow_transformer.pickle'      #BoW TRansformer
#ruta_transformer = './models/tfidftransformer.pkl'       #TFIDF Transformer

'''
Preprocesado del texto
'''

# Función que elimina toda la puntuación, todas las palabras de parada, lematiza las palabras y devuelve una lista de tokens del texto limpio
def limpiaTexto(texto):
   lemmatize=nltk.WordNetLemmatizer()
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

# Función para eliminar emojis
def eliminar_emojis(text): 
   emoj = re.compile("[" 
     u"\U0001F600-\U0001F64F" # emoticons 
     u"\U0001F300-\U0001F5FF" # symbols & pictographs 
     u"\U0001F680-\U0001F6FF" # transport & map symbols 
     u"\U0001F1E0-\U0001F1FF" # flags (iOS) 
     u"\U00002500-\U00002BEF" # chinese char 
     u"\U00002702-\U000027B0" 
     u"\U00002702-\U000027B0" 
     u"\U000024C2-\U0001F251" 
     u"\U0001f926-\U0001f937" 
     u"\U00010000-\U0010ffff" 
     u"\u2640-\u2642" 
     u"\u2600-\u2B55" 
     u"\u200d" 
     u"\u23cf" 
     u"\u23e9" 
     u"\u231a" 
     u"\ufe0f" # dingbats 
     u"\u3030" 
      "]+", re.UNICODE) 
   return re.sub(emoj, '', text)      

# Función que limpia y transforma el texto
def preparaTexto(corpus):
   # Convertimos el texto o lista de textos en DataFRame
   df = pd.DataFrame(data= corpus, columns=["texto"])
   # Eliminamos espacios xa0
   df['texto'] = df['texto'].replace(u'\xa0', u' ')
   # Eliminamos espacios blancos
   df['texto'] = df['texto'].str.strip()
   # Eliminamos emojis
   df['texto'] = df['texto'].apply(eliminar_emojis)
   # Limpiamos texto
   df['texto'] = df['texto'].apply(limpiaTexto)
   # Abrimos el transformador y convertimos el texto a datos numéricos
   with open(ruta_transformer, 'rb') as f:
    loaded_transformer = pickle.load(f)  
    X = loaded_transformer.transform(df["texto"])
   return X

'''
Predicción de toxicidad
'''

# Función para predicción de toxicidad
def prediceToxico(corpus):
   # Abrimos el modelo y hacemos la predicción
   with open(ruta_modelo, 'rb') as g:
    loaded_model = pickle.load(g)
    prediccion = loaded_model.predict(preparaTexto(corpus))
   return prediccion

# Función que recibe el texto de entrada, predice la toxicidad y da una respuesta
def predicciones(texto_analizar):
 # Convertimos el texto de entrada en listas
 # Esta primera lista la guardamos para conservar el comentario original
 corpus_original = [texto_analizar]
 # Esta segunda lista será la que se usará para predecir
 corpus = [texto_analizar]
 # Hacemos un DataFrame Original, con el texto original
 dfo = pd.DataFrame(data= corpus_original, columns=["texto"])
 # Lanzamos el programa para predecir la toxicidad
 prediccion = prediceToxico(corpus) 
 # Añadimos las predicciones al DataFrame Original
 dfo["prediccion"] = pd.DataFrame(data= prediccion, columns=["texto"])
 # Para cada texto imprimimos el texto y su predicción
 for i in dfo["texto"]:
   if dfo["prediccion"].item() == True:
      print(f"El comentario: {i} es tóxico")
   else:
      print(f"El comentario: {i} no es tóxico")

# Lanzamos el programa
predicciones(texto_analizar)



