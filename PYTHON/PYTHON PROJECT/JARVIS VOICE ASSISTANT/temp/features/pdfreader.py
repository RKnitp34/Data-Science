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