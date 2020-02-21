import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

#Function for adding apps to set

def addApp():

    for widget in frame_right.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame_right,text=app, bg="gray")
        label.pack()

#Function fot running selected app set

def runApps():
    for app in apps:
        os.startfile(app)

#Function for saving set

def saveSet():
    with open('save.txt','w') as f:
        for app in apps:
            f.write(app+'\n')

#Canvas

canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

#Frames

frame_right = tk.Listbox(root)
frame_left = tk.Frame(root)
frame_left.place(relwidth=0.5, relheight=1)
frame_right.place(relwidth=0.45, relheight=0.9, relx=0.5, rely=0.05)

#Buttons

openFile = tk.Button(frame_left,text="Open File",
                     padx=10, pady=5,
                     fg="white", bg="#0F0F0F",
                     height = 2, width = 30, command=addApp)
openFile.place(relx=0.15,rely=0.05)

runApps = tk.Button(frame_left,text="Run Apps",
                    padx=10, pady=5,
                    fg="white", bg="#0F0F0F",
                    height = 2, width = 30, command=runApps)
runApps.place(relx=0.15,rely=0.15)

saveSet = tk.Button(frame_left,text="Save Set",
                    padx=10, pady=5,
                    fg="white", bg="#0F0F0F",
                    height = 2, width = 30, command=saveSet)
saveSet.place(relx=0.15,rely=0.25)

root.mainloop()

