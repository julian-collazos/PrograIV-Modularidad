from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QMainWindow


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PropietarioGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.PropietarioGroupBox.setObjectName("PropietarioGroupBox")
        self.IDlabel = QtWidgets.QLabel(self.PropietarioGroupBox)
        self.IDlabel.setGeometry(QtCore.QRect(30, 50, 101, 16))
        self.IDlabel.setObjectName("IDlabel")
        self.NombreLabel = QtWidgets.QLabel(self.PropietarioGroupBox)
        self.NombreLabel.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.NombreLabel.setObjectName("NombreLabel")
        self.TelLabel = QtWidgets.QLabel(self.PropietarioGroupBox)
        self.TelLabel.setGeometry(QtCore.QRect(30, 150, 47, 13))
        self.TelLabel.setObjectName("TelLabel")
        self.IDlineEdit = QtWidgets.QLineEdit(self.PropietarioGroupBox)
        self.IDlineEdit.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self.IDlineEdit.setObjectName("IDlineEdit")
        self.NombreLineEdit = QtWidgets.QLineEdit(self.PropietarioGroupBox)
        self.NombreLineEdit.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.NombreLineEdit.setObjectName("NombreLineEdit")
        self.TelLineEdit = QtWidgets.QLineEdit(self.PropietarioGroupBox)
        self.TelLineEdit.setGeometry(QtCore.QRect(150, 150, 113, 20))
        self.TelLineEdit.setObjectName("TelLineEdit")
        self.ApellidoLabel = QtWidgets.QLabel(self.PropietarioGroupBox)
        self.ApellidoLabel.setGeometry(QtCore.QRect(360, 100, 47, 13))
        self.ApellidoLabel.setObjectName("ApellidoLabel")
        self.CorreoLabel = QtWidgets.QLabel(self.PropietarioGroupBox)
        self.CorreoLabel.setGeometry(QtCore.QRect(360, 150, 47, 13))
        self.CorreoLabel.setObjectName("CorreoLabel")
        self.ApellidoLineEdit = QtWidgets.QLineEdit(self.PropietarioGroupBox)
        self.ApellidoLineEdit.setGeometry(QtCore.QRect(420, 100, 113, 20))
        self.ApellidoLineEdit.setObjectName("ApellidoLineEdit")
        self.CorreoLineEdit = QtWidgets.QLineEdit(self.PropietarioGroupBox)
        self.CorreoLineEdit.setGeometry(QtCore.QRect(420, 150, 113, 20))
        self.CorreoLineEdit.setObjectName("CorreoLineEdit")
        self.AgregarPropietarioPushButton = QtWidgets.QPushButton(self.PropietarioGroupBox)
        self.AgregarPropietarioPushButton.setGeometry(QtCore.QRect(460, 230, 131, 23))
        self.AgregarPropietarioPushButton.setObjectName("AgregarPropietarioPushButton")
        self.verticalLayout.addWidget(self.PropietarioGroupBox)
        self.FincaGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.FincaGroupBox.setObjectName("FincaGroupBox")
        self.DepartamentoLineEdit = QtWidgets.QLineEdit(self.FincaGroupBox)
        self.DepartamentoLineEdit.setGeometry(QtCore.QRect(140, 150, 113, 20))
        self.DepartamentoLineEdit.setObjectName("DepartamentoLineEdit")
        self.RegistroCastralLineEdit = QtWidgets.QLineEdit(self.FincaGroupBox)
        self.RegistroCastralLineEdit.setGeometry(QtCore.QRect(420, 90, 113, 20))
        self.RegistroCastralLineEdit.setObjectName("RegistroCastralLineEdit")
        self.CultivoLabel = QtWidgets.QLabel(self.FincaGroupBox)
        self.CultivoLabel.setGeometry(QtCore.QRect(50, 80, 47, 13))
        self.CultivoLabel.setObjectName("CultivoLabel")
        self.DepartamentoLabel = QtWidgets.QLabel(self.FincaGroupBox)
        self.DepartamentoLabel.setGeometry(QtCore.QRect(50, 150, 71, 16))
        self.DepartamentoLabel.setObjectName("DepartamentoLabel")
        self.RegistroCastralLabel_8 = QtWidgets.QLabel(self.FincaGroupBox)
        self.RegistroCastralLabel_8.setGeometry(QtCore.QRect(316, 90, 81, 20))
        self.RegistroCastralLabel_8.setObjectName("RegistroCastralLabel_8")
        self.CultivoSpinBox = QtWidgets.QSpinBox(self.FincaGroupBox)
        self.CultivoSpinBox.setGeometry(QtCore.QRect(140, 80, 111, 22))
        self.CultivoSpinBox.setObjectName("CultivoSpinBox")
        self.AgregarFincaPushButton = QtWidgets.QPushButton(self.FincaGroupBox)
        self.AgregarFincaPushButton.setGeometry(QtCore.QRect(460, 210, 131, 23))
        self.AgregarFincaPushButton.setObjectName("AgregarFincaPushButton")
        self.verticalLayout.addWidget(self.FincaGroupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mostrar()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PropietarioGroupBox.setTitle(_translate("MainWindow", "Propietario"))
        self.IDlabel.setText(_translate("MainWindow", "Documento identidad"))
        self.NombreLabel.setText(_translate("MainWindow", "Nombre"))
        self.TelLabel.setText(_translate("MainWindow", "Tel/Cel"))
        self.ApellidoLabel.setText(_translate("MainWindow", "Apellido"))
        self.CorreoLabel.setText(_translate("MainWindow", "Correo"))
        self.AgregarPropietarioPushButton.setText(_translate("MainWindow", "Agregar Propietario"))
        self.FincaGroupBox.setTitle(_translate("MainWindow", "Finca"))
        self.CultivoLabel.setText(_translate("MainWindow", "Cultivo"))
        self.DepartamentoLabel.setText(_translate("MainWindow", "Departamento"))
        self.RegistroCastralLabel_8.setText(_translate("MainWindow", "Registro Castral"))
        self.AgregarFincaPushButton.setText(_translate("MainWindow", "Agregar Finca"))
