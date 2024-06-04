import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound as p

def gega(event):
    print(event)
    p.playsound("Sound_Effects/Gegagedigedagedago Meme Sound Effect.mp3")
    
def Superidol(event):
    print(event)
    p.playsound("Sound_Effects/Superidol.mp3")

def fbi(event):
    print(event)
    p.playsound("Sound_Effects/fbi.mp3")
    
def scream(event):
    print(event)
    p.playsound("Sound_Effects/scream.mp3")
    
def jesus(event):
    print(event)
    p.playsound("Sound_Effects/Steven.mp3")

def headshot(event):
    print(event)
    p.playsound("Sound_Effects/headshot_1.mp3")

win = tk.Tk()
win.title()

l1 = tk.Label(win,text="Press any button to play a sound")
l2 = tk.Button(win, text="gegagedigedagedago", relief=GROOVE, width=20)
l2.bind("<Button>",gega)
l3 = tk.Button(win, text="FBI Open Up",relief=GROOVE,width=20)
l3.bind("<Button>", fbi)
l4 = tk.Button(win, text="Steven He",relief=GROOVE,width=20)
l4.bind("<Button>", jesus)
l5 = tk.Button(win, text="scream",relief=GROOVE,width=20)
l5.bind("<Button>", scream)
l6 = tk.Button(win, text="Superidol",relief=GROOVE,width=20)
l6.bind("<Button>", Superidol)
l7 = tk.Button(win, text="Headshot",relief=GROOVE,width=20)
l7.bind("<Button>", headshot)

l1.grid(row=1, column=2)
l2.grid(row=2, column=1)
l3.grid(row=2, column=2)
l4.grid(row=2, column=3)
l5.grid(row=3, column=1)
l6.grid(row=3, column=2)
l7.grid(row=3, column=3)


win.mainloop()