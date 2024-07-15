from tkinter import *
from tkinter import ttk

from googletrans import Translator, LANGUAGES

def change(text="type", src="english", dest="hindi"):
    src1 = src
    dest1 = dest  # Fix the typo here
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    text = source.get(1.0, END)
    s = comb_source.get()
    d = comb_dest.get()
    textget = change(text=text, src=s, dest=d)  # Fix the typo here
    dest.delete(1.0, END)
    dest.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg="Sky Blue")

lab = Label(root, text="Translator", font=("Time New Roman", 20, "bold"))
lab.place(x=100, y=40, height=50, width=300)

frame = Frame(root)
frame.pack(side=BOTTOM)

t = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"), fg="black", bg="Sky Blue")
t.place(x=100, y=100, height=30, width=300)

source = Text(root, font=("Time New Roman", 20, "bold"), wrap=WORD)
source.place(x=10, y=140, height=100, width=480)

langs = list(LANGUAGES.values())

comb_source = ttk.Combobox(root, values=langs)
comb_source.place(x=10, y=300, height=40, width=150)
comb_source.set("english")

button = Button(root, text="Translate", relief=RAISED, command=data)
button.place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(root, values=langs)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("hindi")

d = Label(root, text="Dest Text", font=("Time New Roman", 20, "bold"), fg="black", bg="Sky Blue")
d.place(x=100, y=360, height=20, width=300)

dest = Text(root, font=("Time New Roman", 20, "bold"), wrap=WORD)
dest.place(x=10, y=400, height=100, width=480)

root.mainloop()