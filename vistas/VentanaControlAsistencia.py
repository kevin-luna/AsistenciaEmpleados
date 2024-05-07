from PyQt5.QtWidgets import QWidget
from vistas.Ui_VentanaControlAsistencia import Ui_VentanaControlAsistencia

class VentanaControlAsistencia(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaControlAsistencia()
        self.ui.setupUi(self)

    def agregarEventos(self,controlador):
        self.ui.botonSalir.clicked.connect(controlador.salir)