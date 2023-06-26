import tkinter as tk

def box_fun():
    box = tk.LabelFrame(root, borderwidth=0)
    box_len = tk.LabelFrame(root, borderwidth=0)
    entry = tk.Entry(box,width= 22,font=("Arial",19), background="skyblue" ,foreground="white")
    ent_two =tk.Entry(box_len, width=20 ,font=("arial",19), background="red", foreground="purple" )
    
    
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