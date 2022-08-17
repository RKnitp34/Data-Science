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