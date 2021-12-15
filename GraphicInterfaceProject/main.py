import sys
import PyQt5.QtWidgets as widgets
from UI.AdmVivero import MainWindowVivero

if __name__ == '__main__':
    app = widgets.QApplication(sys.argv)
    window = MainWindowVivero()
    window.show()
    app.exec_()
