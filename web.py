# import webbrowser
# import tempfile
# import urllib.request
# import urllib.parse
# import re
# from tkinter import *
# from tkinter.colorchooser import *
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename





# class Browser:
#     """This creates a relay that allows a user to directly view data sent from a web server."""
#     def __init__(self, master):
#         """Sets up a browsing session."""
#         # Explicit global declarations are used to allow certain variable to be used in all methods.
#         global e1

#         # Here we create some temporary settings that allow us to create a client that ignores proxy settings.
#         self.proxy_handler = urllib.request.ProxyHandler(proxies=None)
#         self.opener = urllib.request.build_opener(self.proxy_handler)

#         # This sets up components for the GUI.
#         menu=Menu(root)
#         root.config(menu=menu)
#         subMenu=Menu(menu)
#         menu.add_cascade(label="Apps",menu=subMenu)
#         subMenu.add_command(label="Gmail")
#         subMenu.add_command(label="Y! Mail")
#         subMenu.add_command(label="Youtube")
#         subMenu.add_command(label="Facebook")
#         subMenu.add_command(label="Github")
#         subMenu.add_command(label="LinkedIn")
#         subMenu.add_separator()
#         editMenu=Menu(menu)
#         menu.add_cascade(label="Settings",menu=editMenu)
#         editMenu.add_command(label="Themes and Colors", command=getColor)
#         editMenu.add_command(label="History")
#         editMenu.add_command(label="Connect account...")
#         editMenu.add_command(label="Exit", command=root.quit)
#         editMenu=Menu(menu)
#         menu.add_cascade(label="Bookmarks",menu=editMenu)
#         editMenu.add_command(label="View")
#         editMenu.add_command(label="Add bookmark")
#         editMenu=Menu(menu)
#         menu.add_cascade(label="Tools",menu=editMenu)
#         editMenu.add_command(label="Inspect Element")
#         editMenu.add_command(label="Manage Extensions")
#         editMenu.add_command(label="Developer Tools")
#         editMenu=Menu(menu)
#         menu.add_cascade(label="Downloads",menu=editMenu)
#         editMenu.add_command(label="Open Downloads Folder", command=callback)

#         Label(root, text='Enter URL',font=("Helvetica",14)).pack(side=TOP)

#         e1 = Entry(root,width=100)
#         e1.pack(side=TOP)

#         Button(root, text='Go', width=10, relief=RAISED, font=("Helvetica",12), command=self.browse).pack(side=TOP)

#         Label(root,text='Quick Links : ',font=("Helvetica",16)).pack(side=BOTTOM)



#         # This binds the return key to self.browse as an alternative to clicking the button.
#         root.bind_all('<Enter>', self.browse)

#     @staticmethod
#     def parsed(data):
#         """Cleans up the data so the file can be easily processed by the browser."""
#         # This removes removes all python-added special characters such as b'' and '\\n' to create understandable HTML.
#         initial = str(data)[2:-1]
#         lines = initial.split('\\n')
#         return lines

#     def navigate(self, query):
#         """Gets raw data from the queried server, ready to be processed."""
#         # This gets the opener to query our request, and submit the response to be parsed.
#         response = self.opener.open(query)
#         html = response.read()
#         return html

#     def browse(self):
#         """Wraps all functionality together for data reading and writing."""
#         # This inputs and outputs the necessary website data from user-specified parameters.
#         raw_data = self.navigate(e1.get())
#         clean_data = self.parsed(raw_data)

#         # This creates a temporary file in which we store our HTML data, and open it in the default browser.
#         with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as cache:
#             cache.writelines(line.encode('UTF-8') for line in clean_data)
#             webbrowser.open_new_tab(cache.name)


# # Creates a Tk() window that is always in front of all other windows.
# root = Tk()
# # root.title("Fennec Browser")
# photo=PhotoImage(file="g.png")
# label=Label(root,image=photo)
# label.pack(side=TOP)
# url1='http://www.google.com'
# url2='http://www.bing.com'
# url3='http://www.yahoo.com'

# def OpenUrl(url):
#     webbrowser.open_new(url)

# from tkinter.colorchooser import *
# def getColor():
#     color = askcolor()

# def callback():
#     name= askopenfilename() 


# frame=Frame(root)
# frame.pack(side=BOTTOM)
# b1=ttk.Button(frame, command=lambda aurl=url1:OpenUrl(aurl))
# b1.pack(side=LEFT)
# m1=PhotoImage(file="g.png")
# b1.config(image=m1)
# tm1=m1.subsample(7,7)
# b1.config(image=tm1)
# b2=ttk.Button(frame, command=lambda aurl=url2:OpenUrl(aurl))
# b2.pack(side=LEFT)
# m2=PhotoImage(file="bing.png")
# b2.config(image=m2)
# tm2=m2.subsample(6,6)
# b2.config(image=tm2)
# b3=ttk.Button(frame, command=lambda aurl=url3:OpenUrl(aurl))
# b3.pack(side=LEFT)
# m3=PhotoImage(file="cosmo.png")
# b3.config(image=m3)
# tm3=m3.subsample(6,6)
# b3.config(image=tm3)
# b4=ttk.Button(root)
# b4.pack(side=LEFT)
# m4=PhotoImage(file="bing.png")
# b4.config(image=m4)
# tm4=m4.subsample(2,2)
# b4.config(image=tm4)
# b5=ttk.Button(root)
# b5.pack(side=RIGHT)
# m5=PhotoImage(file="bing.png")
# b5.config(image=m5)
# tm5=m5.subsample(2,2)
# b5.config(image=tm5)
# # Starts the program by initializing the Browser object and main-looping the Tk() window.
# info_from_server = Browser(root)
# root.mainloop()
""""






"""
# from tkinter import*
# from PIL import ImageTk

# if __name__=="__main__": 

#     root = Tk()
#     root.geometry("1140x800")
#     root.title("WELCOME TO BRAIN POWER SUPERMARKET")
#     root.resizable(0,0)
#     # root.iconbitmap(r'brainpower.ico')

# # frame works
#     Label(text="BRAIN POWER SUPERMARKET BILL MANAGEMENT",bg= "navyblue",fg="white", font=("a1libri",28), width="60",height="1",relief=GROOVE,border=10).pack()

#     f=Frame(root, bg="cyan", highlightbackground="navyblue",highlightthickness=2,width=400,height=550)
#     f.place(x=12,y=90) 

#     frame2= Frame(root, bg="cyan",highlightbackground="black", highlightthickness=2, width=350, height= 550)
#     frame2.place(x=740, y=90)

#     frame1=Frame(root, bd=6, height=450, width=400, relief= RAISED)
#     frame1.pack()


# # ALL FUNCTIONS
#     def Reset():
#         entry_rice.delete (0, END)
#         entry_beans.delete (0, END)
#         entry_spaghetti.delete (0, END)
#         entry_indomine.delete (0, END)
#         entry_bread.delete (0, END)
#         entry_semo.delete (0, END)
#         entry_wheat.delete (0, END)
#         entry_yam.delete (0, END)
#         entry_wine.delete (0, END)
#         entry_milk.delete (0, END)
#         entry_salt.delete (0, END)
#         entry_onions.delete (0, END)


#     def Total():
#         global totalcost, Total_bill, string_bill,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12
#         try:a1=int(rice.get())
#         except: a1=0

#         try:a2=int(beans.get())
#         except: a2=0

#         try:a3=int(spaghetti.get())
#         except: a3=0

#         try:a4=int(indomine.get())
#         except: a4=0

#         try:a5=int(bread.get())
#         except: a5=0

#         try:a6=int(semo.get())
#         except: a6=0

#         try:a7=int(wheat.get())
#         except: a7=0

#         try:a8=int(yam.get())
#         except: a8=0

#         try:a9=int(Wine.get())
#         except: a9=0

#         try:a10=int(milk.get())
#         except: a10=0

#         try:a11=int(salt.get())
#         except: a11=0

#         try:a12=int(onions.get())
#         except: a12=0


# #Creating the cost of each items per quantity
#         c1= 34000*a1
#         c2= 3200*a2
#         c3= 500*a3
#         c4= 1600*a4
#         c5= 1200*a5
#         c6= 750*a6
#         c7= 600*a7
#         c8= 1500*a8
#         c9= 1200*a9
#         c10=1250*a10
#         c11=120*a11
#         c12=50*a12



#         lbl_total = Label(frame2, font=("Times new roman", 18, "bold"), text= ("Total Purchase"), width=16, fg="black", bg="cyan")
#         lbl_total.place(x=40, y=10)

#         entry_total=Entry(frame2, font=("Times new roman", 20, "bold"), textvariable=Total_bill, bd=5, width=20, bg="light green")
#         entry_total.place(x=20, y=60)


#         reciept = Label(frame2, text="-------Receipt-------", font=("a1libre", 19, 'bold'), bg="cyan")
#         reciept.place(x=70, y=115)

#         totalcost= float(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
#         string_bill="NGN.",str("%.2f" %totalcost)
#         Total_bill.set(string_bill)

#     def reciept():
#         quantity=Label(frame2, text=f'ITEM  PRICE QTY \nRice\t{c1} =  {a1}\nBeans\t{c2} =  {a2}\nSpaghetti   {c3}  =  {a3}\nIndomine\t{c4}  =  {a4}\nBread\t{c5} =  {a5}\nSemo\t{c6}  =  {a6}\nWheat\t{c7}  =  {a7}\nYam\t{c8}  =  {a8}\nWine\t{c9}  =  {a9}\nMilk\t{c10}  =  {a10}\nSalt\t{c11}  =  {a11}\nOnions\t{c12}  =  {a12}\n',font=("Times new roman", 12, "bold"),fg="black")
#         quantity.place(x=20, y=170)
#         reciept = Label(frame2, text=    f'TOTAL :NGN{totalcost}',font=("Times new roman", 12, "bold"),fg="black")
#         reciept.place(x=20, y=450)


# #Items of the supermarket 
#     Label(f, text="ITEMS                       PRICE", font=("Gabriola", 20, "bold"), fg="black", bg="cyan").place(x=50, y=0)

#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Rice ..........NGN.34,000.00", fg="black", bg="cyan").place(x=20, y=40)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Beans........NGN.32,000.00", fg="black", bg="cyan").place(x=20, y=70)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Spaghetti .......NGN.500.00", fg="black", bg="cyan").place(x=20, y=100)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Indomine ....NGN.1,600.00", fg="black", bg="cyan").place(x=20, y=130)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Bread .........NGN.1,200.00", fg="black", bg="cyan").place(x=20, y=160)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Semo ...............NGN.750.00", fg="black", bg="cyan").place(x=20, y=190)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Wheat ............NGN.600.00", fg="black", bg="cyan").place(x=20, y=220)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Yam..............NGN.1,500.00", fg="black", bg="cyan").place(x=20, y=250)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Wine............NGN.1,200.00", fg="black", bg="cyan").place(x=20, y=280)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Milk...............NGN.1250.00", fg="black", bg="cyan").place(x=20, y=310)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Salt...............NGN.120.00", fg="black", bg="cyan").place(x=20, y=340)
#     Label(f, font=("lucida a1lligraphy", 18, "bold"), text= "Onions.............NGN.50.00", fg="black", bg="cyan").place(x=20, y=370)


# #ENTRY Work for items
#     rice=StringVar()
#     beans=StringVar()
#     spaghetti=StringVar()
#     indomine=StringVar()
#     bread=StringVar()
#     semo=StringVar()
#     wheat=StringVar()
#     yam=StringVar()
#     Wine=StringVar()
#     milk=StringVar()
#     salt=StringVar()
#     onions=StringVar()
#     Total_bill=StringVar()


# #Labels for the items 
#     lbl_rice= Label(frame1, font=("aria", 15, "bold"), text=  "Rice", width=7, fg="black")
#     lbl_beans= Label(frame1, font=("aria", 15, "bold"), text=  "Beans", width=7, fg="black")
#     lbl_spaghetti= Label(frame1, font=("aria", 15, "bold"), text="Spaghetti", width=7, fg="black")
#     lbl_indomine= Label(frame1, font=("aria", 15, "bold"), text="Indomine", width=7, fg="black")
#     lbl_bread= Label(frame1, font=("aria", 15, "bold"), text="Bread", width=7, fg="black")
#     lbl_semo= Label(frame1, font=("aria", 15, "bold"), text="Semo", width=7, fg="black")
#     lbl_wheat= Label(frame1, font=("aria", 15, "bold"), text="Wheat", width=7, fg="black")
#     lbl_yam= Label(frame1, font=("aria", 15, "bold"), text="Yam", width=7, fg="black")
#     lbl_wine= Label(frame1, font=("aria", 15, "bold"), text="Wine", width=7, fg="black")
#     lbl_milk= Label(frame1, font=("aria", 15, "bold"), text="Milk", width=7, fg="black")
#     lbl_salt= Label(frame1, font=("aria", 15, "bold"), text="Salt", width=7, fg="black")
#     lbl_onions= Label(frame1, font=("aria", 15, "bold"), text="Onions", width=7, fg="black")



#     lbl_rice.grid(row=1, column=0)
#     lbl_beans.grid(row=2, column=0)
#     lbl_spaghetti.grid(row=3, column=0)
#     lbl_indomine.grid(row=4, column=0)
#     lbl_bread.grid(row=5, column=0)
#     lbl_semo.grid(row=6, column=0)
#     lbl_wheat.grid(row=7, column=0)
#     lbl_yam.grid(row=8, column=0)
#     lbl_wine.grid(row=9, column=0)
#     lbl_milk.grid(row=10, column=0)
#     lbl_salt.grid(row=11, column=0)
#     lbl_onions.grid(row=12, column=0)



# #Entry for numbers of items
#     entry_rice=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=rice, bd=5,width=8, bg="white")
#     entry_beans=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=beans, bd=5,width=8, bg="white")
#     entry_spaghetti=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=spaghetti, bd=5,width=8, bg="white")
#     entry_indomine=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=indomine, bd=5,width=8, bg="white")
#     entry_bread=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=bread, bd=5,width=8, bg="white")
#     entry_semo=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=semo, bd=5,width=8,bg="white")
#     entry_wheat=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=wheat, bd=5,width=8,bg="white")
#     entry_yam=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=yam, bd=5,width=8,bg="white")
#     entry_wine=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=Wine, bd=5,width=8,bg="white")
#     entry_milk=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=milk, bd=5,width=8,bg="white")
#     entry_salt=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=salt, bd=5,width=8,bg="white")
#     entry_onions=Entry(frame1,font=("Times new roman", 20, "bold"), textvariable=onions, bd=5,width=8,bg="white")

#     entry_rice.grid(row=1, column=1)
#     entry_beans.grid(row=2, column=1)
#     entry_spaghetti.grid(row=3, column=1)
#     entry_indomine.grid(row=4, column=1)
#     entry_bread.grid(row=5, column=1)
#     entry_semo.grid(row=6, column=1)
#     entry_wheat.grid(row=7, column=1)
#     entry_yam.grid(row=8,column=1)
#     entry_wine.grid(row=9,column=1)
#     entry_milk.grid(row=10,column=1)
#     entry_salt.grid(row=11,column=1)
#     entry_onions.grid(row=12,column=1)


# #buttons
#     btn_resest = Button(frame1, bd=5, bg="red",fg="white", font=("Times new roman", 12, "bold"), width=12, text="Reset", command=Reset)
#     btn_resest.grid(row=14, column=0)


#     btn_total = Button(frame1, bd=5, fg="white", bg="navyblue", font=("Times new roman", 12,"bold"), width=12, text="Total", command=Total)
#     btn_total.grid(row=14, column=1)

#     btn_print_reciept = Button(frame2, bd=5, fg="white", bg="navyblue", font=("Times new roman", 12,"bold"), width=12, text="Print Reciept",command=reciept)
#     btn_print_reciept.place(x=100, y=490)

#     root.mainloop()  


class Num:
    def __init__(self,value) -> None:
        self.value = value
    
    def add(self,other):
        return self.value - other.value
    
x = Num(5)
y = Num(10)

print(x+y) 