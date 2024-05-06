# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

from vistas.Ui_VentanaInicioSesion import Ui_VentanaInicioSesion
from vistas.Ui_VentanaAdministrador import Ui_VentanaAdministrador
from vistas.Ui_VentanaInformacionEmpleado import Ui_VentanaInformacionEmpleado
from vistas.Ui_VentanaControlAsistencia import Ui_VentanaControlAsistencia

class VentanaInicioSesion(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaInicioSesion()
        self.ui.setupUi(self)

class VentanaAdministrador(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaAdministrador()
        self.ui.setupUi(self)

class VentanaInformacionEmpleado(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaInformacionEmpleado()
        self.ui.setupUi(self)

class VentanaControlAsistencia(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaControlAsistencia()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VentanaInicioSesion()
    widget.show()

    widget2 = VentanaAdministrador()
    widget2.show()

    widget3 = VentanaInformacionEmpleado()
    widget3.show()

    widget4 = VentanaControlAsistencia()
    widget4.show()
    sys.exit(app.exec())
