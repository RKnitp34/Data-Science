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