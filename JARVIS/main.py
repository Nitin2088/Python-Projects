import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("good Evening")

    speak("I am Jarvis Sir, Please tell me how may i help you")

def takeCommand():
    '''it takes microphone input and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:

        print(e)

        print("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()

    while True:
         query = takeCommand().lower()
         if 'wikipedia' in query:
             speak("Searching wikipedia")
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")

         elif 'open google' in query:
             webbrowser.open("google.com")

         elif 'open stack overflow' in query:
             webbrowser.open("stackoverflow.com")

         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir the time is:{strTime}")

         elif 'open vs code' in query:
             code = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(code)

         elif 'open coding ninjas' in query:
             webbrowser.open("codingninjas.com")

         elif 'exit jarvis' in query:
             break

