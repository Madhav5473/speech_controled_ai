import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import pyautogui as pag  # for newer version of python we use PyScreeze
import pywhatkit as kit
import smtplib #to send email
import json
import requests
import music


x = pyttsx3.init()

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOTljOTY1YzItNGJhOC00YjI2LWJjZmUtMDAxZmQxMTExNmE1IiwidHlwZSI6ImFwaV90b2tlbiJ9.x_ODxmXGn88lQmFi-ffrTpXr_OgHm5Ed6ncz8ektlWM"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "abcd"
}

def ai(query):
    payload["text"] = query
    #print(payload)
    response = requests.post(url, json=payload, headers=headers)
    #print(response.text)
    result = json.loads(response.text)
    print(result['openai']['generated_text'])
    speak(result['openai']['generated_text'])

def time():
    t = datetime.datetime.now().strftime("%H:%M:%S")
    speak(t)
#time()

def date():
    y = "samwathram" + str(datetime.datetime.now().year)
    m = "nela yemo" + str(datetime.datetime.now().month)
    d = "ee roju thareku" + str(datetime.datetime.now().day)
    speak(d)
    speak(m)
    speak(y)
                                                    
#date()

def wish():
    h = datetime.datetime.now().hour
    if(h<12):
        speak("good morning")
    elif(h >= 12 and h <= 18):
        speak("good evening")
    else:
        speak("good night")
    speak("hi this is balayya")
    speak("happy ga undu")
#wish()

def youtube(ele):
    kit.playonyt(ele)#used to open youtube based on command query search

def google(ele):
    kit.search(ele)#to search in chrome

def whatsapp(to,msg):
    kit.sendwhatmsg_instantly(to,msg)


def sendmail(to,msg):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('www.madhav.msv@gmail.com', 'ljzf okrp ghso xzf')  # Replace with your actual password
    server.sendmail('www.madhav.msv@gmail.com', to, msg)
    server.close()
    print("Email sent successfully")


def speak(audio):
    x.say(audio)
    x.runAndWait() #used to run the program and wait for some time
#speak("Hello World")


def rec():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r1.pause_threshold = 1 #used to pause for some threshold after speaking r1.pause_threshold = 1 
        audio = r1.listen(source)

        try :
            print("Recognizing...")
            query = r1.recognize_google(audio,language = "en-in")#directly connects to google translator in english lang
            print(query) 
        except Exception as e:
            print(e)
            speak("sorry can't understand")
            rec()
            return "None"
        return query
#rec()

def ss():
    speak("im taking the screenshot")
    im1 = pag.screenshot()
    im1.save('D:/projects/ai/college/img.png')#'/' forwordslash is used to write on that specific file


if __name__ == "__main__":
    while True:
        query = rec().lower()
        if "time" in query :
            time()
        elif "date" in query:
            date()
            
        elif "wikipedia" in query:
            print("vethukuthunaa .....")
            speak("Vethukuthunnaaa okka nimasham aggu")
            query = query.replace("wikipedia","")#to replace wikipedia word with nothing
            result = wiki.summary(query, sentences = 2)#used to summarize the entire topic into 2 lines sentence
            print(result)
            speak(result)
        elif "screenshot" in query:
            ss()
        elif "chrome" in query:
            speak("what do you want to search")
            ele = rec()
            speak("opening..")
            google(ele)
        
        elif "youtube" in query:
            speak ("what do you want to search in youtube...")
            ele = rec()
            speak("opening youtube")
            youtube(ele)
        elif "whatsapp" in query:
            try:
                speak("input the number")
                num = "+91"+input()
                speak("say message to send")
                s = rec()
                whatsapp(num,s)
            except Exception as e :
                print(e)


        elif "remember" in query:
            speak("what should i remember")
            data  = rec()
            speak("your likely to remember me that")
            remember = open('data.txt','w')#used to write the data into a txt file which is has to remember
            remember.write(data)
            remember.close()

        elif "forgot" in query:
            remember = open('data.txt','r')
            speak("did you forget this remembered thing")
            speak(remember.read())#read out what we have written in remembered thing

        elif "send mail" in query:
            try:
                speak("enter gmail of the recepient ")
                to = input()
                speak("speak the u have to sent")
                msg = rec()
                sendmail(to,msg)
                speak("sent successfully")
            except Exception as e:
                print(e)
                speak("failed to send")
        elif "play song" in query:
            path = input("enter song path : ")
            music.play_song(path)
        elif "pause the song" in query:
            music.controllor("pause")
        elif "unpause" in query:
            music.controllor("unpause")
        elif "stop" in query:
            music.controllor("stop")


        elif "exit" in query:
            speak("Vellipothuna raa maawa ....")
            print("bye bye")
            exit()
        else:
            ai(query)


