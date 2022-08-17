def science():
    speak('ask the question')
    question = takeCommand()
    print(question)

    app_id = 'ARPX63-ETE4TERRRP'# App id obtained by the above steps
 
    
    # client class
    client = wolframalpha.Client(app_id)# Instance of wolf ram alpha 
    res = client.query(question) 
    try:
        answer = next(res.results).text # Includes only text from the response
        print(answer)
        speak(answer)
    except:
        speak("an string value is not answerable.")s