from tkinter import *
from tkinter import messagebox
import re
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="admin5007",
database="admission"
)
mycur=mydb.cursor()


################## #p1
global entry1 #name
global name
global entry2 #email
global email
global entry3 #password
global password
global entry4 #confirmpassword
global cpassword

################## #p2
global entry5 #12marks
global marks12
global entry6 #coursecode
global cc

################## #p3
global entry7 #fathername
global fname
global entry8 #mothername
global mname
global entry9d #date
global dobd
global entry9d #month
global dobm
global entry9d #year
global doby
global entry10 #gender
global gender 
global entry11 #adharcardno
global adhar
global entry12 #pnumber
global pnum
global entry13 #address
global address

################################ #Personal_Detail_Page3


def check_float(ip):
    try:
        float(ip)
        return True
    except ValueError:
        return False




################################ #Course_Page2



def checkid(em):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,em)):
        return 1
    else:
        return 0


def login():
    
    def clear2():
        entry5.delete(0,END)

    
    name=entry1.get()
    email=entry2.get()
    password=entry3.get()
    cpassword=entry4.get()
    if(name=="" or email=="" or password=="" or cpassword=="" ):
        messagebox.showerror("ERROR", "Blank form not allowed. \n Enter again.")
    elif(checkid(email)==0):
        messagebox.showerror("ERROR", "Invalid Email Address. \n Enter again.")
    elif(len(password) != 8):
        messagebox.showerror("ERROR", "Password too small. \n Enter again.")
    elif(password != cpassword):
        messagebox.showerror("ERROR", "Password does not match. \n Enter again.")
    elif(password==name):
        messagebox.showerror("ERROR", "Password and name can not be same.  \n Enter again.")
    else:
        root1=Tk()
        root1.title("Courses")
        root1.geometry("600x350")
        root1.resizable(False, False)
        root1.configure(bg="black")

        options = [
            "B.Tech",
            "B.Com",
            "B.Sc",
            "B.Arts",
            "B.Business Administration",
            "B.Pharma",
            "B.Design",
            "B.Computer Application",
            "B.Arch",
            "B.Business Studies",
        ]
        
        Label(root1, text="Course Details",bg="goldenrod1",fg="black", font=15).pack(fill=BOTH)
        Label(root1, text="Intermediate Marks",bg="goldenrod1",fg="black").place(x=170,y=100)
        Label(root1, text="Course Required",bg="goldenrod1",fg="black").place(x=170,y=180)

        entry5=Entry( root1,bd=4)
        entry5.place(x=300 ,y=100)

        entry6= StringVar()
        drop = OptionMenu( root1, entry6 , *options).place(x=300,y=180)
        

        def login1():

            def checkmarks(y):
                def login2():
                        
                    def save():
                        def check_int(it):
                            try:
                                int(it)
                                return True
                            except ValueError:
                                return False

                        
                        fname=entry7.get()
                        mname=entry8.get()
                        dobd=entry9d.get()
                        dobm=entry9m.get()
                        doby=entry9y.get()
                        gender=entry10.get()
                        adhar=entry11.get()
                        pnum=entry12.get()
                        address=entry13.get()
                        
                        if(fname=="" or mname=="" or dobd=="" or dobm =="" or doby=="" or gender=="" or adhar=="" or pnum=="" or address==""):
                            messagebox.showerror("ERROR", "Blank form not allowed. \n Enter again.")
                        elif(check_int(dobd)== False or check_int(dobm)== False or check_int(doby)== False or len(dobd)!=2 or len(dobm) !=2 or len(doby)!=4):
                            messagebox.showerror("ERROR", "Invalid Date of Birth. \n Enter again.")
                        else:
                            d= int(dobd)
                            m= int(dobm)
                            y= int(doby)
                            if(len(adhar)!=12 or len(pnum)!=10 or check_int(adhar)== False or check_int(pnum)== False ):
                                messagebox.showerror("ERROR", "Invalid Phone Number or Aadhar Card Number. \n Enter again.")
                            else:
                                if(y%4==0):
                                    if((y<1980 or y>2006) or (m<1 or m>12) or ((m==4 or m==6 or m==9 or m==11)and (d<1 or d>30)) or ((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and (d<1 or d>31)) or (m==2 and d>29)):
                                        messagebox.showerror("ERROR", "Invalid Date of Birth. \n Enter again.")
                                    else:
                                        dob=dobd+"/"+dobm+"/"+doby
                                        sql="INSERT INTO project(name , email , password , marks12 , cc , fname , mname , dob , gender , adhar , pnum , address)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                        val=(name, email, password, marks12, cc, fname, mname, dob, gender, adhar, pnum, address)
                                        mycur.execute(sql,val)
                                        mydb.commit()
                                        root.destroy()
                                        root1.destroy()
                                        root2.destroy()
                                        import thankYou
                                        
                                else:
                                    if((y<1980 or y>2006) or (m<1 or m>12) or ((m==4 or m==6 or m==9 or m==11)and (d<1 or d>30)) or ((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and (d<1 or d>31)) or (m==2 and d>28)):
                                        messagebox.showerror("ERROR", "Invalid Date of Birth. \n Enter again.")
                                    else:
                                        dob=dobd+"/"+dobm+"/"+doby
                                        sql="INSERT INTO project(name , email , password , marks12 , cc , fname , mname , dob , gender , adhar , pnum , address)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                        val=(name, email, password, marks12, cc, fname, mname, dob, gender, adhar, pnum, address)
                                        mycur.execute(sql,val)
                                        mydb.commit()
                                        root.destroy()
                                        root1.destroy()
                                        root2.destroy()
                                        import thankYou
                            
                                
                            


                    
                    def clear3():
                        entry7.delete(0,END)
                        entry8.delete(0,END)
                        entry11.delete(0,END)
                        entry12.delete(0,END)
                        entry13.delete(0,END)


                    root2=Tk()
                    root2.title("Personal Details")
                    root2.geometry("600x500")
                    root2.resizable(False, False)
                    root2.configure(bg="black")
                    option = [
                        "Male",
                        "Female",
                        "Others",
                        ]
                    
                    
                    Label(root2, text="Personal Details",bg="goldenrod1",fg="black", font=15).pack(fill=BOTH)
                    Label(root2, text="Father Name",bg="goldenrod1",fg="black").place(x=170,y=80)
                    Label(root2, text="Mother Name",bg="goldenrod1",fg="black").place(x=170,y=120)
                    Label(root2, text="Date Of Birth",bg="goldenrod1",fg="black").place(x=170,y=160)
                    Label(root2, text="DD",bg="goldenrod1",fg="black").place(x=305,y=200)
                    Label(root2, text="MM",bg="goldenrod1",fg="black").place(x=345,y=200)
                    Label(root2, text="YYYY",bg="goldenrod1",fg="black").place(x=385,y=200)
                    Label(root2, text="Gender",bg="goldenrod1",fg="black").place(x=170,y=240)
                    Label(root2, text="Aadhar Card No",bg="goldenrod1",fg="black").place(x=170,y=280)
                    Label(root2, text="Phone No",bg="goldenrod1",fg="black").place(x=170,y=320)
                    Label(root2, text="Address",bg="goldenrod1",fg="black").place(x=170,y=360)

                    entry7=Entry( root2,bd=4)
                    entry7.place(x=300 ,y=80)

                    entry8=Entry( root2,bd=4)
                    entry8.place(x=300 ,y=120)

                    entry9d=Entry( root2,width=5, bd=4)
                    entry9d.place(x=300,y=160)

                    entry9m=Entry( root2,width=5, bd=4)
                    entry9m.place(x=340,y=160)

                    entry9y=Entry( root2,width=6, bd=4)
                    entry9y.place(x=380,y=160)

                    entry10=StringVar()
                    drop = OptionMenu( root2, entry10 , *option).place(x=300,y=240)

                    entry11=Entry( root2,bd=4)
                    entry11.place(x=300 ,y=280)

                    entry12=Entry( root2,bd=4)
                    entry12.place(x=300 ,y=320)

                    entry13=Entry( root2,width = 40 ,bd=4)
                    entry13.place(x=300 ,y=360)

                    Button(root2,text="Save",bg="goldenrod1",fg="black",command=save,height=1,width=6,bd=4).place(x=220,y=450)
                    Button(root2,text="Clear",bg="goldenrod1",fg="black",command=clear3,height=1,width=6,bd=4).place(x=300,y=450)

                    
                    

                    
                    
                if(cc=="B.Tech"):
                    if(y>=75.0 and y<=100.0):
                        login2()
                    else:
                        messagebox.showerror("ERROR", "Intermediate Marks not up to requirement \n We are sorry.")
                elif(cc=="B.Com"):
                    if(y>=65.0 and y<=100.0):
                        login2()
                    else:
                        messagebox.showerror("ERROR", "Intermediate Marks not up to requirement \n We are sorry.")
                elif(cc=="B.Sc"):
                    if(y>=75.0 and y<=100.0):
                        login2()
                    else:
                        messagebox.showerror("ERROR", "Intermediate Marks not up to requirement \n We are sorry.")
                elif(cc=="B.Arts"):
                    if(y>=60.0 and y<=100.0):
                        login2()
                    else:
                        messagebox.showerror("ERROR", "Intermediate Marks not up to requirement \n We are sorry.")
                elif(cc=="B.Business Administration"):
                    if(y>=65.0 and y<=100.0):
                        login2()
                    else:
                        messagebox.showerror("ERROR", "Intermediate Marks not up to requirement \n We are sorry.")
                elif(cc=="B.Pharma"):
                    if(y>=65.0 and y<=100.0):
                        login2()
                    else:
                        messagebox.showerror("ERROR", "Intermediate Marks not up to requirement \n We are sorry.")
                elif(cc=="B.Design"):
                    if(y>=60.0 and y<=100.0):
                        login2()
                    else:
                        messagebox.showerror("ERROR", "Intermediate Marks not up to requirement \n We are sorry.")
                elif(cc=="B.Computer Application"):
                    if(y>=70.0 and y<=100.0):
                        login2()
                    else:
                        messagebox.showerror("ERROR", "Intermediate Marks not up to requirement \n We are sorry.")
                elif(cc=="B.Arch"):
                    if(y>=65.0 and y<=100.0):
                        login2()
                    else:
                        messagebox.showerror("ERROR", "Intermediate Marks not up to requirement \n We are sorry.")
                elif(cc=="B.Business Studies"):
                    if(y>=65.0 and y<=100.0):
                        login2()
                    else:
                        messagebox.showerror("ERROR", "Intermediate Marks not up to requirement \n We are sorry.")
                else:
                    messagebox.showerror("ERROR", "Invalid Course selection. \n We are sorry.")

               
                
            marks12=entry5.get()
            cc=entry6.get()
            if(marks12=="" or cc==""):
                messagebox.showerror("ERROR", "Blank form not allowed. \n Enter again.")
            elif(check_float(marks12)):
                x=float(marks12)
                checkmarks(x)
            else:
                messagebox.showerror("ERROR", "Input Error \n Invalid Intemediate marks.")
                
            

        Button(root1,text="Next",bg="goldenrod1",fg="black",command=login1,height=1,width=6,bd=4).place(x=220,y=280)
        Button(root1,text="Clear",bg="goldenrod1",fg="black",command=clear2,height=1,width=6,bd=4).place(x=300,y=280)

        


#################### #Login_Page1

def clear1():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)


root=Tk()
root.title("Online College Adimmison Portal Login")
root.geometry("600x400")
root.resizable(False, False)
root.configure(bg="black")

Label(root, text="Login to College",bg="goldenrod1",fg="black", font=15).pack(fill=BOTH)
Label(root, text="Name",bg="goldenrod1",fg="black").place(x=170,y=100)
Label(root, text="E-mail Address",bg="goldenrod1",fg="black").place(x=170,y=140)
Label(root, text="Password ",bg="goldenrod1",fg="black").place(x=170,y=180)            
Label(root, text="Confirm Password ",bg="goldenrod1",fg="black").place(x=170,y=220)

entry1=Entry( root,bd=4)
entry1.place(x=300 ,y=100)

entry2=Entry (root, bd = 4)
entry2.place( x=300,y=140)

entry3=Entry (root,show="*", bd = 4)
entry3.place( x=300,y=180)

entry4=Entry (root,show="*", bd = 4)
entry4.place( x=300,y=220)


Button(root,text="Next",bg="goldenrod1",fg="black",command=login,height=1,width=6,bd=4).place(x=220,y=280)
Button(root,text="Clear",bg="goldenrod1",fg="black",command=clear1,height=1,width=6,bd=4).place(x=300,y=280)






