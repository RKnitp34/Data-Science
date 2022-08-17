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
    speak('Done sir')s