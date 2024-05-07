# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from vistas.VentanaInicioSesion import VentanaInicioSesion
from controladores.ControladorInicioSesion import ControladorInicioSesion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaInicioSesion()
    controladorInicioSesion = ControladorInicioSesion(ventana)
    ventana.show()
    sys.exit(app.exec())
