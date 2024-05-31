import playsound as p
import tkinter as tk 
from tkinter import *
from tkinter import ttk

def gega(event):
    print(event)
    p.playsound("Sound_Effects/Gegagedigedagedago Meme Sound Effect.mp3")
    
def Superidol(event):
    print(event)
    p.playsound("Sound_Effects/Super Idol 的笑容都没你的甜( Meme Sound Effect )( Creator Sound Effect ).mp3")

def fbi(event):
    print(event)
    p.playsound("Sound_Effects/FBI Open Up Meme - Sound Effect (HD).mp3")
    
def scream(event):
    print(event)
    p.playsound("Sound_Effects/insane-funny-scream-199845.mp3")
    
def jesus(event):
    print(event)
    p.playsound("Sound_Effects/Steven He - I Will Send You To Jesus.mp3")

def headshot(event):
    print(event)
    p.playsound("Sound_Effects/headshot_1.mp3")

win = tk.Tk()
win.attributes('-topmost',True)
gegag = PhotoImage(file="Image/gega.png")
fbis = PhotoImage(file="Image/fbi.png")
steven = PhotoImage(file="Image/Steven.png")
screams = PhotoImage(file="Image/scream.png")
superidol = PhotoImage(file="Image/Superidol.png")
headshots = PhotoImage(file="Image/headshot.png")


l1 = tk.Label(win,text="Press any image to play a sound")
l2 = tk.Label(win, image=gegag, width=50)
l2.bind("<Button>",gega)
l3 = tk.Label(win, image=fbis, width=50)
l3.bind("<Button>", fbi)
l4 = tk.Label(win, image=steven, width=50)
l4.bind("<Button>", jesus)
l5 = tk.Label(win, image=screams, width=50)
l5.bind("<Button>", scream)
l6 = tk.Label(win, image=superidol, width=50)
l6.bind("<Button>", Superidol)
l7 = tk.Label(win, image=headshots, width=50)
l7.bind("<Button>", headshot)

l1.grid(row=1, column=2)
l2.grid(row=2, column=1)
l3.grid(row=2, column=2)
l4.grid(row=2, column=3)
l5.grid(row=3, column=1)
l6.grid(row=3, column=2)
l7.grid(row=3, column=3)


win.mainloop()