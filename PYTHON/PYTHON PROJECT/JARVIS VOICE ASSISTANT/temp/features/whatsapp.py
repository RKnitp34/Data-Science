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
        pywhatkit.sendwhatmsg("+916203770683","Hello from jarvis assiatant from rakesh sir",0, 44)  #22hr means 10 bajker and 28 means 28 minutes
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
        pywhatkit.sendwhatmsg("+916204834527","Hello from GeeksforGeeks",0,49)  #22hr means 10 bajker and 28 means 28 minutes
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
        speak("ok sir , sending whatsapp message !") s