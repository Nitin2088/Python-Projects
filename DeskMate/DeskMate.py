import random

import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as w
import os
# import openai
from config import apikey
import random
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

chatt = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key="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"
)

chatStr = ""
def chat(query):

    global  chatStr
    print(chatStr)
    # openai.api_key = "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"
    chatStr += f"Nitin: {query}\n DeskMate:"
    # response = openai.Completion.create(
    #      model="gpt-3.5-turbo-instruct",
    #       prompt=chatStr,
    #       temperature=1,
    #       max_tokens=256,
    #       top_p=1,
    #       frequency_penalty=0,
    #       presence_penalty=0
    #     )
    response = chatt.invoke(f"{query} answer in 20 words")
    speak(response.content)
    chatStr += f"{response.content}\n"
    # return  response["choices"][0]["text"]
    return  response.content

    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")

        # with open(f"Openai/prompt - {random.randint(1,2343434356)}","w") as f:
    with open(f"Openai/prompt - {random.randint(1,123456) }.txt","w") as f:
        f.write(text)



engine = pyttsx3.init()
voices = engine.getProperty('voices')
# voices = engine.setProperty('rate',150)
engine.setProperty('voice',voices[0].id)

# def ai(prompt):
#     openai.api_key = apikey
#     text = f"OpenAI response for prompt: {prompt}\n****************\n\n"
#     response = openai.Completion.create(
#          model="gpt-3.5-turbo-instruct",
#           prompt=prompt,
#           temperature=1,
#           max_tokens=256,
#           top_p=1,
#           frequency_penalty=0,
#           presence_penalty=0
#         )
#     print(response.content)
#     text += response.content
#     if not os.path.exists("Openai"):
#         os.mkdir("Openai")
#
#         # with open(f"Openai/prompt - {random.randint(1,2343434356)}","w") as f:
#     with open(f"Openai/prompt - {random.randint(1,123456) }.txt","w") as f:
#         f.write(text)




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

    speak("I am your DeskMate, Please tell me how may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1.0
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return('Some Error Occured, Sorry')


if __name__ == "__main__":
    wishMe()
    while True:
        print('Listening....')
        query = takecommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia","https://www.wikipedia.com"],['google',"https://www.google.com"],
                 ['coding ninjas',"https://www.codingninjas.com/"], ["chat GPT","https://chat.openai.com/"]]
        for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    speak(f"Opening {site[0]} sir...")
                    w.open(site[1])
        if 'open vs code' in query:
             code = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             speak(f"Opening vs code sir...")
             os.startfile(code)

        elif 'open GitHub' in query:
            path = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc\\GitHub Desktop.lnk"
            speak(f"Opening Git HUb sir...")
            os.startfile(path)

        elif 'play music' in query:
             musicpath = "C:\\Users\\HP\\Music\\downfall-21371.mp3"
             os.startfile(musicpath)

        elif 'the time' in query:
             strTime1 = datetime.datetime.now().strftime("%H")
             strTime2 = datetime.datetime.now().strftime("%M")
             speak(f"Sir the time is:{strTime1} baj  ke {strTime2} minute")

        elif 'quit' in query:
            speak('Exiting the console......That was nice meeting you Sir')
            break


        elif "using artificial intelligence".lower() in query.lower():
            speak(f'Generating the answer for {query} sir')
            ai(prompt=query)

        else:
            chat(query)
