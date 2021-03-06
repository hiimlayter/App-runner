import os
from tkinter import filedialog, simpledialog
import tkinter as tk
import sys

root = tk.Tk()
root.title("App Runner")
root.resizable(width=False, height=False)
sets = []
activeSet = ""
activeSetApps = []
activeApp = ""

# - - - - - - - - - - - -FUNCTIONS - - - - - - - - - - - - - - - -

def getName():
    return simpledialog.askstring("Set name", "New set name: ")


def setRead():  # Function for set reading
    if os.path.isdir('sets'):
        for file in os.listdir(os.getcwd() + "\sets"):
            if os.path.isfile(os.path.join(os.getcwd() + "\sets", file)):
                sets.append(file)
    else:
        os.mkdir("sets")

def selectSetByIndex(id):  # Functions for list element selection
    global activeSetApps
    global activeSet
    activeSetApps.clear()
    activeSet = sets[id]
    try:
        dir = "sets/"+str(activeSet)
        f = open(dir, "r")
        activeSetApps = f.read().split("\n")
        printApps()
        f.close()
    except:
        os.mkdir("sets")
        dir = "sets/"+str(activeSet)+".txt"
        f = open(dir, "r")
        activeSetApps = f.read().split("\n")
        printApps()
        f.close()


def selectSet(evt):  # Functions for list element selection
    global activeSetApps
    global activeSet
    activeSetApps.clear()
    activeSet = str(setsList.get(setsList.curselection()))
    try:
        dir = "sets/"+str(activeSet)+".txt"
        f = open(dir, "r")
        activeSetApps = f.read().split("\n")
        printApps()
        f.close()
    except:
        os.mkdir("sets")
        dir = "sets/"+str(activeSet)+".txt"
        f = open(dir, "r")
        activeSetApps = f.read().split("\n")
        printApps()
        f.close()


def appSelect(evt):
    global activeSetApps
    global activeApp
    activeApp = str(appsList.get(appsList.curselection()))
    print(activeApp)

# BUTTTONS

def addApp():  # Function for adding apps to set
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
    printApps()


def removeApp():  # Function for removing apps from set
    appClear()
    global activeSetApps
    global activeApp
    print(activeSetApps)
    activeSetApps.remove(activeApp)
    dir = "sets/"+str(activeSet)+".txt"
    f = open(dir, "r")
    lines = f.readlines()
    f.close()
    f = open(dir, "w")
    for line in lines:
        if line.strip("\n") != activeApp:
            f.write(line)
    print(activeSetApps)
    printApps()


def runApps():  # Function fot running selected app set
    global activeSetApps
    for app in activeSetApps:
        if app != "":
            os.startfile(app)


def delSet():  # Function for removing set
    global activeSet
    to_del = str(activeSet) + ".txt"
    global sets
    dir = "sets/"+to_del
    os.remove(dir)
    sets.remove(to_del)
    appClear()
    printSets()


def addSet():  # Function for adding new set
    print("Add Set")
    setName = getName()
    print(sets)
    dir = "sets/" + setName + ".txt"
    f = open(dir, "w")
    f.close()
    sets.append(setName + ".txt")
    printSets()

# LISTING

def printSets():  # Function for printing list of sets
    setClear()
    for set in sets:
        setsList.insert(tk.END, set.replace('.txt', ''))


def printApps():  # Function for printing list of apps
    global activeSetApps
    appClear()
    for app in activeSetApps:
        if app != "":
            appsList.insert(tk.END, app)


def setClear():  # Function for lists clearing
    setsList.delete(0, 'end')


def appClear():
    appsList.delete(0, 'end')

# - - - - - - - - - - - - - - GUI - - - - - - - - - - - - - - - -


# Canvas
canvas = tk.Canvas(root, height=700, width=700, background="#353535")
canvas.pack()

# Frames
appSetList = tk.Frame(root, bg="#353535")
appSetOptions = tk.Frame(root, bg="#353535")
appsInSet = tk.Frame(root, bg="#353535")
appsOptions = tk.Frame(root, bg="#353535")

appSetOptions.place(relwidth=0.4, relheight=0.3, relx=0.05, rely=0.05)
appSetList.place(relwidth=0.4, relheight=0.4, relx=0.55, rely=0.05)
appsInSet.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.5)
appsOptions.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.85)

# Labels
setsListLabel = tk.Label(appSetList, text="Saved sets:", bg="#353535", fg="#FFFFFF")
appsListLabel = tk.Label(appsInSet, text="Apps to start in set:", bg="#353535", fg="#FFFFFF")

setsListLabel.place(relwidth=1, relheight=0.1, rely=0)
appsListLabel.place(relwidth=1, relheight=0.1, rely=0)

# ListBoxes
setsList = tk.Listbox(appSetList, exportselection=False)
appsList = tk.Listbox(appsInSet, exportselection=False)

setsList.bind('<<ListboxSelect>>', selectSet)
appsList.bind('<<ListboxSelect>>', appSelect)

setsList.place(relwidth=1, relheight=0.9, rely=0.1)
appsList.place(relwidth=1, relheight=0.9, rely=0.1)

# Buttons
runSet = tk.Button(appSetOptions, text="Run Set",
                   padx=5, pady=2,
                   height=2, width=30, command=runApps)
runSet.place(relx=0.15, rely=0.2)

addSet = tk.Button(appSetOptions, text="Add Set",
                   padx=5, pady=2,
                   height=2, width=30, command=addSet)
addSet.place(relx=0.15, rely=0.5)

delSet = tk.Button(appSetOptions, text="Delete Set",
                   padx=5, pady=2,
                   height=2, width=30, command=delSet)
delSet.place(relx=0.15, rely=0.8)

addApp = tk.Button(appsOptions, text="Add App",
                   padx=5, pady=2,
                   height=2, width=30, command=addApp)
addApp.place(relx=0.05)

removeApp = tk.Button(appsOptions, text="Remove App",
                      padx=5, pady=2,
                      height=2, width=30, command=removeApp)
removeApp.place(relx=0.6)

setRead()
printSets()
printApps()

if len(sys.argv)>1 :
    id = int(sys.argv[1])
    selectSetByIndex(id-1)
    runApps()
else:
    root.mainloop()
