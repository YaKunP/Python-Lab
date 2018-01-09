from tkinter import *    # Import all definitions from tkinter(将Tkinter模块中的所有类、函数和常量的定义导入到程序中)

window = Tk()    # Create a window
lable = Label(window, text = "Welcome to Python")    # Create a label
button = Button(window, text = "Click Me")    # Create a button
lable.pack()    # Place the label in the window（使用一个包管理器将label放在容器中）
button.pack()    # Place the button in the window

window.mainloop()    # Create an event loop（事件循环）