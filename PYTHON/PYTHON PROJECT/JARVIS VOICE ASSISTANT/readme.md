# J.A.R.V.I.S - A personal assistant

## Created and Tested on windows with Python 3.9.0

An attempt to make a very simple, Personal Assistant that understands speech as well as text input and is capable of performing tasks other than conversing.

The basic idea behind this project is to create a simple stand-alone application
that helps less tech savvy people in the world to use the computer without feeling ignorant or computer illiterate.

The application works same like Siri/ Google Assistant etc. But the application deals with the computer itself mainly.

The U.I of the application is self-explanatory and minimal.
Currently it takes text as input as most of the people are not very good at speaking.

- ### Converses, barely.

    **Talk to J.A.R.V.I.S :** hello jarvis <br>
    **J.A.R.V.I.S :** Hi, I'm jarvis 2.0 the Robot. Speed 1 terahertz, memory 1 zigabyte.what can i do you for  sir.

    **Talk to J.A.R.V.I.S :** Who created you?<br>
    **J.A.R.V.I.S :** Rakesh sir  is the one who created me.

    **Talk to J.A.R.V.I.S :** What does JARVIS stand for?<br>
    **J.A.R.V.I.S :** JARVIS stands for Just A Rather Very Intelligent System.
    
    **Talk to J.A.R.V.I.S :** youtube search <br>
    **J.A.R.V.I.S :** OK SIR , this is i found for your search.
    
    **Talk to J.A.R.V.I.S :** alarm <br>
    **J.A.R.V.I.S :** OK SIR , tell me the time .

    All conversation is only for the hardcoded patterns, which are quite few. Can be easily extended to add by using python scripts and modules.

- ### Automate youtube : Play, Pause, Open, Fullscreen, Skip etc.

    Uses shell commands to play and pause youtube videos.

    **Talk to J.A.R.V.I.S :** search this songs on youtube<br>
    **J.A.R.V.I.S :** tell me the song name<br>
    **Talk to J.A.R.V.I.S :** pause the videos<br>
    **J.A.R.V.I.S :** Done sir!<br>
    **Talk to J.A.R.V.I.S :** please open youtube jarvis<br>
    **J.A.R.V.I.S :** Done, sir!

- ### Tells time.
    
    **Talk to J.A.R.V.I.S :** what time is it?<br>
    **J.A.R.V.I.S :** The time is 7:40 pm{convets its in 24 hours format }


- ### Suggests Googling for all unrecognized interrogative questions

    **Talk to J.A.R.V.I.S :** What is NIT, PATNA?<br>
    **J.A.R.V.I.S :** OK SIR , this is i found for your search.

- ### Plays any song, first search result in youtube

    **Talk to J.A.R.V.I.S :** play me a song<br>
    **J.A.R.V.I.S :** What song, sir?<br>
    **Talk to J.A.R.V.I.S :** Rockstar<br>
    **J.A.R.V.I.S :**  OK SIR , this is i found for your search.

    Uses youtube.py script to find the first search result for the last user input in above case, and opens it in microsoft edge.

- ### Searches internet.

    **Talk to J.A.R.V.I.S :** Google what is the answer to life?<br>
    **J.A.R.V.I.S :**  OK SIR , this is i found for your search.<br>
    **Talk to J.A.R.V.I.S :** Search youtube for BGMI<br>
    **J.A.R.V.I.S :** OK SIR , this is i found for your search.<br>
    **Talk to J.A.R.V.I.S :** Search for my location on google maps<br>
    **J.A.R.V.I.S :** Done it!.

- ### SET Alarm.

    **Talk to J.A.R.V.I.S :** Set alarm.<br>
    **J.A.R.V.I.S :** Enter the time.<br>
    **J.A.R.V.I.S :** Time for wakeup sir<br>
    **J.A.R.V.I.S :** alarm closed<br>

    

- ### Launches Programs.
    
    **Talk to J.A.R.V.I.S :** open vs code<br>
     **J.A.R.V.I.S :** ok sir , wait a second<br>
    **J.A.R.V.I.S :** Your Command is done<br>
    **Talk to J.A.R.V.I.S :** open chrome / open firefox / open calculator / open vlc<br>
    **J.A.R.V.I.S :** ok sir , wait a second<br>
    **J.A.R.V.I.S :** Your Command is done<br>

- ### Closing Programs.
    
    **Talk to J.A.R.V.I.S :** Close vs code<br>
    **J.A.R.V.I.S :** ok sir , wait a second<br>
    **J.A.R.V.I.S :** Your Command is done<br>
    **Talk to J.A.R.V.I.S :** close chrome / close firefox / close calculator / close vlc<br>
    **J.A.R.V.I.S :** ok sir , wait a second<br>
    **J.A.R.V.I.S :** Your Command is done<br>

- ### General Science question.
    import wolframalpha #pip install wolframalpha
    
    **Talk to J.A.R.V.I.S :** question<br>
    **J.A.R.V.I.S :** ask the question<br>
    **Talk to J.A.R.V.I.S :** who is the prime minister of india?<br>
    **J.A.R.V.I.S :** Narendra Modi<br>
    **J.A.R.V.I.S :** Your Command is done<br>

- ### English to Hindi Translator.
    from googletrans import Translator
    from gtts import gTTS #pip install googletrans
    
    **Talk to J.A.R.V.I.S :** Translate this <br>
    **J.A.R.V.I.S :** Tell me the line<br>
    **Talk to J.A.R.V.I.S :** i am eating a mango.<br>
    **J.A.R.V.I.S :** The translation for this line is: Main ek Aam kha rha hu.<br>

- ### Dictionary.
    for dictionar search rom PyDictionary import PyDictionary as Dict
    
    **Talk to J.A.R.V.I.S :** Dict <br>
    **J.A.R.V.I.S :** Dictionary Started!<br>
    **J.A.R.V.I.S :** tell me the problem!<br>
    **Talk to J.A.R.V.I.S :** what is meaning of mango.<br>
    **J.A.R.V.I.S :** The meaning of mango is Aam.<br>

- ### Wikipedia search.
    import wikipedia #pip install wikipedia
    
    **Talk to J.A.R.V.I.S :** sahrukh khan wikipedia <br>
    **J.A.R.V.I.S :** 'Searching Wikipedia...<br>
    **J.A.R.V.I.S :** tell me the problem!<br>
    **J.A.R.V.I.S :** According to Wikipedia {result from wikipedia}.<br>


- ### Other:
    
    Standard replies for unrecognized/unmatched inputs

   **Talk to J.A.R.V.I.S :** you are dumb<br>
    **J.A.R.V.I.S :** please say that again.<br>

    **Talk to J.A.R.V.I.S :** go to sleep / exit / quit / bye / goodbye

    closes the python script.

## Requirements:

Make sure you install these packages before moving forward to other python libraries-





Individual packages listed as follows-

- ### Speech Recognition
    `pip install SpeechRecognition`

- ### PyAudio is required for microphone input
    `pip install pyaudio`
`

- ### ttsx3: (Offline Text to Speech Service)
    `pip install pyttsx3`
- ### wikipedia: (for wikipedia search)
    `pip install wikipedia`
- ### pywhatkit: (Send WhatsApp messages.Play a YouTube video.Perform a Google Search.Get information on a particular topic)
    `pip install pywhatkit`
- ### Pyjokes: (for funny jokes)
    `pip install pyjokes`
- ### wolframalpha: (for searching general science question and many pruposes)
    `pip install wolframalpha`
- ### keyboard: ( used to get full control of the keyboard)
    `pip install keyboard`
- ### Translator: ( for translates english to hindi)
    `pip install googletrans`

- ### Optional for Google Text to Speech :
   + #### gTTS: (Google Text to Speech service)
      `pip install googletrans`

   + #### PyGame: (For audio playback with gTTS)
       `pip install pygame`

Voice mode may give a series of warnings for numerous reasons, but still might fuction properly.

## Application:
jarvis is build to help the people with limited computer knowledge but it is also important to note that the other class of users might find some specific functionalities such as system logging useful.

The people who are not familiar getting around on their own on a computer can use this application as it abstracts away all the steps and presents only most important. Like they can just say to connect to a particular wifi or bluetooth, it will connect. Want to decrease screen brightness or volume? Want to open and close an application, file? Just say it as you would to a person, it will do the work for you.



It can also help with getting around web by opening, closing, bookmarking, reload, back, next etc a webpage just by saying it to do so.


Finally, it the solution for monitoring the computer. It is the solution for the parents who got a computer from their son/daughter and can’t operate it to talk to them. It is the solution for the people who are willing to make a computer as their real assistant( not like fake so called assistants like Siri, Cortana etc ), just like Tony Stark?. Even if anyone uses it, you get complete stats about what he/she was doing, what did they connected etc.

## Contribution:

A lot can be done with this project.Core AI chatbot like functionality can be added. More python scripts can be associated. Pull requests for any such changes are accepted. Feel free to fork this project and make your own changes too.
