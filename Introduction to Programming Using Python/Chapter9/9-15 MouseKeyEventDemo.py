from tkinter import *    # Import all definitions from tkinter

class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()    # Create a window
        window.title("Event Demo")    # Set a title
        canvas = Canvas(window, bg = "white", width = 200, height = 100)
        canvas.pack()

        # Bind with <Button-1> event
        canvas.bind("<Button-1>", self.processMouseEvent)

        # Bind with <Key> event
        canvas.bind("<key>", self.processKeyEvent)
        canvas.focus_set()

        window.mainloop()    # Create an event loop

    def processMouseEvent(self, event):
        print("clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button is clicked? ", event.num)

    def processKeyEvent(self, event):
        print("keysym? ", event.keysym)
        print("char? ", event.char)
        print("keycode? ", event.keycode)

MouseKeyEventDemo()    # Create GUI



'''
    Note:(为什么出错，没找到原因)
    C:\Users\tipin\AppData\Local\Programs\Python\Python36\python.exe "C:/Users/tipin/PycharmProjects/Python-Lab/Introduction to Programming Using Python/Chapter9/9-15 MouseKeyEventDemo.py"
Traceback (most recent call last):
  File "C:/Users/tipin/PycharmProjects/Python-Lab/Introduction to Programming Using Python/Chapter9/9-15 MouseKeyEventDemo.py", line 29, in <module>
    MouseKeyEventDemo()    # Create GUI
  File "C:/Users/tipin/PycharmProjects/Python-Lab/Introduction to Programming Using Python/Chapter9/9-15 MouseKeyEventDemo.py", line 14, in __init__
    canvas.bind("<key>", self.processKeyEvent)
  File "C:\Users\tipin\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1245, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Users\tipin\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1200, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "key"


网上同问题：
What is the event for the Windows key in Tkinter? I'm using Linux, but I would like answers for both Linux and Windows. If Mac has a similar key, feel free to let me know the binding for it. I image there are different events for the left and right windows keys.
The windows key doesn't seem to register in my program that is supposed to catch all key presses and print what they are to the screen. I haven't seen an answer in my searches online. I've seen references to Mod4 being associated with the Windows key, but that's not a proper Tkinter event (so says my error):
_tkinter.TclError: bad event type or keysym "Mod4"
E.g. the following code gets the above error.
textWidget.bind("<Mod4>", self.myFunction)

答案：
Okay, I found the answer. It was pretty simple, and I don't know why I couldn't find it on the Internet, anywhere.
The event is called Super_L (for the left Windows key on Linux). The right Windows key is Super_R. I don't know if these events work on Windows and Mac, though.
Anyway, the reason my event key-press finder didn't find it was because I had a script running at my computer start-up that defined the compose key as being the left windows key. So, it didn't register for some reason.

'''