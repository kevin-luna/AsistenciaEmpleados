# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from vistas.Ui_VentanaInicioSesion import Ui_VentanaInicioSesion
from vistas.Ui_VentanaControlAsistencia import Ui_VentanaControlAsistencia
from vistas.Ui_VentanaAdministrador import Ui_VentanaAdministrador
from vistas.Ui_VentanaInformacionEmpleado import Ui_VentanaInformacionEmpleado

class VentanaInicioSesion(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaInicioSesion()
        self.ui.setupUi(self)

    def obtenerUsuario(self):
        nombre = self.ui.campoUsuario.text()
        clave_acceso = self.ui.campoContrasena.text()
        return Usuario(nombre,clave_acceso)

class VentanaControlAsistencia(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaControlAsistencia()
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

class Empleado:
    def __init__(self,numeroEmpleado,nombre,apellidoPaterno,apellidoMaterno,horaEntrada,horaSalida):
        self.numeroEmpleado = numeroEmpleado
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.horaEntrada = horaEntrada
        self.horaSalida = horaSalida
    
    def setNumeroEmpleado(self,numeroEmpleado):
        self.numeroEmpleado = numeroEmpleado

    def getNumeroEmpleado(self):
        return self.numeroEmpleado

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellidoPaterno(self,apellidoPaterno):
        self.apellidoPaterno = apellidoPaterno

    def getApellidoPaterno(self):
        return self.apellidoPaterno

    def setApellidoMaterno(self,apellidoMaterno):
        self.apelllido_materno = apellidoMaterno

    def getApellidoPaterno(self):
        return self.apellidoMaterno

    def setHoraEntrada(self,horaEntrada):
        self.horaEntrada = horaEntrada

    def getHoraEntrada(self):
        return self.horaEntrada

    def setHoraSalida(self,horaSalida):
        self.horaSalida = horaSalida

    def getHoraSalida(self,horaSalida):
        return self.horaSalida

class RegistroAsistencia:
    def __init__(self,numeroEmpleado,nombre,horaLlegada,horaSalida,retrasado):
        self.numeroEmpleado = numeroEmpleado
        self.nombre = nombre
        self.horaLlegada = horaLlegada
        self.horaSalida = horaSalida
        self.retrasado = retrasado

    def set_numeroEmpleado(self,numeroEmpleado):
        self.numeroEmpleado = numeroEmpleado

    def get_numeroEmpleado(self):
        return self.numeroEmpleado

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_horaLlegada(self,horaLlegada):
        self.horaLlegada = horaLlegada

    def get_horaLlegada(self):
        return self.horaLlegada

    def set_horaSalida(self,horaSalida):
        self.horaSalida = horaSalida

    def get_horaSalida(self):
        return self.horaSalida

    def set_retrasado(self,retrasado):
        self.retrasado = retrasado

    def get_retrasado(self):
        return self.retrasado

class Usuario:
    def __init__(self,nombre,clave):
        self.nombre = nombre
        self.clave = clave

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setClave(self,clave):
        self.clave = clave

    def getClave(self):
        return self.clave

app = QApplication(sys.argv)
ventanaInicioSesion = VentanaInicioSesion()
ventanaInformacionEmpleado = VentanaInformacionEmpleado()
ventanaControlAsistencia = VentanaControlAsistencia()
ventanaAdministrador = VentanaAdministrador()

def iniciarSesion(self):
        print("Hiciste click al boton")
        usuario = ventanaInicioSesion.obtenerUsuario()
        nombre = usuario.getNombre()
        clave = usuario.getClave()
        if nombre == 'admin' and clave == 'admin':
            print('Cargando el panel de administrador')
            ventanaInicioSesion.close()
            ventanaAdministrador.show()

        elif nombre == 'empleado' and clave == 'empleado':
            print('Cargando el panel del empleado')
            ventanaInicioSesion.close()
            ventanaControlAsistencia.show()

def agregarEmpleado():
    ventanaInformacionEmpleado.show()

def editarEmpleado():
    pass

def eliminarEmpleado():
    pass

def salirVentanaAsistencia():
    ventanaControlAsistencia.close()

def guardarEmpleado():
     pass

def cancelarRegistroEmpleado():
    ventanaInformacionEmpleado.close()
    
ventanaInicioSesion.ui.botonIniciarSesion.clicked.connect(iniciarSesion)
ventanaControlAsistencia.ui.botonSalir.clicked.connect(salirVentanaAsistencia)
ventanaAdministrador.ui.botonAgregarEmpleado.clicked.connect(agregarEmpleado)
ventanaInformacionEmpleado.ui.botonCancelar.clicked.connect(cancelarRegistroEmpleado)

if __name__ == "__main__":
    ventanaInicioSesion.show()
    sys.exit(app.exec())
