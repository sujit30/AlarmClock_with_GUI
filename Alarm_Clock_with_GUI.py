import datetime
from tkinter import *
from playsound import playsound
root=Tk()
root.title("Alarm Clock")
root.geometry("700x300")
root.configure(bg="cyan")
Label(root,text="When do you want to be waken up???",font=("Times",14,'bold'),fg="red",bg="cyan").grid(row=0,column=1)
Label(root,text="Enter time in hours(24-hour format): ",bg="cyan").grid(row=1,column=0)
Label(root,text="Enter time in minutes: ",bg="cyan").grid(row=2,column=0,sticky=W)
a=IntVar()
b=IntVar()
Entry(root,textvariable=a).grid(row=1,column=1,sticky=W)
Entry(root,textvariable=b).grid(row=2,column=1,sticky=W)
def Wake():
    print("Waking you up at",a.get(),".",b.get())
    while True:
        if((a.get()==datetime.datetime.now().hour) and (b.get()==datetime.datetime.now().minute)):
            print("Wake up")
            playsound("alarm2.mp3")
            break
Button(root,text="Wake Me Up",command=Wake).grid(row=3,column=1,sticky=W)
root.mainloop()