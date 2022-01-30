import pynput
from tkinter import Label


class Keystroke:
    def onpress(self, key):
        try:
            if key.char == self.key:
                self.label.config(bg=self.pressedcolor)
        except AttributeError:
            pass

    def onrelease(self, key):
        try:
            if key.char == self.key:
                self.label.config(bg=self.bg)
        except AttributeError:
            pass

    def __init__(self, window, key, x, y, bg, pressedcolor, textcolor):
        self.window = window
        self.key = key
        self.x = x
        self.y = y
        self.bg = bg
        self.pressedcolor = pressedcolor
        self.textcolor = textcolor
        self.label = Label(self.window,
                           text=self.key.upper(),
                           bg=self.bg,
                           fg=self.textcolor,
                           font=("Comic Sans", 35),
                           width=2)
        self.label.place(x=self.x, y=self.y)
        listener = pynput.keyboard.Listener(on_press=self.onpress, on_release=self.onrelease)
        listener.start()
