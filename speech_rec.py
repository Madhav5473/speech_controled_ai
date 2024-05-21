import pyttsx3
x = pyttsx3.init()

import speech_recognition as sr
def speak(audio):
    x.say(audio)
    x.runAndWait() #used to run the program and wait for some time

def rec():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r1.pause_threshold = 1 #used to pause for some threshold after speaking r1.pause_threshold = 1 
        audio = r1.listen(source)

        try :
            print("Recognizing...")
            query = r1.recognize_google(audio,language = "en-in")#directly connects to google translator in english lang
            return query 
        except Exception as e:
            print(e)
            speak("sorry can't understand")
            rec()
            return "None"
        return query
rec()

        

