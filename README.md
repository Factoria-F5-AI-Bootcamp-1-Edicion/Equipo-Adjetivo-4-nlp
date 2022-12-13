# Equipo Adjetivo - Detección de mensajes de odio en comentarios de Youtube

Este proyecto tiene como objetivo automatizar el proceso de deteccion de mensajes de odio
en los comentarios provenientes de un canal de Youtube en tiempo real mediante la integracion 
con el servicio de bots proporcionado por la API de Telegram.

Nuestra API recibe los comentarios del canal, los procesa y realiza la prediccion de contenido de odio 
a traves de un modelo de Machile Learning basado en un algoritmo de Ensemble. 

Si dicho comentario es clasificado como de odio , envia una notificacion al Telegram del propietario del canal de Youtube 

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Clona el proyecto_

```
git clone https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/Equipo-Adjetivo-4-nlp.git
```

_Instalar dependencias_

```
pip install -r requirements.txt
```

_Moverse a la carpeta src/ del proyecto_

```
cd Equipo-Adjetivo-4-nlp/src
```

_Usuario debe obtener las credenciales de autenticacion de Telegram y Youtube (tokens)_

```
https://developers.google.com/youtube/registering_an_application?hl=es-419
https://core.telegram.org/bots
```

_Crear un archivo .env con las siguientes dos variables de entorno correspondientes a las credenciales de Youtube y Telegram_


| Variable de entorno | Descripción                    |  Ejemplo                                        |
|---------------------|--------------------------------|-------------------------------------------------|
| `KEY_TLG`           | token de Telegram              | `Conversación con @BotFather y comando /newbot` |
| `KEY_YT`            | token de API Youtube           | `Token de Youtube Data API`                     |




## Despliegue 📦

_Ejecutar API desde directorio raiz_

```
python src/main.py
```

_Abrir cliente de Telegram (version mobile o escritorio), iniciar una conversacion con @Telgram_

```
Ejecutar comando /start
```

## Project structure
```bash
.
├── config                      
│   ├── main.yaml                   # Main configuration file
│   ├── model                       # Configurations for training model
│   │   ├── model1.yaml             # First variation of parameters to train model
│   │   └── model2.yaml             # Second variation of parameters to train model
│   └── process                     # Configurations for processing data
│       ├── process1.yaml           # First variation of parameters to process data
│       └── process2.yaml           # Second variation of parameters to process data
├── data            
│   ├── final                       # data after training the model
│   ├── processed                   # data after processing
│   ├── raw                         # raw data
│   └── raw.dvc                     # DVC file of data/raw
├── docs                            # documentation for your project
├── dvc.yaml                        # DVC pipeline
├── .flake8                         # configuration for flake8 - a Python formatter tool
├── .gitignore                      # ignore files that cannot commit to Git
├── Makefile                        # store useful commands to set up the environment
├── models                          # store models
├── notebooks                       # store notebooks
├── .pre-commit-config.yaml         # configurations for pre-commit
├── pyproject.toml                  # dependencies for poetry
├── README.md                       # describe your project
├── src                             # store source code
│   ├── __init__.py                 # make src a Python module 
│   ├── process.py                  # process data before training model
│   └── train_model.py              # train model
└── tests                           # store tests
    ├── __init__.py                 # make tests a Python module 
    ├── test_process.py             # test functions for process.py
    └── test_train_model.py         # test functions for train_model.py
```


## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Lenguaje de programacion) - Python 3.10.7
* Metodología Scrum.
* IDE: Visual Studio Code
* Gestor de paquetes: pip
* Herramienta organizativa : Trello
* librerias de M.L: Scikit-learn y catboost
* Librerias NPL : Spacy, spamoji y NLTK, re, string y TextBlob
* Librerias para comunicacion con servicios externos : requests.
* Herramientas de  analisis : Pandas, Seaborn y matplotlib.



## Versionado 📌

Sistema de control de versiones Git

## Autores ✒️

* Victor Arbiol (Product Owner-Developer) 
* Mayra Espinoza (Developer) 
* Nayare Soledad (Developer) 
* Sebastian Degaudenci (Scrum Master) 





