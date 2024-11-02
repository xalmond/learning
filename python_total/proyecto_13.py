import webbrowser
import datetime
import wikipedia

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes


# Listen mic and get text
def transform_voice_2_text():

    # Init objects
    rec = sr.Recognizer()

    with sr.Microphone() as mic:

        # Start process
        rec.pause_threshold = 0.8
        print('Puedes empezar a hablar.')
        audio = rec.listen(mic)  # Almacena el audio escuchado en una variable
        print(audio)
        text = rec.recognize_sphinx(audio)  # Proceso de reconocer  de Google
        print(text)

def say_a_text(text):

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


say_a_text('Hola, ¿qué tal?')


print(transform_voice_2_text())
