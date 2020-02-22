import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("App Runner")
root.resizable(width=False,height=False)
sets = []

if os.path.isdir('sets'):
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()+"\sets"):
        sets.append(filenames)
else:
    os.mkdir("sets")



#Functions for lists clearing

def setClear():
    for widget in appSetList.winfo_children():
        widget.destroy()

def appClear():
    for widget in appsInSet.winfo_children():
        widget.destroy()

#Function for adding apps to set

def addApp():

    appClear()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"), ("all files", "*.*")))
    if filename != "":
        apps.append(filename)

    printSets()

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

appSetList = tk.Frame(root)
appSetOptions = tk.Frame(root)
appsInSet = tk.Frame(root)
appsOptions = tk.Frame(root)

appSetOptions.place(relwidth=0.4, relheight=0.3, relx=0.05, rely=0.05)
appSetList.place(relwidth=0.4, relheight=0.4, relx=0.55, rely=0.05)
appsInSet.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.5)
appsOptions.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.85)

#Labels

setsListLabel = tk.Label(appSetList,text="Saved sets:")
appsListLabel = tk.Label(appsInSet,text="Apps to start in set:")

setsListLabel.place(relwidth=1,relheight=0.1, rely=0)
appsListLabel.place(relwidth=1,relheight=0.1, rely=0)

#ListBoxes

setsList = tk.Listbox(appSetList)
appList = tk.Listbox(appsInSet)

setsList.place(relwidth=1,relheight=0.9, rely=0.1)
appList.place(relwidth=1,relheight=0.9, rely=0.1)

#Buttons

runSet = tk.Button(appSetOptions,text="Run Set",
                    padx=5, pady=2,
                    fg="white", bg="#0F0F0F",
                    height = 2, width = 30, command=runApps)
runSet.place(relx=0.15,rely=0.2)

addSet = tk.Button(appSetOptions,text="Add Set",
                     padx=5, pady=2,
                     fg="white", bg="#0F0F0F",
                     height = 2, width = 30, command=addApp)
addSet.place(relx=0.15,rely=0.5)

delSet = tk.Button(appSetOptions,text="Del Set",
                    padx=5, pady=2,
                    fg="white", bg="#0F0F0F",
                    height = 2, width = 30, command=saveSet)
delSet.place(relx=0.15,rely=0.8)

addApp = tk.Button(appsOptions,text="Add App",
                    padx=5, pady=2,
                    fg="white", bg="#0F0F0F",
                    height = 2, width = 30, command=saveSet)
addApp.place(relx=0.05)

removeApp = tk.Button(appsOptions,text="Remove App",
                    padx=5, pady=2,
                    fg="white", bg="#0F0F0F",
                    height = 2, width = 30, command=saveSet)
removeApp.place(relx=0.6)

#Function for printing list of sets

def printSets():
    for set in sets:
        label = tk.Label(setsList,text=set, bg="gray")
        label.pack()

printSets()

root.mainloop()

