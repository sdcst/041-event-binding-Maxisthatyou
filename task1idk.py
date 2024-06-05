import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound as p

def gega(event):
    print(event)
    p.playsound("Sound_Effects/Gegagedigedagedago Meme Sound Effect.mp3", block=False)
    
def Superidol(event):
    print(event)
    p.playsound("Sound_Effects/Superidol.mp3", block=False)

def fbi(event):
    print(event)
    p.playsound("Sound_Effects/fbi.mp3", block=False)
    
def scream(event):
    print(event)
    p.playsound("Sound_Effects/scream.mp3", block=False)
    
def jesus(event):
    print(event)
    p.playsound("Sound_Effects/Steven.mp3", block=False)

def headshot(event):
    print(event)
    p.playsound("Sound_Effects/headshot_1.mp3", block=False)

win = tk.Tk()

Fbi=PhotoImage(file="fbi1.png")
steven=PhotoImage(file="Steven.png")
screams=PhotoImage(file="scream.png")
superidol=PhotoImage(file="Superidol.png")
headshots=PhotoImage(file="headshot.png")
gegas=PhotoImage(file="gega.png")



l1 = tk.Label(win,text="Press any image to play a sound")
l2 = tk.Label(win, image=gegas, width=250, height=250)
l2.bind("<Button>",gega)
l3 = tk.Label(win, image=Fbi, width=250, height=250)
l3.bind("<Button>", fbi)
l4 = tk.Label(win, image=steven, width=250, height=250)
l4.bind("<Button>", jesus)
l5 = tk.Label(win, image=screams, width=250, height=250)
l5.bind("<Button>", scream)
l6 = tk.Label(win, image=superidol, width=250, height=250)
l6.bind("<Button>", Superidol)
l7 = tk.Label(win, image=headshots, width=250, height=250)
l7.bind("<Button>", headshot)

l1.grid(row=1, column=2)
l2.grid(row=3, column=1)
l3.grid(row=3, column=2)
l4.grid(row=3, column=3)
l5.grid(row=4, column=1)
l6.grid(row=4, column=2)
l7.grid(row=4, column=3)


win.mainloop()