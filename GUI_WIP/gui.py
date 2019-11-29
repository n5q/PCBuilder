import tkinter as tk
from os import path
import requests


if path.exists("c:\Python\py.ico"):
    pass
else:
    url = "https://drive.google.com/uc?export=download&id=1QJN6bN3aH3vt6NDAtAWZmG4KStBep12z"
    r = requests.get(url, allow_redirects=True)
    open("c:\Python\py.ico", "wb").write(r.content)


root= tk.Tk()
root.title("PC Builder")
root.iconbitmap(r"c:\Python\py.ico")

screen = tk.Canvas(root, width = 400, height = 300,  relief = "raised")
screen.pack()


label1 = tk.Label(root, text="PC Builder")
label1.config(font=("helvetica", 14))
screen.create_window(200, 25, window=label1)

label2 = tk.Label(root, text="Enter your Budget in US Dollars:")
label2.config(font=("helvetica", 10))
screen.create_window(200, 100, window=label2)

budgetEntry = tk.Entry (root) 
screen.create_window(200, 140, window=budgetEntry)

def getBudget():
    global cpu
    budget = (budgetEntry.get())
    processor = tk.Tk()
    processor.title("Processor Selection")
    processor.iconbitmap(r"c:\Python\py.ico")
    processorSelect = tk.Canvas(processor, width = 300, height = 25,  relief = "raised")
    processorSelect.pack()
    cpuLabel = tk.Label(processor, text = "Select your preferred processor brand")
    cpuLabel.config(font=("helvetica",13))
    processorSelect.create_window(150, 15, window=cpuLabel)
    cpu = ""
    def processorInput():
        pass
    #command == 
    tk.Radiobutton(processor, text = "Intel", variable = cpu,value = "Intel", indicator = 0,background = "#0071c5").pack(fill = "x", ipady = 20)
    tk.Radiobutton(processor, text = "AMD", variable = cpu,value = "AMD", indicator = 0,background = "#ca0505").pack(fill = "x", ipady = 20)
    

button1 = tk.Button(text="Confirm budget", command=getBudget, bg="brown", fg="white", relief = "flat", font=("helvetica", 9, "bold"))
screen.create_window(200, 180, window=button1)






root.mainloop()

def test(a,b):
    return(a+b)
while True:
    print(cpu)
