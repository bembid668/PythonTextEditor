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
    

root.mainloop()
