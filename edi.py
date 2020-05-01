
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import time

window = tk.Tk(className="Editor")  #forms a window through the tkinter module

def saveas(): #basic function for saving file
    global text  
    txt = text.get("1.0", "end-1c") #return text index to index
    filename = fd.asksaveasfilename()
    doc=open(filename, "w+") #write file in a location
    doc.write(txt)
    doc.close()

filename = ""

def open_file():
    global filename
    global text
    original = text.get("1.0", "end-1c")
    filename = fd.askopenfilename(initialdir = "/home", title = "Select file")
    f = open(filename)
    txt = f.read()
    if txt == original or original == "":
        text.delete("1.0", "end")
        text.insert(chars = txt, index = "1.0")
    else:
        choice = messagebox.askyesno(title = NONE, message = "File not saved. Do you want to save it?")
        if choice == "yes":
            try:
                if filename == "":     #filename isn't valid variable to check this for initial nameless document
                    saveas()           #need a variable to hold initial nameless document's data for this logic to work
                    text.delete("1.0", "end")
                    text.insert(chars = txt, index = "1.0")       
                else:    
                    save()
                    text.delete("1.0", "end")
                    text.insert(chars = txt, index = "1.0")
                
            except:
                pass           
                    
        else:
            text.delete("1.0", "end")
            text.insert(chars = txt, index = "1.0")


def save():
    global filename
    global text  
    try:
        txt = text.get("1.0", "end-1c")
        doc=open(filename, "w+") #write file in a location
        doc.write(txt)
        doc.close()
    except:
        saveas()


def new_file():
    # global filename
    # filename = fd.askopenfile(initialdir = "/home", title = "Create a new file")
    # f = open(filename, "w+")
    pass



def about():
    details = """
This is a simple text editor made in python.
    """
    messagebox.showinfo("About", details)


def select_fonts(new_font):
    global text
    global curr_font
    curr_font = new_font
    text.config(font = new_font)


def dark_mode():
    global text
    global curr_font
    text.config(bg = "black", fg = "white", font = curr_font, insertbackground = "white")



def light_mode():
    global text
    global curr_font
    text.config(bg = "white", fg = "black", font = curr_font, insertbackground = "black")



menubar = Menu(window)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = new_file, background = "black", foreground = "white")
filemenu.add_command(label = "Open", command = open_file, background = "black", foreground = "white")
filemenu.add_command(label = "Save",command = save, background = "black", foreground = "white")
filemenu.add_command(label = "Save As", command = saveas, background = "black", foreground = "white")
filemenu.add_command(label = "Exit", command = window.quit, background = "black", foreground = "white")
menubar.add_cascade(label = "File", menu = filemenu, background = "black", foreground = "white")

edit = Menu(menubar, tearoff = 0)
fonts = Menu(edit, tearoff = 0)
interface = Menu(edit, tearoff = 0)
fonts.add_command(label = "Arial", command = lambda:select_fonts("Arial"), background = "black", foreground = "white")
fonts.add_command(label = "Times", command = lambda:select_fonts("Times"), background = "black", foreground = "white")
fonts.add_command(label = "Helvetica", command = lambda:select_fonts("Helvetica"), background = "black", foreground = "white")
interface.add_command(label = "Dark mode", command = dark_mode, background = "black", foreground = "white")
interface.add_command(label = "Light mode", command = light_mode, background = "black", foreground = "white")
edit.add_cascade(label = "Interface", menu = interface, background = "black", foreground = "white")
edit.add_cascade(label = "Fonts", menu = fonts, background = "black", foreground = "white")
menubar.add_cascade(label = "Edit", menu = edit, background = "black", foreground = "white")

help_menu = Menu(menubar, tearoff = 0)
help_menu.add_command(label = "About",command = about, background = "black", foreground = "white" )
menubar.add_cascade(label = "Help", menu = help_menu, background = "black", foreground = "white")

window.config(menu=menubar)

text= Text(window, bg = "black", fg = "white") #this line is for being able to add text in the window 
curr_font = "Verdana"
text.config(font = curr_font, insertbackground = "white")
text.pack(fill = BOTH, expand = True)


window.mainloop()
