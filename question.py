from tkinter import *
from tkinter import ttk
import turtle
import random

window = Tk()
window.configure(bg='black')
window.title("About The Ball")
window.geometry('1500x1000')
window.resizable(0,0)

but_loc_x=[200,600,1000]
but_loc_y=[200,350,600]

def thanks_flower():
    window.destroy()
    t = turtle.Turtle()
    w = turtle.Turtle()
    s = turtle.Screen()
    s.setup(700,800)
    s.bgcolor("black")
    t.pencolor("pink")
    w.pencolor('pink')
    t.speed(0)

    w.write('Thank You!\n(*^▽^*)',font=("Courier",70,'bold'),align='center')
    w.penup
    w.hideturtle()
    t.hideturtle()

    t.goto(0,-190)

    valid = True
    while valid == True:
        for i in range(155):
            t.circle(190-i,90)
            t.lt(90)
            t.circle(190-i,90)
            t.lt(18)

def sad():
    window.destroy()
    w = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    w.pencolor('pink')

    w.write('ME:\n(┬┬﹏┬┬)',font=("Courier",70,'bold'),align='center')
    w.penup
    w.hideturtle()


def onLeave(event):
    button2.config(bg='white')
 
def onEnter(event):
    button2.config(bg='red')
 
def onEnter2(event):
    button1.config(bg='green')
def onLeave2(event):
    button1.config(bg='white')

def button_hover(event):
    window.after(50)
    but_pos_x=random.choice(but_loc_x)
    but_pos_y=random.choice(but_loc_y)

    button2.place_configure(x=but_pos_x,y=but_pos_y)
    
#def unhover(event):
    #window.after(500)
    #button2.place_configure(x=600,y=350)

label1 = Label(window, text="Will You Go To Ball With Me?",font=("Courier",15,'bold'),fg="pink",bg='black')

button1 = Button(window,text="Yes",font=("Courier",15,'bold'),fg="pink",bg='white',command=thanks_flower)

button2 = Button(window,text="    No    ",font=("Courier",15,'bold'),fg="pink",bg='white',command=sad)

label1.grid(row=0,column=0,columnspan=7,padx=500,pady=30,sticky="WE")
button1.grid(row=1,column=2,padx=350,pady=20,sticky='WE')
button2.grid(row=2,column=2,padx=350,pady=20,sticky='WE')
button2.bind('<Leave>', onLeave)
button2.bind('<Enter>', onEnter)
button1.bind('<Leave>', onLeave2)
button1.bind('<Enter>', onEnter2)
button2.bind("<Enter>",button_hover)
#button2.bind("<Leave>",unhover)

window.mainloop()