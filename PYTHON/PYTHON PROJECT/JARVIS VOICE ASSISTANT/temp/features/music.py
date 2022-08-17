def music():
    speak('tell me the name of song')
    musicname=takeCommand()
    if 'rockstar' in musicname :
        os.startfile('F:\\music1')
    else:
         pywhatkit.playonyt(musicname)