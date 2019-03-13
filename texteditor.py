import sys
v=sys.python_version
if "2.7" in v:
    from Tkinter import *
elif "3.3" in v or "3.4" in v:
    from tkinter import *
    import tkFileDialog
root=Tk("Text Editor")
text = Text(root)
text.grid()

def saveas():
    global text
    t = text.get("1.0, "end-1c")
    savelocation = tkFileDialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

button = Button(root, text="Save", command=saveas)
button.grid()

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.conf(font="Courier")

def Fontarial():
    global text
    text.conf(font="arial")

def Fonttimes():
    global text
    text.conf(font="times")

font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff = 0)

Helvetica = IntVar()
arial = IntVar()
times = IntVar()
Courier = IntVar()

font.menu.add_checkbutton(label="Courier", variable = Courier, command = FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable = Helvetica, command = FontHelvetica)
font.menu.add_checkbutton(label="arial", variable = arial, command = Fontarial)
font.menu.add_checkbutton(label="times", variable = times, command = Fonttimes)

root.mainloop()
