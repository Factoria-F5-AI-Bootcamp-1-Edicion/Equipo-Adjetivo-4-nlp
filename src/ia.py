import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
import nltk
from nltk.tokenize import wordpunct_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import spacy
from sklearn.feature_extraction.text import CountVectorizer
import re
from spacy import displacy
from spacy.lang.en.stop_words import STOP_WORDS
import nltk
from nltk import SnowballStemmer
import warnings

warnings.filterwarnings("ignore")
# ---------- Cosas a descargar para que ntlk funcione correctamente en Inglés----------
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
#--------------------------------------------------------------------------------------
# Para obtener las raices de una palbra
stemmer=SnowballStemmer('english')
wnl = WordNetLemmatizer()
# Crea un objeto nlp vacío para procesar ingles --> pipeline de procesamiento
nlp = spacy.load("en_core_web_sm")
ruta_modelo = '../models/modelo_entrenado_final.pkl'
loaded_model = pickle.load(open(ruta_modelo, 'rb'))

def eliminar_emojis(text):
    
    #nlp.add_pipe("emoji", first=True)
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
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
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', text)

def eliminar_stopwords(x):
   global stopwords
   english_stopwords = stopwords.words('english')
   english_stopwords.append('nt')
   # Resta de conjuntos : stopwords sin los elementos del segungo conjunto set
   stopwords = set(english_stopwords) - set(['i', 'he', 'she', 'you', 'me', 'we', 'us',
                                                   'this', 'them', 'that', 'those', 'her', 'his'])
   return ' '.join([word for word in x.split() if word not in (stopwords)])                                                

# Creamos una función con la limpieza de datos
def limpiaTexto(texto):


   text_mod = re.sub('.*?¿', '', texto)
   re.sub('[0-9]+', '', text_mod)
   text_mod = re.sub('[%s]' % re.escape(string.punctuation), '', text_mod)
   text_mod = re.sub('\w*\d\w*', '', text_mod)
   text_mod = re.sub('\n', '', text_mod)
   text_mod = re.sub(r'[^\w\s]', '', text_mod)
   text_mod = re.sub(r'#', '', text_mod)
   text_mod = re.sub(r'@[A-Za-z0-9]+', '', text_mod)
   text = re.sub('(\\\\u([a-z]|[0-9])+)', ' ', text)
   text = re.sub(r'https|http?:\/\/\S+', '', text)
   return text_mod
def minusculas(text):
    text = text.lower()
    return text

def lematiza_nombres(words):
    global wnl
    a = []
    for token in words:
        lemmetized_word = wnl.lemmatize(token)
        a.append(lemmetized_word)
    return a

def lematiza_verbos(words):
    global wnl
    a = []
    for token in words:
        lemmetized_word = wnl.lemmatize(token, pos='v')
        a.append(lemmetized_word)
    return a

def lematiza_adjetivos(words):
    global wnl
    a = []
    for token in words:
        lemmetized_word = wnl.lemmatize(token,pos='a')
        a.append(lemmetized_word)
    return a

def lematiza_adverbios(words):
    global wnl
    a = []
    for token in words:
        lemmetized_word = wnl.lemmatize(token, pos='r')
        a.append(lemmetized_word)
    return a

def lematiza_adj_satelites(words):
    global wnl
    a = []
    for token in words:
        lemmetized_word = wnl.lemmatize(token,pos='s')
        a.append(lemmetized_word)
    return a
def list_to_strs(text):
    return ' '.join(text)


def preparaTexto(texto):
   
   texto = eliminar_emojis(texto)
   texto = eliminar_stopwords(texto)
   texto = minusculas(texto)
   texto = word_tokenize(texto)
   texto= lematiza_nombres(texto)
   texto=lematiza_verbos(texto)
   texto=lematiza_adjetivos(texto)
   texto= lematiza_adverbios(texto)
   texto = lematiza_adj_satelites(texto)
   texto = list_to_strs(texto)
   ruta_transformer = '../models/transformer.pkl'
   #ruta_transformer = './models/tfidftransformer.pkl'
   loaded_transformer = pickle.load(open(ruta_transformer, 'rb'))
   input = [f"{texto}"]
   text_bow = loaded_transformer.transform(input)
   X = text_bow
   return X

# Función para predicción de toxicidad
def prediceToxico(texto):
   prediccion = loaded_model.predict(preparaTexto(texto))
   if prediccion == 1:
     print("Deben tomarse medidas.")
     return "\n\nDeben tomarse medidas."
   else:
      print("Este mensaje no parece ser tóxico")
      return "\n\nDeben tomarse medidas."

     