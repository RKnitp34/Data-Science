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