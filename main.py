from tkinter import *
from tkinter import font
from tkinter import filedialog as fd

root = Tk()
root.title('ITOA')
root.geometry('700x700')

def select_file():
    filetypes = (
        ('Image files', '*.jpg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title = 'Open a file',
        initialdir = '/',
        filetypes = filetypes
    )

    print(filename)

def print_file():
    select_file()

buttonFnt = font.Font(size=18)
addFile = Button(root, text='Add Image', font=buttonFnt, command=print_file)
addFile.place(x=275, y = 20)

root.mainloop()