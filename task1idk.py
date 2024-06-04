import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound as p

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

fbis=PhotoImage(file="Fbi.png")
steven=PhotoImage(file="Steven.png")
screams=PhotoImage(file="scream.png")
superidol=PhotoImage(file="superidol.png")
headshots=PhotoImage(file="headshot.png")
gegas=PhotoImage(file="gega.png")



l1 = tk.Label(win,text="Press any image to play a sound")
l2 = tk.Label(win, image=gegas)
l2.bind("<Button>",gega)
l3 = tk.Label(win, image=fbis)
l3.bind("<Button>", fbi)
l4 = tk.Label(win, image=steven)
l4.bind("<Button>", jesus)
l5 = tk.Label(win, image=screams)
l5.bind("<Button>", scream)
l6 = tk.Label(win, image=superidol)
l6.bind("<Button>", Superidol)
l7 = tk.Label(win, image=headshots)
l7.bind("<Button>", headshot)

l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
l6.pack()
l7.pack()


win.mainloop()