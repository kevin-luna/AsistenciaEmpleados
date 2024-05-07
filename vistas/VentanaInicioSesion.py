from PyQt5.QtWidgets import QWidget
from vistas.Ui_VentanaInicioSesion import Ui_VentanaInicioSesion
from modelos.Usuario import Usuario

class VentanaInicioSesion(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaInicioSesion()
        self.ui.setupUi(self)

    def obtenerUsuario(self):
        nombre = self.ui.campoUsuario.text()
        clave_acceso = self.ui.campoContrasena.text()
        return Usuario(nombre,clave_acceso)


    def buscarComponente(self,nombre):
        return self.ui.findChild(nombre)

    def agregarEventos(self,controlador):
        self.ui.botonIniciarSesion.clicked.connect(controlador.iniciarSesion)