import os
import time
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    voice = recognizer.recognize_google(audio, language="ru-RU").lower()
    print("[log] Распознано: " + voice)
    execute_cmd(voice)



def execute_cmd(v):
    if v =='время':
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif v == 'выключить компьютер':
        os.system('shutdown -s')

    elif v == 'открой вк' or v == 'открой vk':
        webbrowser.open("www.vk.com")

    elif v == 'открой ютуб' or v == 'открой youtube':
        webbrowser.open("www.youtube.com")
        


r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

speak("Universa вас слушает")
stop_listening = r.listen_in_background(m, callback)

while True:

    time.sleep(0.1) # infinity loop
