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