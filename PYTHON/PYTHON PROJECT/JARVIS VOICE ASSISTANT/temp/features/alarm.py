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