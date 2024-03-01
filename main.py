import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import openai
import datetime
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "some error occured sorry from zora"

if __name__ == "__main__":
    say("Hello, I am your virtual assistant ZORA.")
    while True:
        print("Listening.....")
        query = takeCommand()
        website=[["YouTube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["Google","https://www.google.com"]]
        for site in website:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir")
                webbrowser.open(site[1])
        if "play music" in query:
            musicPath = r"C:\Users\DEBANGSHU\Downloads\Music\MaanMeriJaan.mp3"
            os.system(f"explorer {musicPath}")
            say(query)
        if "the time" in query:
            musicPath = r"C:\Users\DEBANGSHU\Downloads\Music\MaanMeriJaan.mp3"
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"sir the time is {strfTime}")
        say(query)