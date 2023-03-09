from tkinter import *
from tkinter import font
from tkinter import filedialog as fd
import PIL.Image

root = Tk()
root.title('ITOA')
root.geometry('900x900')
root.config(bg='#1e1e1e')

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

    return filename

def convert_img():
    file_path = select_file()

    try:
        img = PIL.Image.open(file_path)
    except:
        print(file_path, 'File not found')

    width, height = img.size
    aspect_ratio = height/width
    new_width = 80
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))

    img = img.convert('L')

    characters = ['.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!',
                  'i', '>', '<', '~', '+', '_', '-', '?', '[', ']', '{',
                  '}', '1', '(', ')', '|', '\\', '/', 't', 'f', 'j', 'r',
                  'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C',
                  'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b',
                  'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%',
                  'B', '@', '$']
    
    pixels = img.getdata()
    new_pixels = [characters[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split the string of characters to fit the new width
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] 
                   for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    with open("ascii_image.txt", 'w+') as f:
        f.write(ascii_image)

    ls = Label(root, width=500, height=500, bg='#1e1e1e',
               fg='white', highlightthickness=0 )
    ls.place(x=-10, y=80)
    # create tkinter text area to hold ascii
    ascii_box = Text(root, width=80, height=aspect_ratio * new_width * 0.55, 
                     bg='#1e1e1e', fg='white', highlightthickness=0)
    ascii_box.place(x=150, y=80)
    ascii_box.insert(INSERT,  ascii_image)

buttonFnt = font.Font(size=18)
addFile = Button(root, text='Add Image', font=buttonFnt, command=convert_img)
addFile.place(x=365, y=10)

root.mainloop()