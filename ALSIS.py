import pyttsx3
import os
import webbrowser
import pyaudio
import speech_recognition as sr 
import datetime

same = pyttsx3.init('sapi5')
voices =same.getProperty('voices')
same.setProperty('voice',voices[1].id)

def speak(audio):
    same.say(audio)
    same.runAndWait()

def startup():
    speak("Hello Sir !")
    speak("I Am Als Intelligent System ,You can also say me ALSIS or JARVIS.")
    speak("Start to check Security of your System. ")
    speak("Analysing start")
    speak("Analysing was completed  ,  Now System is secured, no malicious file is found.")
    speak("Startup task is completed ,  Now I am free you can tell me another task.")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir.")
        speak("Have a nice day sir.")

    elif hour>=12 and hour<16 :
        speak("Good Afternoon sir.")
        speak("Have a nice day")   

    elif hour>=16 and hour <20:
          speak("Good evening sir")

    elif hour>=20 and hour<24:
          speak("Good night sir.")
          speak("Sweet Dreams.")
          speak("Take care.")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
       print("Recognizing...")
       query =r.recognize_google(audio,language="en-in")
       print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    print("Initializing...")
    wishMe()
    startup()
    
    while True:

     query =takecommand().lower()

     if 'open youtube' in query:
      webbrowser.open("youtube.com")

     elif 'open google' in query:
         webbrowser.open("google.com")

     elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com") 

     elif 'play music' in query:
         music_dir='D:\\mobile internal\\Download'
         songs = os.listdir (music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir,songs[0]))

     elif 'who are you' in query:
         speak("I am AI developed by Mr.Aniket Sapkal, and my name is ALSIS, you can also say me Jarvis.  ")   

     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir , time is {strTime}")
     elif 'open visual code' in query:
         codepath="C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe"
         os.startfile(codepath)   

     
