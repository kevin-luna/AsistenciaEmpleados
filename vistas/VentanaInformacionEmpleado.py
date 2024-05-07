from PyQt5.QtWidgets import QWidget
from vistas.Ui_VentanaInformacionEmpleado import Ui_VentanaInformacionEmpleado

class VentanaInformacionEmpleado(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaInformacionEmpleado()
        self.ui.setupUi(self)

    def agregarEventos(self,controlador):
        self.ui.botonGuardarEmpleado.clicked.connect(controlador.guardarEmpleado)
        self.ui.botonCancelar.clicked.connect(controlador.cancelar)