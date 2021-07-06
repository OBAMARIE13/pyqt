from tkinter import *

root = Tk()
root.title("Ciné Club")
root.geometry("400x400+200+200")
texte = Entry().pack()
boutton = Button(text="Ajouter un film", fg="black", bg="White" ).pack()
texte2 = Entry().pack()
boutton2 = Button(text="Supprimer le(s) film(s)", fg="black", bg="White" ).pack()
root.mainloop()