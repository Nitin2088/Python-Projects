import requests
import json
import win32com.client as wincom


city = input("Enter the name of the city:")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6e20aaa1a35bf393e7600a826af1045d"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["main"]["temp"]
a = int(w-273.15)
x = wdic["main"]["feels_like"]
b = int(x-273.15)
y = wdic["wind"]["speed"]
c = wdic["main"]["humidity"]

speaK = wincom.Dispatch("SAPI.SpVoice")
text = f"\n\nThe current weather in {city} is {a} degree celcius but feels like {b} degree celcius  The speed  of the wind is {y} miles per hour and the humidity is {c}  "
print(text)
speaK.Speak(text)

