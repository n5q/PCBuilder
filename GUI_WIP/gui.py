import tkinter as tk
from os import path
import requests

if path.exists("c:\Python\py.ico"):
    pass
else:
    url = "https://drive.google.com/uc?export=download&id=1QJN6bN3aH3vt6NDAtAWZmG4KStBep12z"
    r = requests.get(url, allow_redirects=True)
    open('c:\Python\py.ico', 'wb').write(r.content)


root= tk.Tk()
root.title("PC Builder")
root.iconbitmap(r"c:\Python\py.ico")

screen = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
screen.pack()


label1 = tk.Label(root, text='PC Builder')
label1.config(font=('helvetica', 14))
screen.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter your Budget in US Dollars:')
label2.config(font=('helvetica', 10))
screen.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
screen.create_window(200, 140, window=entry1)


    
button1 = tk.Button(text='Confirm budget', bg='brown', fg='white', font=('helvetica', 9, 'bold'))
screen.create_window(200, 180, window=button1)

processor = ""
# tk.Radiobutton(root, text = "Intel", variable = processor,value = "Intel", indicator = 0,background = "blue").pack(fill = "both", ipady = 200, ipadx = 20)



root.mainloop()
