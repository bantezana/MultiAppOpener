import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
appsCollected = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as exe:
        tempFile = exe.read()
        tempFile = tempFile.split(',')
        appsCollected = [x for x in tempFile if x.strip()]

def addApplications():
    for widget in frame.winfo_children():
        widget.destroy()

    appName = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables","*.exe"),("All Files", "*.*")))

    appsCollected.append(appName)
    print(appName)
    for mainAppOpener in appsCollected:
        label = tk.Label(frame, text=mainAppOpener, bg="grey")
        label.pack() 

def runApplicaitons():
    for mainAppOpener in appsCollected:
        os.startfile(mainAppOpener)

canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="grey", command=addApplications)
openFile.pack()

runFiles = tk.Button(root, text="Run File(s)", padx=10, pady=5, fg="white", bg="grey", command=runApplicaitons)
runFiles.pack()

for mainAppOpener in appsCollected:
    label = tk.Label(frame, text=mainAppOpener)
    label.pack()

root.mainloop()


with open('save.txt', 'w') as exe:
    for mainAppOpener in appsCollected:
        exe.write(mainAppOpener + ',')