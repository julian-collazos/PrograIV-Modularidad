from UI.MainWindow import *

class MainWindowVivero(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.AgregarPropietarioPushButton.clicked.connect(self.aceptarPropietario)
        self.AgregarFincaPushButton.clicked.connect(self.aceptarFinca)

    def mostrar(self):
        QMessageBox.information(self,"Bienvenida","Bienvenido al programa")

    def aceptarPropietario(self):
        if not self.IDlineEdit.text() or not self.NombreLineEdit.text() or not self.ApellidoLineEdit.text()\
                or not self.TelLineEdit.text() or not self.CorreoLineEdit.text():
            QMessageBox.critical(self, "Error", "No Se han ingresado todos los datos. Por favor revise e intente nuevamente")
        else:
            QMessageBox.information(self, "Valido", "Se ha insertado correctamente la informacion")
            self.IDlineEdit.clear()
            self.NombreLineEdit.clear()
            self.ApellidoLineEdit.clear()
            self.TelLineEdit.clear()
            self.CorreoLineEdit.clear()

    def aceptarFinca(self):
        if not self.CultivoSpinBox.text() or not self.DepartamentoLineEdit.text()\
                or not self.RegistroCastralLineEdit.text():
            QMessageBox.critical(self, "Error", "No Se han ingresado todos los datos. Por favor revise e intente nuevamente")
        else:
            QMessageBox.information(self, "Valido", "Se ha insertado correctamente la informacion")
            self.CultivoSpinBox.clear()
            self.DepartamentoLineEdit.clear()
            self.RegistroCastralLineEdit.clear()
