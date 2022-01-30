import tkinter
from tkinter import Tk, PhotoImage, Label, messagebox
from pynput import mouse
from time import sleep
from threading import Thread
from keystrokes import Keystroke
x = 0
window = Tk()
cps = tkinter.StringVar()
cps.set(str(x))


class Wait:
    def __init__(self):
        global x
        global cps
        sleep(1)
        x -= 1
        cps.set(str(x))
        window.update()


def onclick(a,b,button,pressed):
    if button.left and pressed:
        global x
        global cps
        x += 1
        cps.set(str(x))
        window.update()
        t = Thread(target=Wait)
        t.start()


if __name__ == '__main__':
    window.geometry("100x70")
    window.title("")
    window.config(bg='grey')
    text = Label(window,text="CPS",font=("Arial",20),fg='green',bg='black')
    text.pack()
    cpscount = Label(window,textvariable=cps,font=("Comic Sans",20),bg='grey')
    cpscount.pack()
    try:
        icon = PhotoImage(file='mouse.png')
        window.iconphoto(True, icon)
    except tkinter.TclError:
        messagebox.showinfo(title="Cps Counter",message="No icon for window\n(doesnt affect code)")
    try:
        if messagebox.askyesno(title="Cps Counter",message="Do you want Keystrokes as well?"):
            window.geometry("200x200")
            wkey = Keystroke(window,'w', 60, 0, 'grey','white','black')
            akey = Keystroke(window,'a', 0, 59, 'grey','white','black')
            skey = Keystroke(window,'s', 60, 59, 'grey','white','black')
            dkey = Keystroke(window,'d', 120, 59, 'grey','white','black')
            window.geometry("180x118")
            text.config(font=("Arial",15))
            text.place(x=174,y=0,anchor='ne')
            cpscount.config(font=("Comic Sans",15),anchor='nw')
            cpscount.place(x=142,y=30)

    except RuntimeError:
        pass
    cpscounter = mouse.Listener(on_click=onclick)
    cpscounter.start()
    window.mainloop()
