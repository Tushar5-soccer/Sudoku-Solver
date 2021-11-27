from tkinter import *


root=Tk()
root.title("Thank You Page")
root.geometry("600x300")
root.resizable(False, False)
root.configure(bg="black")

Label(root, text="Thnak You",bg="goldenrod1",fg="black", font=15).pack(fill=BOTH)
Label(root, text="Admission is Complete \n Thank you for becoming a part of our college.",bg="goldenrod1",font=25,fg="black").place(x=100,y=120)
