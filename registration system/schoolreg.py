import tkinter 
from tkinter import *
from tkinter import ttk
# from tkinter import Image,image_types
from PIL import Image,ImageTk
from datetime import date




def email_date_frame():
    global secondroot
    emailframe = Label(root,text="emmanuelseun078@gmail.com",width=20,height=3,bg="green",
                       fg="white",anchor="e").pack(side="top",fill=X)
    
    schoolimgframe = Label(root,width=320,height=180,image=scchool_image).place(x=640,y=70)
    
    secondroot = LabelFrame(root,text="STUDENT DETAILS",bg="#4D4D4D",width=750,
                            height=320).place(x=60,y=280)
    
    
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
    global firstname,middlename,lastname,dob,radio,da_te
    firstname = StringVar()
    middlename = StringVar()
    lastname = StringVar()
    dob = StringVar()
    radio = IntVar()
    da_te = StringVar()




def showdate():
    global tdaysdate
    ti_me = date.today()
    tdaysdate = ti_me.strftime("%d/%m/%Y")


    
def combovalues():
    global deparments,classes
    deparments = ("SCIENCE",
                 "COMMERCIAL",
                 "ART")
    classes = ("JS1",
               "JS2",
               "JS3",
               "SS1",
               "SS2",
               "SS3")


def frames():
    combovalues()
    vars()
    showdate()
    
    namelabel = Label(master=secondroot,text="FIRSTNAME",bg="#4D4D4D",fg="white",
                      font=("Arial",10)).place(x=90,y=330)
    
    nameentry = Entry(secondroot,width=22,font=("Arial",10),
                      textvariable=firstname).place(x=210,y=330)

    surnlabel = Label(secondroot,text="MIDDLENAME",bg="#4D4D4D",fg="white",
                      font=("Arial",10)).place(x=90,y=380)
    
    surentry = Entry(secondroot,width=22,font=("Arial",10),
                      textvariable=middlename).place(x=210,y=380)

    lasnamelabel = Label(secondroot,text="LASTNAME",bg="#4D4D4D",fg="white",
                      font=("Arial",10)).place(x=90,y=430)
    
    lasnamentry = Entry(secondroot,width=22,font=("Arial",10),
                      textvariable=lastname).place(x=210,y=430)
    
    doblabel = Label(secondroot,text="DATE OF BIRTH",fg="white",
                     font=("Arial",10),bg="#4D4D4D").place(x=90,y=480)
    
    dopentry = Entry(secondroot,textvariable=dob,width=22,
                     font=("Arial",10)).place(x=210,y=480)
    
    genderframe = Label(secondroot,fg="white",text="GENDER",font=("Arial",10),
                        bg="#4D4D4D").place(x=90,y=530)
    
    gender1 =  Radiobutton(secondroot,text="Male",bg="#4D4D4D",value=1,command=rselection,
                           font=("Arial",12),variable=radio).place(x=170,y=530)
    
    gender2 =  Radiobutton(secondroot,text="Female",value=2,bg="#4D4D4D",command=rselection, 
                           font=("Arial",12),variable=radio).place(x=230,y=530)

    departlabel = Label(root,text="DEPARTMENT",font=("Arial",10),
                        fg="white",bg="#4D4D4D").place(x=460,y=330)

    depatcombo = ttk.Combobox(root,values=deparments,width=13).place(x=560,y=330)

    class_frame = Label(master=secondroot,text="CLASS",font=("Arial",10),
                        bg="#4D4D4D",fg="white").place(x=460,y=380)
    
    classescombo = ttk.Combobox(master=secondroot,values=classes,width=12).place(x=560,y=380)

    dateframe = Label(master=root,width=12,font=("Arial",10),textvariable=da_te,fg="white",bg=root_bg).pack(anchor="se",padx=10,side="bottom")
    
    da_te.set(tdaysdate)



root_bg = "#06283D"
if __name__=="__main__":
    root = Tk()
    root.title("SCHOOL REGISTER")
    root.geometry("1000x660+160+20")
    root.config(bg=root_bg)
    root.iconbitmap("images.ico")

    scchool_image = ImageTk.PhotoImage(Image.open("registration system//sch_image.png").resize((320,180)))

    email_date_frame()    

    root.mainloop()