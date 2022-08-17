import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import time
import PyPDF2
from googletrans import Translator
from gtts import gTTS #pip install googletrans
import subprocess
import pywhatkit
import pyautogui
import PIL
import keyboard
from PyDictionary import PyDictionary as Dict
import pyjokes  #pip install pyjokes
from playsound import playsound 
import requests,json #pip install requests
# from bs4 import BeautifulSoup
import os
import wolframalpha #pip install wolframalpha







Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
# print(voices[1].id)
Assistant.setProperty('voice', voices[0].id)
Assistant.setProperty('rate', 170)


def speak(audio):
   Assistant.say(audio)
   Assistant.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hi, I'm jarvis 2.0 the Robot. Speed 1 terahertz, memory 1 zigabyte.How can i do you for  sir ")       

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
            
            return "None"
        return query
def music():
    speak('tell me the name of song')
    musicname=takeCommand()
    if 'rockstar' in musicname :
        os.startfile('F:\\music1')
    else:
         pywhatkit.playonyt(musicname)
def whatsapp():
    speak('tell me the name of the person')
    name=takeCommand()
    name=name.lower()

    if 'aryan' in name:
        # speak('tell me the message!')
        # msg=takeCommand()
        # speak('tell me the time sir')
        # speak('time in hour')
        # hour=int(takeCommand())
        # speak('time in minutes')
        # min=int(takeCommand())
        pywhatkit.sendwhatmsg("+91**********","Hello from jarvis assiatant from rakesh sir",0, 44)  #22hr means 10 bajker and 28 means 28 minutes
        speak("ok sir , sending whatsapp message !")               
    elif 'rajeev119' in name:
        speak('tell me the message!')
        msg=takeCommand()
        speak('tell me the time sir')
        speak('time in hour')
        hour=int(takeCommand())
        speak('time in minutes')
        min=int(takeCommand())
        pywhatkit.sendwhatmsg("+91xxxxxxxxxx","Hello from GeeksforGeeks",22, 28)  #22hr means 10 bajker and 28 means 28 minutes
        speak("ok sir , sending whatsapp message !")               
    elif 'Rakesh' in name:
        speak('tell me the message!')
        msg=takeCommand()
        speak('tell me the time sir')
        speak('time in hour')
        hour=int(takeCommand())
        speak('time in minutes')
        min=int(takeCommand())
        pywhatkit.sendwhatmsg("+91*********","Hello from GeeksforGeeks",0,49)  #22hr means 10 bajker and 28 means 28 minutes
        speak("ok sir , sending whatsapp message !") 
    else:
        speak('tell me the number!')
        phoneno=int(takeCommand())
        ph='+91' + phoneno
        speak('tell me the message!')
        msg=takeCommand()
        speak('tell me the time sir')
        speak('time in hour')
        hour=int(takeCommand())
        speak('time in minutes')
        min=int(takeCommand())
        pywhatkit.sendwhatmsg(ph,msg,hour,min)  #22hr means 10 bajker and 28 means 28 minutes
        pywhatkit.sendwhatmsg("+91xxxxxxxxxx","Hello from GeeksforGeeks",22, 28)  #22hr means 10 bajker and 28 means 28 minutes
        speak("ok sir , sending whatsapp message !") 
def screenshot():
    speak("ok Boss , what should i name that file ?")
    kk=pyautogui.screenshot()
    kk.save('D:\\')
def closeapps():
    speak("ok sir , wait a second")
    if 'youtube' in query:
        os.system("TASKKILL /F /in chrome.exe")
    if 'chrome' in query:
        os.system("TASKKILL /F /in chrome.exe")
    if 'telegram' in query:
        os.system("TASKKILL /F /in Telegram.exe")
    if 'code' in query:
        os.system("TASKKILL /F /in code.exe")
    speak("Your Command is done")
def youtubeauto():
    speak("whats is your command")
    command=takeCommand()
    if 'pause' or 'plaY' in command:
        keyboard.press('space bar')
    if 'restart' in command:
        keyboard.press('0')
    if 'mute' in command:
        keyboard.press('m')
    if 'skip' in command:
        keyboard.press('1')
    if 'back' in command:
        keyboard.press('j')
    if 'full screnn mode' in command:
        keyboard.press('f')
    if 'film mode' in command:
        keyboard.press('t')
    speak('Done sir')
def chromeauto(): 
    speak('chrome automation started!')
    command=takeCommand()
    if 'close tab' in command:
        keyboard.press_and_release('ctrl + w')
    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + t')
    elif 'open new window' in command:
        keyboard.press_and_release('ctrl + n')
    elif 'history' in command:
        keyboard.press_and_release('ctrl + h')
    elif 'downloads ' in command:
        keyboard.press_and_release('ctrl + d')
def Dict():
    speak('Dictionary Started!')
    speak('tell me the problem')
    problem1=takeCommand()
    if 'meaning' in problem1: 
        problem1=problem1.replce('what is the',"")
        problem1=problem1.replce('meaning',"")
        problem1=problem1.replce('syononame',"")
        problem1=problem1.replce('antoname',"")
        problem1=problem1.replce('of',"")
        problem1=problem1.replce('jarvis',"")
        result=Dict.meaning(problem1)
        print(result)
        speak("The meaning of {problem1} is {result}")
    if 'synoname' in problem1: 
        problem1=problem1.replce('what is the',"")
        problem1=problem1.replce('meaning',"")
        problem1=problem1.replce('syononame',"")
        problem1=problem1.replce('antoname',"")
        problem1=problem1.replce('of',"")
        problem1=problem1.replce('jarvis',"")
        result=Dict.synonym(problem1)
        print(result)
        speak("The meaning of {problem1} is {result}")
    if 'antoname' in problem1: 
        problem1=problem1.replce('what is the',"")
        problem1=problem1.replce('meaning',"")
        problem1=problem1.replce('syononame',"")
        problem1=problem1.replce('antoname',"")
        problem1=problem1.replce('of',"")
        problem1=problem1.replce('jarvis',"")
        result=Dict.antonym(problem1)
        print(result)
        speak("The meaning of {problem1} is {result}")
def alarm():
    speak("enter the time!")
    time=input("Enter the time:")       
            
    while True:
        pctime=datetime.datetime.now()
        now=pctime.strftime("%H:%M:%S")
        if now==time:        
            speak("Time for wake up Sir!")          
            playsound('alarm.mp3')          
            speak("alarm closed!")            
        elif now>time:
            break               
def takehindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='hi')
            print(f"You said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            
            return "None"
        return query
def Translator():
    speak('Tell me the line')
    line=takehindi()
    translate=Translator()
    result=translate.translate(line) #it will tranlate the line in english
    Text=result.text #it will convert the result
    speak('The translation for this line is: {+Text}')
def Temp():
    speak('tell me the place name')
    search="temperature in patna"
    url='https://www.google.com/search?q={search}'
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temperature =data.find("div",class_="BNeawe").text
    speak(f" current {search} is  {temperature}")
# ARPX63-ETE4TExxxx
def wolfram(query):
    api_id="ARPX63-ETE4TExxxx"
    requester = wolframalpha.Client(api_id) # Instance of wolf ram alpha  # client class
    requested=requester.query(query) # Stores the response from 
    
    try:
        Answer =next (requested.results).text #include only text from respnse
        speak(Answer)
    except:
        speak("an string value is not answerable.")
def calculator(query):
    term=str(query)
    term=term.replace("jarvis","")
    term=term.replace("multiply","")
    term=term.replace("add","")
    term=term.replace("substract","")
    term=term.replace("into","")
    term=term.replace("plus","")
    term=term.replace("minus","")
    term=term.replace("addtion","")
    final=str(term)
    try:
        result=wolfram(final)
        speak(f"{result}")
    except:
        speak("an string value is not answerable.")
def science():
    speak('ask the question')
    question = takeCommand()
    print(question)

    app_id = 'ARPX63-ETE4TERRRP' # 
 
    
    # client class
    client = wolframalpha.Client(app_id)# Instance of wolf ram alpha 
    res = client.query(question) 
    try:
        answer = next(res.results).text # Includes only text from the response
        print(answer)
        speak(answer)
    except:
        speak("an string value is not answerable.")
def Reader():
    speak("tell me the name of the book")  
    name =takeCommand()
    if 'india' in name:
        os.startfile()
        book=open()
        pdfreader=PyPDF2.PdfFileReader(book)
        pages=pdfreader.gerNumpages()
        speak(f"Number of pages in this book is {pages}")
        speak('from which page i have to start reading sir?')
        numpage=int(input('enter the page number'))
        page=pdfreader.getpage(numpage)
        text=page.extractText()
        speak('in which language ,I have to Read')
        lang=takeCommand()
        if 'hindi' in lang:
            trans1=Translator()
            texthin=trans1.translate(text,'hi')
            textm=texthin.text
            speech=gTTs(text =textm)
            speech.save('book.mp3')
            playsound('book.mp3')
        else:
            speak(text)




    
    
   




    









if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'screenshot' in query:
            screenshot()
        elif 'closeapps' in query:
            closeapps()
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'youtube search ' in query:
            speak('OK SIR , this is i found for your search')
            query=query.replace('jarvis',"")
            query=query.replace('youtube search',"")
            web='https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
            speak('done sir')
        elif 'website ' in query:
            speak('OK SIR , this is i found for your search')
            query=query.replace('jarvis',"")
            query=query.replace('website',"")
            web1=query.replace('open',"")
            web2='https://www.'+web1 + '.com'
            webbrowser.open(web2)
            speak('done sir')
  

        elif 'open google' in query:
            speak('opening google...')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  
        elif 'open my facebook account' in query:
            webbrowser.open("https://www.facebook.com/profile.php?id=100010034524825") 


        elif 'play music' in query:
            music_dir = 'F:\\music1'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play songs' in query:
            music()


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'send whatsapp ' in query:
            whatsapp()

        elif 'open code' in query:
            codePath = "C:\\Users\\Rakesh gupta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Rakesh Sir.")
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Rakesh Sir ")
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")             
 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
        elif "i love you" in query:
            speak("It's hard to understand but")
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            #subprocess.call('shutdown / p /f' )
        elif 'joke' in query:
            get=pyjokes.get_joke 
            speak(get)  
        elif 'repeat my word' in query:
            speak('speak sir')
            said=takeCommand()
            speak(f'You said:{said}') 
        elif 'my location ' in query: 
            webbrowser.open('https://www.google.co.in/maps/search/Hotels/@26.5815611,85.4852044,14z/data=!4m8!2m7!3m6!1sHotels!2sSitamarhi,+Bihar!3s0x39ecf0d7d039429d:0x25381a43016ecd04!4m2!1d85.5012971!2d26.5886976?hl=en&authuser=0')          
        elif 'dict ' in query:
            Dict()
            
        elif 'alarm' in query:
            alarm()
        elif 'translator ' in  query:
            Translator()
        elif 'temperature' in query:
            Temp()
        elif 'question' in query:
            science()
        elif 'chromeautomate' in query:
            chromeauto();
           
     





        





              
        
               
        

