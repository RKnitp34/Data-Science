import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import time
import subprocess
#import pyjokes  #pip install pyjokes
#from ecapture import ecapture as ec #pip install ecapture

import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hi, I'm jarvis 2.0 the Robot. Speed 1 terahertz, memory 1 zigabyte.How can i do you for  sir")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            
            return "none"
        return query
query=takeCommand()
if 'hello ' in query:
    speak('hello sir')