from PySide2 import QtWidgets


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("connexion")
        self.setup_ui()



    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.nom = QtWidgets.QLineEdit()
        self.nom.setPlaceholderText("nom")
        self.email = QtWidgets.QLineEdit()
        self.email.setPlaceholderText("email")
        self.coche = QtWidgets.QCheckBox("se souvenir de moi")

        self.main_layout.addWidget(self.nom)
        self.main_layout.addWidget(self.email)
        self.main_layout.addWidget(self.coche)




app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
