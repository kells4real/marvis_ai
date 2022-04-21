import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)

name = ""
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greet(name):
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak(f'Good Morning, {name}!')

    if currentH >= 12 and currentH < 18:
        speak(f'Good Afternoon, {name}!')

    if currentH >= 18 and currentH != 0:
        speak(f'Good Evening, {name}!')


speak('Hello, I am your digital assistant MARVIS!')
speak('How may I help you?')


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f'User: {query} \n')

    except sr.UnknownValueError:
        speak(f"Sorry {name}! I didn't get that! Try typing the command!")
        query = str(input('Command: '))

    return query

def getName():
    speak("What's your name please? ")
    speak("Would you like to type your name or say it? Answer type or say.")
    answer = myCommand()
    global name
    if "say" in answer or "say it" in answer or "hey" in answer or "c" in answer:
        speak("say your name!")
        name = myCommand()
    else:
        name = input("Enter your name please: ")

    if name:
        greet(name)
    else:
        getName()

getName()


if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif 'open code' in query or 'open visual studio code' in query:
            speak('opening visual studio code')
            os.system("code")

        elif 'open pycharm' in query or "open python" in query:
            speak('opening pycharm')
            os.startfile("C:/Program Files/JetBrains/PyCharm 2021.2.2/bin/pycharm64.exe")

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ["Just doing my thing!", "I am fine!", "Nice!", "I am nice and full of energy", "I'm dope"]
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = input("Enter recipient's email: ")
            speak("Please enter your username")
            email = input("Email: ")
            speak("Now enter your password")
            password = input("Password: ")
            if 'me' not in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, recipient, content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak(f'Sorry {name}! I am unable to send your message at this moment!')


        elif 'bye' in query or 'bye marvis' in query or 'goodnight marvis' in query or 'talk to you later' in query\
                or 'goodnight' in query:
            speak('okay')
            speak(f'Bye {name}, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak(f'Hello {name}')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'play music' in query:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('Okay, here is your music! Enjoy!')


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')
