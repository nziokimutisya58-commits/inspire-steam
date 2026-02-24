from tkinter import *

def Hello():
    print("hello from mother fuckin")


root = Tk()
root.geometry("600x600")
Frame_one = Frame(root)
Frame_one.pack()

button_one = Button(Frame_one,text="say Hello",command = Hello)
root,mainloop()
