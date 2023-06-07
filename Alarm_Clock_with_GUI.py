import datetime
from tkinter import *
from playsound import playsound
root=Tk()
root.geometry("500x500")
root.configure(bg="cyan")
Label(root,text="When do you want to be waken up???").grid(row=0,column=0)
Label(root,text="Enter time in hours: ").grid(row=1,column=0)
Label(root,text="Enter time in minutes: ").grid(row=2,column=0)
a=IntVar()
b=IntVar()
Entry(root,textvariable=a).grid(row=1,column=1)
Entry(root,textvariable=b).grid(row=2,column=1)

def Wake():
    print("Waking you up at",a.get(),".",b.get())
    while True:
        if((a.get()==datetime.datetime.now().hour) and (b.get()==datetime.datetime.now().minute)):
            print("Wake up")
            playsound("alarm2.mp3")
            break
Button(root,text="Wake Me Up",command=Wake).grid(row=3,column=1)
root.mainloop()