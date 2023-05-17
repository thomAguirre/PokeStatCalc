import tkinter as tk
from tkinter import ttk

#Entry classes
main = tk.Tk() #this makes a plain window
main.title("Pokemon Stat Calculator")

#declare variables
level_var = tk.IntVar() 
base_var = tk.IntVar()
iv_var = tk.IntVar()
ev_var = tk.IntVar()

#Level
label_level = tk.Label(main, text="Enter the Pokemon's Level (0 - 100):",
                 font=('helvetica',14,'bold'))
level_entry = tk.Entry(main, 
    textvariable = level_var, 
    font=('calibre',14,'normal'))

#Base Stat
label_base = tk.Label(main, text="Enter the Pokemon's Base Stat:",
                 font=('helvetica',14,'bold'))
base_entry = tk.Entry(main,
    textvariable = base_var,
    font=('calibre',14,'normal'))  

#IV
label_iv = tk.Label(main, text="Enter the Pokemon's IV (0 - 31):",
                 font=('helvetica',14,'bold'))
iv_entry = tk.Entry(main,
    textvariable = iv_var,
    font=('calibre',14,'normal')) 

#EV
label_ev = tk.Label(main, text="Enter the Pokemon's EV (0 - 252):",
                 font=('helvetica',14,'bold'))            
ev_entry = tk.Entry(main,
    textvariable = ev_var,
    font=('calibre',14,'normal')) 


def getVars():
    #Gets the variables from the boxes
    level = int(level_var.get())
    base = int(base_var.get())
    iv = int(iv_var.get())
    ev = int(ev_var.get())
    
    #Calculate the stat
    #Casting to int after each step because pokemon math doesn't use floats
    stat = int(ev / 4)
    stat = int(2 * base + iv + stat)
    stat = int(stat * level)
    stat = int(stat / 100) + 5

    #Popup result
    popup = tk.Toplevel(main)
    popup.title("Result")
    popup_label = tk.Label(popup, text=stat, font=('calibre',14,'normal'))
    popup_label.pack()
    
    #Clear the variables
    level_var.set("")
    base_var.set("")
    iv_var.set("")
    ev_var.set("")

    
    
submit_button = tk.Button(main,
    text="Submit",
    font=('calibre',14,'normal'),
    command = getVars
)

#pack the things
label_level.pack()
level_entry.pack()

label_base.pack()
base_entry.pack()

label_iv.pack()
iv_entry.pack()

label_ev.pack()
ev_entry.pack()

submit_button.pack()
main.mainloop()
