import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import random
import webbrowser
import os
import time
from halo import Halo
from playsound import playsound
from termcolor import colored
import smtplib, ssl
#import socket

#socket.getaddrinfo('127.0.0.1', 80)
wake = False
voice = "jarvis"
name = "jarvis"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


#emailing:
#smtp_server = "smtp.gmail.com"
#port = 587  # For starttls
#sender_email = "my@gmail.com"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def startup():
    print(voices)
    print(colored("INITIATING BOOT SEQUENCE", "yellow"))
    #time.sleep(4)
    print(colored("Boot Successful", "yellow"))
    #time.sleep(2)
    print("Initiating speech recognition...")
    #time.sleep(2)
    print("Initiating voices")
    #time.sleep(3)
    print("Wrapping up...")
    #time.sleep(4)

    ####### 2025 note: idk why i did this boot sequence with time.sleep() it just makes the thing slower lol

    print(colored("J.A.R.V.I.S. is ready to use!", "green"))
    playsound("boot.mp3")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(f"I am {name}. Speak my name whenever you need me!")

def wakeFunciton():

    r = sr.Recognizer()
    with sr.Microphone() as source:
       
        print(colored("Listening...", "blue"))
        audio = r.listen(source)
        r.energy_threshold = 300

    try: 
        print("Processing...")
        print(f"looking for name: {name}")
        wakeName = r.recognize_google(audio, language="en-in")
        print(f"User said: {wakeName}\n")
        

    except Exception as e:
        print(e)
        print(colored("Sorry, I did not catch that. Please try again...", "red"))
        speak("Sorry, I did not catch that. Please try again.")
        return "None"
    return wakeName

def takeCommand():
    # recognising user speech from microphone and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
       
        print(colored("Listening...", "blue"))
        playsound('chime1.mp3')
        audio = r.listen(source)
        r.energy_threshold = 300

    try: 
        print("Processing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        

    except Exception as e:
        print(e)
        print(colored("Sorry, I did not catch that. Please try again...", "red"))
        speak("Sorry, I did not catch that. Please try again.")
        takeCommand()
        return "None"
    return query

def sendEmail(to, content):

    # Create a secure SSL context
    context = ssl.create_default_context()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls(context=context)
    server.login('email_id_here', 'pass_here')
    server.sendmail('email_id_here', to, content)
    server.close()

if __name__ == "__main__":
    startup()
    while True:
        wakeName = wakeFunciton().lower()
        if name in wakeName:
            print("waking up!")
            wake = True
            # logic for executing tasks based on query
            query = takeCommand().lower()
            playsound('chime2.mp3')
            if 'wikipedia' in query:
                speak("Searching wikipedia.....")
                query = query.replace("wikipedia", "")
                if name in query:
                    query = query.replace(f"{name}", "")
                results = wikipedia.summary(query, sentences=2)
                # print(f"searching wikipedia for {query}\n")
                speak("According to Wikipedia:")
                print(results)
                speak(results)

            #basic commands

            elif 'how are you' in query:
                speak("I am doing wonderful. Thanks for asking!")


            elif 'who are you' in query:
                speak(f"Hello! My name is {name}. I am a very cool AI.")

            elif 'what is your name' in query:
                speak(f"hello! i am {name} how may i help you")

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
                url = "google.com/search?q=" + query
                webbrowser.open(query)

            elif 'on google' in query:
                query = query.replace("on google ", "")
                url = "google.com/search?q=" + query
                speak("Here are some results from google:")
                webbrowser.open(query)
                
            elif 'how to' in query:
                speak("Here are some results from google:")
                url = "google.com/search?q=" + query
                webbrowser.open(url)
            
            elif 'what is' in query:
                    query = query.replace("what is", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)
                    speak("here are some results from google.")
                    url = "google.com/search?q=" + query
                    webbrowser.open(query)

            elif 'who is' in query:
                query = query.replace("who is", "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)
                speak("here are some results from google.")
                url = "google.com/search?q=" + query
                webbrowser.open(query)
            
            #utility

            elif 'change your name' in query:
                speak("alright. please enter a name here.")
                name = input("Enter a new name here: ").lower()
                speak("OK. Changing my name.")
                print(colored("Changing my name......", "blue"))
                time.sleep(1)
                print(colored("DONE", "green"))
                print(f"Name changed to: {name}")
                speak(f"My name is {name} now")
            
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

                    to = "your own email here"

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
            
            elif 'change your voice' in query:
                speak("okay. changing my voice.")
                if voice == "jarvis":
                    voice = "alexa" ## lol
                    engine.setProperty('voice', voices[1].id)
                else:
                    voice = "jarvis"
                    engine.setProperty('voice', voices[0].id)
                speak("this is my new voice now")
                
                

            #fun

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
                webbrowser.open("your yt channel link if you want")

            elif 'tell me a joke' in query:
                #print(random.choice(jokeLibrary))
                #speak(random.choice(jokeLibrary))
                # jokes library
                try:
                    jokeLibrary = ["What's the best thing about Switzerland? I don't know, but the flag is a big plus.", "Why did the picture go to jail? It was framed.",
                                    "Why did the broom wake up late? It over swept.", "Why do you go to bed every night? because the bed won't come to you."]
                    joke = random.choice(jokeLibrary)
                    print(joke)
                    speak(joke)
                    playsound('badumtss.mp3')
                except Exception as e:
                    print(e)

            #else:
            #if the query is not coded yet
            #    speak("I'm Sorry, i dont know how to respond to that.")
            #   if query != "":
            #        speak("But, i can search it on google if you'd like.")
             #       webbrowser.open(query)

            
            #if query == "":
            #    speak("please speak louder, i do not understand.")