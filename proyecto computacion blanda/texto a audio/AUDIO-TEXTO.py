# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:55:58 2020

@author: Alex
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as recurso:
    print("grabando...")
    audio = r.listen(recurso)
    try:
      texto = r.recognize_google(audio,language='es-ES')
      print("esto es lo que ha dicho : {}".format(texto))
      with open("audio.wav","wb") as fichero:
            fichero.write(audio.get_wav_data())
    except:
              print("suerte para la proxima, habla mas fuerte")
