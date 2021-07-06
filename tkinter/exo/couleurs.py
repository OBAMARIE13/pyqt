from tkinter import *
from tkinter.colorchooser import askcolor


root = Tk()
root.title("COULEUR")
root.geometry('500x500+200+200')

def changecouleur():
    couleurs = askcolor(title="Les couleurs")
    root.configure(bg=couleurs[5])



bouton = Button(text='choisir une couleur', fg='black', bg='white', command=changecouleur).pack()
root.mainloop()