import playsound as p
import tkinter as tk 
from tkinter import *
from tkinter import ttk

def baby(event):
    print(event)
    p.playsound("Justin Bieber - Baby ft.Ludacris.mp3")
    
def Superidol(event):
    print(event)
    p.playsound("Super Idol 的笑容都没你的甜( Meme Sound Effect )( Creator Sound Effect ).mp3")

def headshot(event):
    print(event)
    p.playsound("headshot_1.mp3")
    
def scream(event):
    print(event)
    p.playsound("insane-funny-scream-199845.mp3")
    
def cat(event):
    print(event)
    p.playsound("funny-meow-110120.mp3")


win = tk.Tk()
win.attributes('-topmost',True)
Bieber = PhotoImage(file="Bieber.png")
cats = PhotoImage(file="cat.png")
headshots = PhotoImage(file="headshot.png")
screams = PhotoImage(file="scream.png")
superidol = PhotoImage(file="Superidol.png")


l1 = tk.Label(win,text="Press any image to play a sound")
l2 = tk.Label(win, image=Bieber )
l2.bind("<Button>",baby)
l3 = tk.Label(win, image=Superidol )
l3.bind("<Button>",)

l1.pack()
b1.pack()
l2.pack()
b2.pack()

win.mainloop()