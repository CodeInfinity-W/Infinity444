import tkinter
from tkinter import*

win = Tk()
win.geometry('500x500')
win.title("Technoblade")

nav_Frame = Frame(win, width=100, height=100, bg = "purple")
nav_Frame.place(relx = 0.1, rely = 0.1)

second_Frame = Frame(win, width=100, height=100, bg="purple")
second_Frame.place(relx = 0.4, rely = 0.1)

third_Frame = Frame(win, width=100, height=100,bg="purple")
third_Frame.place(relx = 0.7, rely = 0.1)

fourth_Frame = Frame(win, width=100, height=100,bg="gold")
fourth_Frame.place(relx = 0.1, rely = 0.4)

fifth_Frame = Frame(win, width=100, height=100,bg="gold")
fifth_Frame.place(relx = 0.4, rely = 0.4)

sixth_Frame = Frame(win, width=100, height=100,bg="gold")
sixth_Frame.place(relx = 0.7, rely = 0.4)

seventh_Frame = Frame(win, width=100, height=100,bg="black")
seventh_Frame.place(relx = 0.1, rely = 0.7)

eigth_Frame = Frame(win, width=100, height=100,bg="black")
eigth_Frame.place(relx = 0.4, rely = 0.7)

ninth_Frame = Frame(win, width=100, height=100,bg="black")
ninth_Frame.place(relx = 0.7, rely = 0.7)
win.mainloop()