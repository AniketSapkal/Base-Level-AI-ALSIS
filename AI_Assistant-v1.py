import pyttsx3
import os
import webbrowser
import pyaudio
import speech_recognition as sr
import datetime
import time
import calendar
import pywhatkit
import speedtest



same = pyttsx3.init('sapi5')
voices = same.getProperty('voices')
same.setProperty('voices', voices[0].id)


def speak(audio):
    same.say(audio)
    same.runAndWait()


def tellDay():
    now=datetime.datetime.now()
    speak("Today is "+ now.strftime("%A,%d %B ,  %y "))
    print("Today is "+ now.strftime("%A %d, %B , %y "))


def startup():
    speak("Hello Sir !")
    speak("I Am AI voice Assistant ")
    speak("  You can give me command like ")
    print("\n  * You can give me command like : \n")
    print(" 'open youtube' \t\t  'open Google' \n 'what the time' \t\t 'who are you' \n 'play music' \t\t\t 'google search' \n 'Youtube search' \t\t 'open Website '")
    speak("  open youtube ")
    time.sleep(1)
    speak("  open Google ")
    time.sleep(1)
    speak("  what the time ")
    time.sleep(1)
    speak("who are you")
    


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir.")
        speak("Have a nice day sir.")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon sir.")
        speak("Have a nice day")

    elif hour >= 16 and hour < 20:
        speak("Good evening sir")

    elif hour >= 20 and hour < 24:
        speak("Good night sir.")
        speak("Sweet Dreams.")
        speak("Take care.")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    print("\nInitializing...\n ")
    wishMe()
    tellDay()
    startup()

    while True:

        query = takecommand().lower()

        if 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open chrome' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\mobile internal\\Download'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'who are you' in query:
            speak(
                "I am AI developed by Mr. Aniket Sapkal and Mr. Aniket Sutrawe, you can also say me Jarvis.  ")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , time is {strTime}")
        elif 'open visual code' in query:
            codepath = "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'youtube search' in query:
                speak("Ok, Sir ,This is what I found for your search")
                query=query.replace("youtube search ","")
                web='https://www.youtube.com/results?search_query='+query
                webbrowser.open(web)
                speak("Done sir")    
        elif 'google search' in query:
                speak("Ok, Sir ,This is what I found for your search")
                query=query.replace("google search ","")
                pywhatkit.search(query)
                speak("Done sir")           
        elif 'website' in query:
                speak("Ok Sir, Launching...... ")
                query=query.replace("website ","")
                web1=query.replace("open"," ")
                web2='https://www.'+ web1 +'.com'
                webbrowser.open(web2)
                pywhatkit.search(query)
                speak("Done sir") 
        elif 'net speed' in query:
                speak("It takes few seconds please wait!")
                print("processing.....\n It takes few seconds please wait!")
                wifi  = speedtest.Speedtest()
                speeddow=wifi.download()
                speedup=wifi.upload()
                print("Wifi Download Speed is " + str(speeddow))
                speak("Wifi Download Speed is " )
                speak(speeddow)
                print("Wifi Upload Speed is "+ str(speedup))
                speak("Wifi Upload Speed is ")
                speak(speedup)
                
        else :
            print("Sorry command not found")