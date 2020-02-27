import ntpath
import os
from tkinter import filedialog
import tkinter as tk
ntpath.basename("a/b/c")

root = tk.Tk()
root.title("App Runner")
root.resizable(width=False, height=False)
sets = []
activeSet = ""
activeSetApps = []
activeApp = ""

# - - - - - - - - - - - -FUNCTIONS - - - - - - - - - - - - - - - -

# Function for set reading


def setRead():
    if os.path.isdir('sets'):
        for file in os.listdir(os.getcwd() + "\sets"):
            if os.path.isfile(os.path.join(os.getcwd() + "\sets", file)):
                sets.append(file)
    else:
        os.mkdir("sets")

# Functions for getting name of file


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

# Function for list element selection


def selectSet(evt):
    global activeSetApps
    global activeSet
    activeSetApps.clear()
    activeSet = str(setsList.get(setsList.curselection()))
    dir = "sets/"+str(activeSet)+".txt"
    f = open(dir, "r")
    activeSetApps = f.read().split("\n")
    print("select: active:")
    print(activeSetApps)
    printApps()
    f.close()


def selectApp(evt):

    print("selected app")


# BUTTTONS

# Function for adding apps to set

def addApp():
    appClear()
    global activeSetApps
    global activeSet
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select File", filetypes=(("PNG", "*.png"), ("Executables", "*.exe"), ("JPG", "*.jpg"), ("All files", "*.*")))
    if filename != "":
        activeSetApps.append(filename)
    dir = "sets/"+str(activeSet)+".txt"
    f = open(dir, "a")
    f.write(str(filename)+"\n")
    f.close()
    print("add: active:")
    print(activeSetApps)
    printApps()

# Function for removing apps from set


def removeApp():

    appClear()
    # ...
    printSets()

# Function fot running selected app set


def runApps():
    global activeSetApps
    for app in activeSetApps:
        os.startfile(app)

# Function for removing set


def delSet():
    printSets()

# Function for adding new set


def addSet():
    print("Add Set")
    printSets()

# LISTING

# Function for printing list of sets


def printSets():
    setClear()
    for set in sets:
        setsList.insert(tk.END, set.replace('.txt', ''))

# Function for printing list of apps


def printApps():
    global activeSetApps
    appClear()
    for app in activeSetApps:
        if app != "":
            appList.insert(tk.END, path_leaf(app))

# Function for lists clearing


def setClear():
    setsList.delete(0, 'end')


def appClear():
    appList.delete(0, 'end')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - GUI - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Canvas


canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

# Frames

appSetList = tk.Frame(root)
appSetOptions = tk.Frame(root)
appsInSet = tk.Frame(root)
appsOptions = tk.Frame(root)

appSetOptions.place(relwidth=0.4, relheight=0.3, relx=0.05, rely=0.05)
appSetList.place(relwidth=0.4, relheight=0.4, relx=0.55, rely=0.05)
appsInSet.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.5)
appsOptions.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.85)

# abels

setsListLabel = tk.Label(appSetList, text="Saved sets:")
appsListLabel = tk.Label(appsInSet, text="Apps to start in set:")

setsListLabel.place(relwidth=1, relheight=0.1, rely=0)
appsListLabel.place(relwidth=1, relheight=0.1, rely=0)

# ListBoxes

setsList = tk.Listbox(appSetList)
appList = tk.Listbox(appsInSet)

setsList.bind('<<ListboxSelect>>', selectSet)
appList.bind('<<ListboxSelect>>', selectApp)

setsList.place(relwidth=1, relheight=0.9, rely=0.1)
appList.place(relwidth=1, relheight=0.9, rely=0.1)

# Buttons

runSet = tk.Button(appSetOptions, text="Run Set",
                   padx=5, pady=2,
                   fg="white", bg="#0F0F0F",
                   height=2, width=30, command=runApps)
runSet.place(relx=0.15, rely=0.2)

addSet = tk.Button(appSetOptions, text="Add Set",
                   padx=5, pady=2,
                   fg="white", bg="#0F0F0F",
                   height=2, width=30, command=addSet)
addSet.place(relx=0.15, rely=0.5)

delSet = tk.Button(appSetOptions, text="Delete Set",
                   padx=5, pady=2,
                   fg="white", bg="#0F0F0F",
                   height=2, width=30, command=delSet)
delSet.place(relx=0.15, rely=0.8)

addApp = tk.Button(appsOptions, text="Add App",
                   padx=5, pady=2,
                   fg="white", bg="#0F0F0F",
                   height=2, width=30, command=addApp)
addApp.place(relx=0.05)

removeApp = tk.Button(appsOptions, text="Remove App",
                      padx=5, pady=2,
                      fg="white", bg="#0F0F0F",
                      height=2, width=30, command=removeApp)
removeApp.place(relx=0.6)


setRead()
printSets()
printApps()

root.mainloop()
