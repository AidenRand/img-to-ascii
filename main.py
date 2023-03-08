from tkinter import *
from tkinter import font
from tkinter import filedialog as fd
import PIL.Image

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

    return filename

def convert_img():
    img_flag = True
    file_path = select_file()

    try:
        img = PIL.Image.open(file_path)
        img_flag = True
    except:
        print(file_path, 'File not found')

    width, height = img.size
    aspect_ratio = height/width
    new_width = 1000
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

    with open("ascii_image.txt", 'w') as f:
        f.write(ascii_image)

buttonFnt = font.Font(size=18)
addFile = Button(root, text='Add Image', font=buttonFnt, command=convert_img)
addFile.place(x=275, y = 20)

root.mainloop()