from tkinter import *
from timeit import default_timer


root = Tk()



txt = StringVar()
root.title('CHRONO')
root.geometry('500x500+200+300')
mylabel = Label(text='')
box = Entry(textvariable = txt).pack()

def temp():
    actu = default_timer() - start 
    min, second = divmod(actu, 60)
    heure, minute = divmod(min, 60)
    str_time = "%d:%02d:%02d" % (heure, min, seconds)
    canvas.itemconfigure(text_clock, text=str_time)
    root.after(1000, temps)


canvas = Canvas(root, width=800, heigth=800, bg="white")
canvas.pack(padx=10, pady=10)
start = default_timer()
text_clock = canvas.create_text(40, 20)


root.mainloop()