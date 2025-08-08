from tkinter import *
import os

import time

w=Tk()
w.geometry("2000x2000")
w.attributes('-fullscreen',True)
def dest():
    os.system('login.py')
    w.destroy()


i = PhotoImage(file="t5.png")
c = Label(w,image=i)
c.place(x=-300,y=-175)

q = Label(w,text='Welcome to Criminals Record Managment System ',bg="#001024", font=("Arial", 43, "bold"), fg="orange"  )
q.place(x=0,y=0)

wd='''This platform is designed to streamline and enhance the
efficiency of law enforcement operations. With powerful
tools for case management, suspect profiling,
investigation tracking, and data analysis, our system
ensures that justice is served with precision and speed.
The intuitive interface and robust security measure
guarantee that sensitive information remains
protected at all times.'''

q = Label(w,text=wd,bg="#001024", font=("Arial", 20, "bold"), fg="white"  )
q.place(x=6,y=120)
q1 = Button(w,text='Tap Here to Sign up ',command=dest,bg="#001024", font=("Arial", 23, "bold"), fg="orange"  )
q1.place(x=110,y=460)
q2=Label(w,text='Create an account to continue to continue',bg="#001024", font=("Arial", 25, "bold"), fg="silver" )
q2.place(x=10,y=400)
q3=Label(w,text='Already a user? Tap here to login ',bg="#001024", font=("Arial", 25, "bold"), fg="silver" )
q3.place(x=10,y=550)
q4 = Button(w,text='Login With Your Username ',command=dest,bg="orange", font=("Arial", 23, "bold"), fg="white"  )
q4.place(x=50,y=610)
w.mainloop()