'''
Project--->JARVIS
'''
#pip install speechrecognition
'''
Converts human voice → text  (instruction by user)
Helps Jarvis understand what you speak through microphone.
'''
#py -3.12 -m pip install package as python --version=3.12,3.14
#pip install sounddevice
'''
Accesses microphone and speaker audio
Records sound from mic
Acts as an alternative to PyAudio.
'''
#pip install pyttsx3
'''
Converts text → speech (System i.e Jarvis speaks the text)
Makes Jarvis speak.
'''
#pip install setuptools
'''
Helps Python install/build packages properly
Many libraries depend on it internally
'''
#py -3.12 -m pip install vosk
'''
alternative of pocketsphinx
'''
#pip install pywithkit
'''
*Why it is useful in Jarvis

Without PyWhatKit:
:manually store links
:maintain dictionary
:update links
--------------------------------
*With PyWhatKit:
:dynamic search
:any song works
:much less code
---------------------------------
'''

import speech_recognition as sr
import pyaudio as pa
import pyttsx3
import webbrowser as wb
import pywhatkit as pw #PyWhatKit is a Python automation library that USES YouTube search internally.(do not need to create a dictionary of songs and there url)

recognizer=sr.Recognizer()

def speak(text):
    engine = pyttsx3.init() # initialising so that text->speech i.e jarvis can speak
    engine.setProperty('rate',190)
    engine.say(text) #say()->to make jarvis speak this 
    engine.runAndWait()
    del engine

def processcommand(c):
    if("open google" in c.lower()):
        wb.open("https://google.com")
    elif("open youtube" in c.lower()):
        wb.open("https://youtube.com")
    elif("open ai" in c.lower()):
        wb.open("https://chatgpt.com") 

    elif("play" in c.lower()):
        song = c.lower().replace("play ","")
        speak(f"Playing {song}")
        pw.playonyt(song)   #directly play song on yt

if __name__=="__main__":
    speak("Hello I am Jarvis Saatvik sir")
    while(True):
        #Listen for the wake word Jarvis

        #obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognising...")
        try:
            with sr.Microphone() as source:
               print("Listening...")
               audio = r.listen(source,timeout=2,phrase_time_limit=3)
            word=r.recognize_google(audio)
            print("Detected:", word)

            if("jarvis" in word.lower()):
                print("Welcome to Virtual World...")
                speak("Ya I am Listening Saatvik")
                with sr.Microphone() as source:
                   print("Jarvis is Active...")
                   audio = r.listen(source,timeout=2, phrase_time_limit=3)
                   command=r.recognize_google(audio)
                   if("stop jarvis" in command.lower()):
                        speak("Shutting down sir")
                        break   #out of infinite loop

                   processcommand(command)
        except Exception as e:
            print("Error")