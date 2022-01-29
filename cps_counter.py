import tkinter
from tkinter import Tk, PhotoImage, Label, messagebox
from pynput import mouse
from time import sleep
from threading import Thread
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
    cpscounter = mouse.Listener(on_click=onclick)
    cpscounter.start()
    window.geometry("100x70")
    window.title("cps counter")
    window.config(bg='grey')
    text = Label(window,text="CPS",font=("Arial",20),fg='green',bg='black')
    text.pack()
    cpscount = Label(window,textvariable=cps,font=("Comic Sans",20),bg='grey')
    cpscount.pack()
    try:
        icon = PhotoImage(file='mouse.png')
        window.iconphoto(True, icon)
    except Exception:
        messagebox.showinfo(title="cps_counter",message="No icon for window\n(doesnt affect code)")
    window.mainloop()
