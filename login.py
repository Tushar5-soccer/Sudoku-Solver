from tkinter import *
from tkinter import messagebox

def login():
    name=entry1.get()
    im=entry2.get()
    cc=entry3.get()
    if(name=="" or im=="" or cc==""):
        messagebox.showerror("ERROR", "Blank form not allowed. \n Enter again.")
    else:
        r1=messagebox.askyesno("LOGIN", "The name you entered is "+ name )
        r2=messagebox.askyesno("LOGIN", "The Intermetiate marks you entered is "+ im)
        r3=messagebox.askyesno("LOGIN", "The Course Code you entered is "+ cc )
        if(r1==0 or r2==0 or r3==0):
            messagebox.showerror("ERROR", "Login Failed ")
        else:
            check(name,im,cc)

def check_float(ip):
    try:
        float(ip)
        return True
    except ValueError:
        return False

def check_int(it):
    try:
        int(it)
        return True
    except ValueError:
        return False
                
def check(z,a,b):
    x=a
    y=b

    if(check_float(x) and check_int(y)):
        c1=float(x)
        c2=int(y)
        if(c2==1):
            if(c1>=75.0 and c1<=100.0):
                messagebox.showinfo("Info", "Fill other details \n Your course is B.TECH")
                f= open("Sdatabase.txt","a")
                f.write(z+" "+x+" B.TECH ")
                f.close()
                pDetails()
            else:
                messagebox.showerror("ERROR", "Intermediate Marks does not requirement \n We are sorry.")
        elif(c2==2):
            if(c1>=75.0 and c1<=100.0 and c1<=100.0):
                messagebox.showinfo("Info", "Fill other details \n Your course is B.SC")
                f= open("Sdatabase.txt","a")
                f.write(z+" "+x+" B.SC ")
                f.close()
                pDetails()
            else:
                messagebox.showerror("ERROR", "Intermediate Marks does not requirement \n We are sorry.")
        elif(c2==3):
            if(c1>=60.0 and c1<=100.0):
                messagebox.showinfo("Info", "Fill other details \n Your course is B.ARCH")
                f= open("Sdatabase.txt","a")
                f.write(z+" B.ARCH ")
                f.close()
                pDetails()
            else:
                messagebox.showerror("ERROR", "Intermediate Marks does not requirement \n We are sorry.")
        elif(c2==4):
            if(c1>=60.0 and c1<=100.0):
                messagebox.showinfo("Info", "Fill other details \n Your course is BCA")
                f= open("Sdatabase.txt","a")
                f.write(z+" "+x+" BCA ")
                f.close()
                pDetails()
            else:
                messagebox.showerror("ERROR", "Intermediate Marks does not requirement \n We are sorry.")
        elif(c2==5):
            if(c1>=65.0 and c1<=100.0):
                messagebox.showinfo("Info", "Fill other details \n Your course is BPharma")
                f= open("Sdatabase.txt","a")
                f.write(z+" "+x+" BPharma ")
                f.close()
                pDetails()
            else:
                messagebox.showerror("ERROR", "Intermediate Marks does not requirement \n We are sorry.")
        elif(c2==6):
            if(c1>=65.0 and c1<=100.0):
                messagebox.showinfo("Info", "Fill other details \n Your course is B.COM")
                f= open("Sdatabase.txt","a")
                f.write(z+" "+x+" B.COM ")
                f.close()
                pDetails()
            else:
                messagebox.showerror("ERROR", "Intermediate Marks does not requirement \n We are sorry.")
        elif(c2==7):
            if(c1>=65.0 and c1<=100.0):
                messagebox.showinfo("Info", "Fill other details \n Your course is BBA")
                f= open("Sdatabase.txt","a")
                f.write(z+" "+x+" BBA ")
                f.close()
                pDetails()
            else:
                messagebox.showerror("ERROR", "Intermediate Marks does not requirement \n We are sorry.")
        elif(c2==8):
            if(c1>=60.0 and c1<=100.0):
                messagebox.showinfo("Info", "Fill other details \n Your course is B.Design")
                f= open("Sdatabase.txt","a")
                f.write(z+" "+x+" B.Design ")
                f.close()
                pDetails()
            else:
                messagebox.showerror("ERROR", "Intermediate Marks does not requirement \n We are sorry.")
        elif(c2==9):
            if(c1>=65.0 and c1<=100.0):
                messagebox.showinfo("Info", "Fill other details \n Your course is BBS")
                f= open("Sdatabase.txt","a")
                f.write(z+" "+x+" BBS ")
                f.close()
                pDetails()
            else:
                messagebox.showerror("ERROR", "Intermediate Marks does not requirement \n We are sorry.")
        else:
            messagebox.showerror("ERROR", "Input Error \n Wrong Course Code ")
    else:
        messagebox.showerror("ERROR", "Input Error \n Either Wrong Intemediate marks or Wrong Course Code ")





def ccode():
    messagebox.showinfo("Course Code Details", "B.TECH = 01 \n B.SC   = 02 \n B.ARCH = 03 \n BCA   = 04 \n BPharma = 05 \n B.COM  = 06 \n BBA   = 07 \n B.Design = 08 \n BBS = 09")

def dobinfo():
    messagebox.showinfo("DOB Info", "Format for DOB is \n DD/MM/YYYY")

def clear1():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    
def clear2():
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(0,END)
    entry9.delete(0,END)
    entry10.delete(0,END)


def sInfo():  
    fname=entry4.get()
    mname=entry5.get()
    dob=entry6.get()
    ac=entry7.get()
    pn=entry8.get()
    em=entry9.get()
    add=entry10.get()
    if(fname=="" or mname=="" or dob=="" or ac=="" or pn=="" or em=="" or add==""):
         messagebox.showerror("ERROR", "Blank form not allowed. \n Enter again.")
    else:
        if(len(ac)==12 and len(pn)==10 ):
            f= open("Sdatabase.txt","a")
            f.write(fname+" "+mname+" "+dob+" "+ac+" "+pn+" "+em+" "+add+" ")
            f.close()
            messagebox.showinfo("Completion", "Admission Completed \n You can exit now.")
            root.destroy()

        else:
            messagebox.showerror("ERROR", "Input Error. \n Enter again.")
    
def pDetails():
    root1=Tk()
    root1.title("Personal Details")
    root1.geometry("600x450")
    root1.resizable(False, False)
    root1.configure(bg="black")

    global entry4
    global entry5
    global entry6
    global entry7
    global entry8
    global entry9
    global entry10
    
    Label(root1, text="Personal Details",bg="goldenrod1",fg="black", font=15).pack(fill=BOTH)
    Label(root1, text="Father's Name",bg="goldenrod1",fg="black").place(x=170,y=80)
    Label(root1, text="Mother's Name",bg="goldenrod1",fg="black").place(x=170,y=120)
    Label(root1, text="Date of Birth",bg="goldenrod1",fg="black").place(x=170,y=160)
    Label(root1, text="Aadhar Card No.",bg="goldenrod1",fg="black").place(x=170,y=200)
    Label(root1, text="Phone No.",bg="goldenrod1",fg="black").place(x=170,y=240)
    Label(root1, text="E-mail Address",bg="goldenrod1",fg="black").place(x=170,y=280)
    Label(root1, text="Address",bg="goldenrod1",fg="black").place(x=170,y=320)
    entry4=Entry( root1,bd=4)
    entry4.place(x=300 ,y=80)
    
    entry5=Entry (root1, bd = 4)
    entry5.place( x=300,y=120)

    entry6=Entry (root1, bd = 4)
    entry6.place( x=300,y=160)
    
    entry7=Entry (root1, bd = 4)
    entry7.place( x=300,y=200)

    entry8=Entry (root1, bd = 4)
    entry8.place( x=300,y=240)

    entry9=Entry (root1, bd = 4)
    entry9.place( x=300,y=280)
    
    entry10=Entry(root1,width=30, bd=4)
    entry10.place(x=300,y=320)

    Button(root1,text="Save",bg="goldenrod1",fg="black",command=sInfo,height=1,width=6,bd=4).place(x=180,y=400)
    Button(root1,text="Clear",bg="goldenrod1",fg="black",command=clear2,height=1,width=6,bd=4).place(x=260,y=400)
    Button(root1,text="DOB info",bg="goldenrod1",fg="black",command=dobinfo,height=1,width=6,bd=4).place(x=340,y=400)


root=Tk()
root.title("Online College Adimmison Portal Login")
root.geometry("600x400")
root.resizable(False, False)
root.configure(bg="black")

global entry1
global entry2
global entry3
global cc

Label(root, text="LOGIN to College",bg="goldenrod1",fg="black", font=15).pack(fill=BOTH)
Label(root, text="Name",bg="goldenrod1",fg="black").place(x=170,y=120)
Label(root, text="Intermediate marks",bg="goldenrod1",fg="black").place(x=170,y=160)
Label(root, text="Course Code",bg="goldenrod1",fg="black").place(x=170,y=200)

entry1=Entry( root,bd=4)
entry1.place(x=300 ,y=120)

entry2=Entry (root, bd = 4)
entry2.place( x=300,y=160)

entry3=Entry (root, bd = 4)
entry3.place( x=300,y=200)

Button(root,text="Next",bg="goldenrod1",fg="black",command=login,height=1,width=6,bd=4).place(x=180,y=280)
Button(root,text="Clear",bg="goldenrod1",fg="black",command=clear1,height=1,width=6,bd=4).place(x=260,y=280)
Button(root,text="Course Code Details",bg="goldenrod1",fg="black",command=ccode,height=1,width=16,bd=4).place(x=340,y=280)


root.mainloop()
