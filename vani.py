import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import smtplib, ssl
import wikipedia
import random
from playsound import playsound
from termcolor import colored

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#email birthday: 9th march 1999

#print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def startup():
    playsound('bootT.mp3')
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am Vani! How may i help you?")

def takeCommand():
    #using speech recognition module to recognize user's voice and return string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Processing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Could not recognize, try again.")
        return "None"
    return query

def wakeFunciton():
    #using speech recognition module to recognize user's voice and return string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("wake command....")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        wake = r.recognize_google(audio, language="en-in")
        print(f"user said: {wake}\n")
    except Exception as e:
        print(e)
        print("Could not recognize, try again.")
        return "None"
    return wake

def sendEmail(to, content):
    # Create a secure SSL context
    context = ssl.create_default_context()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls(context=context)
    server.login('email here', 'password here') # this is the AI bot's email address.
    server.sendmail('email here again', to, content)
    server.close()

if __name__ == "__main__":
    startup()
    while True:
        wake = wakeFunciton().lower()
        if 'vani' in wake:
            #wake the bot!
            query = takeCommand().lower()

            #do stuff
            #basic commands
            if 'how are you' in query:
                speak("I am doing wonderful. Thanks for asking!")
                query = takeCommand()

            elif 'who are you' in query:
                speak("Hello! My name is Vani. I am a very cool AI made by big brain rooshil. I was born on the 18th of December 2020.")

            elif 'what is your name' in query:
                speak("Hello! i am Vani. how may i help you")
                query = takeCommand()

            elif 'what are you doing' in query:
                speak("I am waiting for your commands!")
                query = takeCommand()

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M %p")
                speak(f"the time is {strTime}")

                #search commands
            elif 'open youtube' in query:
                speak("alright. opening youtube.")
                webbrowser.open("youtube.com")
            
            elif 'open google' in query:
                speak("alright. opening google.")
                webbrowser.open("google.com")

            elif 'open chrome' in query:
                speak("alright. getting google chrome.")
                os.startfile('C:\Program Files\Google\Chrome\Application\Chrome.exe')

            elif 'search google for' in query:
                query = query.replace("search google for", "")
                webbrowser.open(query)

            elif 'on google' in query:
                query = query.replace("on google ", "")
                speak("Here are some results from google:")
                webbrowser.open(query)

            elif 'how to' in query:
                speak("Here are some results from google:")

                webbrowser.open(url)
            
            elif 'what is' in query:
                query = query.replace("what is", "")
                speak("here are some results from google.")
                webbrowser.open(query)
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)
                except Exception as e:
                    print("There was an error contacting wikipedia.")

            elif 'who is' in query:
                query = query.replace("who is", "")
                speak("here are some results from google.")
                webbrowser.open(query)
                try:
                    results = wikipedia.summary(query, sentences=2)
                    print(results)
                    speak(results)
                except Exception as e:
                    print("There was an error contacting wikipedia.")

            elif 'send an email' in query:
                try:
                    speak("would you prefer to type or speak?")
                    method = takeCommand()
                    if 'speak' in method:
                        speak("What do you want me to say?")
                        content = takeCommand()
                    elif 'type' in method:
                        speak("What do you want me to say?")
                        content = input("Enter what you want me to say: ")

                    to = "your own email id here"

                    speak(f"Are you sure you want to send this message? content: {content}")
                    confirmation = takeCommand()
                    if 'yes' in confirmation:
                        speak("alright. Sending email.")
                        sendEmail(to, content)
                        speak("Email sent!")
                        print(colored("Email was sent.", "green"))
                except Exception as e:
                    print(e)
                    speak("Sorry. I was not able to send the email at this moment. Please check your internet connection!")
            
            elif 'today is my birthday' in query:
                speak("wonderful!")
                playsound('happyBirthday.mp3')
            #fun commandz

            elif 'rock paper scissors' in query:
                rpsPick = ['Rock!', 'Paper!', 'Scissors!']
                speak("Okay. Get Ready: Rock Paper Sissors Shoot!")
                print(random.choice(rpsPick))
                speak("hopefully i won.")

            elif 'open among us' in query:
                speak("alright. opening among us.")
                os.startfile('C:\Program Files (x86)\Innersloth\Among Us\Among us.exe')

           

            elif 'my channel' in query:
                speak("getting your youtube channel:")
                webbrowser.open("idk yt linnk here")
            
            elif 'tell me a joke' in query:
                try:
                    # jokes library
                    jokeLibrary = ["What's the best thing about Switzerland? I don't know, but the flag is a big plus.", "Why did the picture go to jail? It was framed.",
                                    "Why did the broom wake up late? It over swept.", "Why do you go to bed every night? because the bed won't come to you."]
                    joke = random.choice(jokeLibrary)
                    print(joke)
                    speak(joke)
                    playsound('badumtss.mp3')
                except Exception as e:
                    print(f"there was an error: {e}")
            else:
                speak("I'm sorry. i dont know how to respond to that.")