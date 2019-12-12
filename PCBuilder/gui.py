import tkinter as tk
from os import path
from os.path import expanduser as rootDir
from os import name as osName
from requests import get
from datetime import datetime
from PCBuilder import buildPC

mainPath = (rootDir("~") + r"\Documents\PCBuilder")
resources = mainPath + "Resources"


if path.exists(resources + "icon.ico"):
    pass
else:
    url = "https://drive.google.com/uc?export=download&id=1QJN6bN3aH3vt6NDAtAWZmG4KStBep12z"
    r = get(url, allow_redirects=True)
    open(resources + "icon.ico", "wb").write(r.content)


root= tk.Tk()
root.title("PC Builder")

root.iconbitmap(resources + "icon.ico")
screen = tk.Canvas(root, width = 400, height = 300)
screen.pack()


label1 = tk.Label(root, text="PC Builder", font=("helvetica",14))
screen.create_window(200, 25, window=label1)

label2 = tk.Label(root, text="Enter your Budget in US Dollars:", font=("helvetica", 10))
screen.create_window(200, 100, window=label2)

budgetEntry = tk.Entry (root)
screen.create_window(200, 140, window=budgetEntry)


time = lambda format : datetime.now().strftime(format)
# print(time(("%d/%m/%Y %H:%M:%S")))

def getOutput():
    usage.destroy()
    build = (buildPC(budget,cpu.get(),use.get()))
    print(build)
    output = tk.Tk()
    output.title("Completed Build")
    output.iconbitmap(resources + "icon.ico")
    outputWindow = tk.Canvas(output, width = 600, height = 300)
    outputWindow.pack()
    outputLabel = tk.Label(output, text = build, font=("consolas",10))
    outputWindow.create_window(300,100, window=outputLabel)

def getUsage():
    global use
    global usage
    processor.destroy()
    usage = tk.Tk()
    usage.title("Select Usage")
    usage.iconbitmap(resources + "icon.ico")
    usageSelect = tk.Canvas(usage, width = 300, height = 25)
    usageSelect.pack()
    usageLabel = tk.Label(usage, text = "What is your main usage?", font=("helvetica",13))

    usageSelect.create_window(150, 15, window=usageLabel)
    use = tk.StringVar(usage)
    tk.Radiobutton(usage,command = getOutput, text = "Work", variable = use,value = "Work", indicator = 0,background = "grey33").pack(fill = "x", ipady = 20)
    tk.Radiobutton(usage,command = getOutput, text = "Gaming", variable = use,value = "Gaming", indicator = 0,background = "grey66").pack(fill = "x", ipady = 20)



def getCPU():
    global cpu
    global processor
    processor = tk.Tk()
    processor.title("Processor Selection")
    processor.iconbitmap(resources + "icon.ico")
    processorSelect = tk.Canvas(processor, width = 300, height = 25)
    processorSelect.pack()
    cpuLabel = tk.Label(processor, text = "Select your preferred processor brand", font=("helvetica",13))
    processorSelect.create_window(150, 15, window=cpuLabel)
    cpu = tk.StringVar(processor)
    tk.Radiobutton(processor, text = "Intel", variable = cpu,value = "Intel",command = getUsage, indicator = 0,background = "#0071c5").pack(fill = "x", ipady = 20)
    tk.Radiobutton(processor, text = "AMD", variable = cpu,value = "AMD",command = getUsage, indicator = 0,background = "#ca0505").pack(fill = "x", ipady = 20)


def getBudget():
    global budget
    budget = (int(budgetEntry.get()))
    getCPU()

button1 = tk.Button(text="Confirm budget", command=getBudget, bg="brown", fg="white", relief = "flat", font=("helvetica", 9, "bold"))
screen.create_window(200, 180, window=button1)






root.mainloop()


