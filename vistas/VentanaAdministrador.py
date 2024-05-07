from PyQt5.QtWidgets import QWidget
from vistas.Ui_VentanaAdministrador import Ui_VentanaAdministrador

class VentanaAdministrador(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaAdministrador()
        self.ui.setupUi(self)

    def buscarComponente(self,nombre):
        return self.ui.findChild(nombre)

    def agregarEventos(self,controlador):
        self.ui.botonAgregarEmpleado.clicked.connect(controlador.agregarEmpleado)
        self.ui.botonEditarEmpleado.clicked.connect(controlador.editarEmpleado)
        self.ui.botonEliminarEmpleado.clicked.connect(controlador.eliminarEmpleado)