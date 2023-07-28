import tkinter as tk

def on_enter():
    entry.delete(0,tk.END)
def on_leave():
    if entry.get() == " ":
        entry.insert(0,"ENTER A WORD:")


def on_enter(e):
    ent_two.delete(0,tk.END)
def on_leave(e):
    if ent_two.get() == " ":
        entry.insert(0,"ENTER A STRING")


def box_fun():
    global entry,ent_two
    box = tk.LabelFrame(root, borderwidth=0)
    box_len = tk.LabelFrame(root, borderwidth=0)
    
    entry = tk.Entry(box,width= 22,font=("Arial",19), background="skyblue" ,foreground="white")
    entry.insert(0,"ENTER A WORD")
    entry.bind("<FocusIn>",on_enter)
    entry.bind("FocusOut>",on_leave)
    
    ent_two =tk.Entry(box_len, width=20 ,font=("arial",19), background="red", foreground="purple" )
    ent_two.insert(0,"ENTER A STRING")
    ent_two.bind("<FocusIn>",on_enter)
    ent_two.bind("FocusOut>",on_leave)
    
    
    box.grid(row=0,column=0 , padx=40 , pady=30)
    box_len.grid(row=1, column=0 , padx=10, pady=40)
    entry.grid(row=0, column=0)
    ent_two.grid(row=1, column=1)


if __name__=="__main__":
    root = tk.Tk()
    root.title = ("GOD DID")
    root.geometry("400x400")
    root.resizable(0,0)
    # root.config(background="white")

    box_fun()
    tk.mainloop()