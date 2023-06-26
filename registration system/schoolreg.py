import tkinter 
from tkinter import *

def email_date_frame():
    global secondroot
    emailframe = Label(root,text="emmanuelseun078@gmail.com",width=20,height=3,bg="green",
                       fg="white",anchor="e").pack(side="top",fill=X)
    
    secondroot = LabelFrame(root,text="STUDENT DETAILS",bg="#4D4D4D",width=750,
                            height=320).place(x=60,y=120)
    
    frames()

def rselection():
    value = radio.get()
    if value == 1:
        gender = "Male"
        print(gender)
    else:
        gender = "Female"
        print(gender)

def vars():
    global firstname,middlename,lastname,dob,radio
    firstname = StringVar()
    middlename = StringVar()
    lastname = StringVar()
    dob = StringVar()
    radio = IntVar()
    
def frames():
    vars()
    
    namelabel = Label(secondroot,text="FIRSTNAME:",bg="#4D4D4D",fg="white",
                      font=("Arial",10)).place(x=90,y=140)
    
    nameentry = Entry(secondroot,width=22,font=("Arial",10),
                      textvariable=firstname).place(x=210,y=140)

    surnlabel = Label(secondroot,text="MIDDLENAME:",bg="#4D4D4D",fg="white",
                      font=("Arial",10)).place(x=90,y=190)
    
    surentry = Entry(secondroot,width=22,font=("Arial",10),
                      textvariable=middlename).place(x=210,y=190)

    lasnamelabel = Label(secondroot,text="LASTNAME:",bg="#4D4D4D",fg="white",
                      font=("Arial",10)).place(x=90,y=240)
    
    lasnamentry = Entry(secondroot,width=22,font=("Arial",10),
                      textvariable=lastname).place(x=210,y=240)
    
    doblabel = Label(secondroot,text="DATE OF BIRTH:",fg="white",
                     font=("Arial",10),bg="#4D4D4D").place(x=90,y=290)
    
    dopentry = Entry(secondroot,textvariable=dob,width=22,
                     font=("Arial",10)).place(x=210,y=290)
    
    genderframe = Label(secondroot,fg="white",text="GENDER",font=("Arial",10),
                        bg="#4D4D4D").place(x=90,y=340)
    
    gender1 =  Radiobutton(secondroot,text="Male",bg="#4D4D4D",value=1,command=rselection,
                           font=("Arial",12),variable=radio).place(x=170,y=340)
    
    gender2 =  Radiobutton(secondroot,text="Female",value=2,bg="#4D4D4D",command=rselection, 
                           font=("Arial",12),variable=radio).place(x=230,y=340)





root_bg = "#06283D"
if __name__=="__main__":
    root = Tk()
    root.title("SCHOOL REGISTER")
    root.geometry("1000x660+160+20")
    root.config(bg=root_bg)

    email_date_frame()
    

    root.mainloop()