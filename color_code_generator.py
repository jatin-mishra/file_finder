from tkinter import *
from tkinter import colorchooser

def generate_color():
    choose = colorchooser.askcolor(title="select color")
    print(f'red component : {choose[0][0]}')
    print(f'green component : {choose[0][1]}')
    print(f'black component : {choose[0][2]}')
    print(f'hex. code for the color is : {choose[1]}')


root = Tk()
root.title('color_code_generator')
btn = Button(root,text="choose color",command=generate_color)
btn.pack()
root.geometry("300x300+200+200")
root.mainloop()