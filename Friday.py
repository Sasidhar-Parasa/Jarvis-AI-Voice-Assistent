from posixpath import expanduser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time
import pywhatkit
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Boss!")
    elif hour >= 16 and hour < 19:
        speak("Good Evening Boss!")
    else:
        speak("Good Night Boss!")
        pass

    speak("This is Friday. How can I help you?")


def takeCommand():
    # Microphone input and its conversion

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sshh.. Listening!")
        r.pause_threshold = 1
        r.dynamic_energy_ratio = 0.1
        audio = r.listen(source)

    try:
        print("Analysing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print("Pardon me!")
        # speak("Sorry thats out of my scope!")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('your mail ID', 'Password')
    server.sendmail('your mail ID', to, content)
    server.close()


if __name__ == "__main__":
    greetMe()
    while True:
        query = takeCommand().lower()
        # Logics
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'hello' in query:
            speak("Hello Boss!")

        elif 'how are you' in query:
            speak("I am Good, as you take care of me!")

        elif 'joke' in query:
            speak("What does Thor Call his Underpants?, Thunderwear.")

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'send message' in query:
            speak("What should I say")
            ab=takeCommand()
            speak("please enter at what you need to send message")
            print("Hours: ")
            hr=int(input())
            print("Minutes: ")
            minutes=int(input())
            pywhatkit.sendwhatmsg('Phone Number',ab,hr,minutes)

        elif 'set time' in query:
            speak("Set the website alarm as H:M:S(all in two digits)")
            set_Alaram = input("Set the website alarm as H:M:S(all in two digits)")
            speak("Enter the website you want to open")
            url = input("Enter the website you want to open")
            Actual_Time = time.strftime("%I:%M;%S")
            while (Actual_Time != set_Alaram):
                print("The time is" + Actual_Time)
                Actual_Time = time.strftime("%I:%M:%S")
                time.sleep(1)
            if (Actual_Time == set_Alaram):
                speak("You should see your webpage Boss")
                print("You should see your webpage now:- ")
                webbrowser.open(url)

        elif 'music' in query:
            webbrowser.open('spotify.com')

        elif 'time' in query:
            stringTime = datetime.datetime.now() .strftime("%H:%M:%S")
            speak(f'The time is {stringTime}')

        elif 'open code' in query:
            vscodePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
            os.startfile(vscodePath)

        elif 'open whatsapp' in query:
            intellijPath = "C:\ProgramData\Lenovo\WhatsApp\WhatsApp.exe"
            os.startfile(intellijPath)

        elif 'open pycharm' in query:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)

        elif 'stop' in query:
            break

        elif 'thank you' in query:
            speak("That's my job boss!. Donot mention")

        elif 'send email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "Enter E-mail Adress"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Failed to send, Try Again!")

        elif 'temperature' in query:
            search="temparature in vijayawada"
            link=f"https://www.google.com/search?q={search}"
            r=requests.get(link)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            print(f"current {search} is {temp}")
            speak(f"current {search} is {temp}")
