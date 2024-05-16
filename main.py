# This Python file uses the following encoding: utf-8
import sys
import sqlite3


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from vistas.Ui_VentanaInicioSesion import Ui_VentanaInicioSesion
from vistas.Ui_VentanaControlAsistencia import Ui_VentanaControlAsistencia
from vistas.Ui_VentanaAdministrador import Ui_VentanaAdministrador
from vistas.Ui_VentanaInformacionEmpleado import Ui_VentanaInformacionEmpleado
from datetime import datetime

conexion = sqlite3.connect('JEB.db')

class VentanaInicioSesion(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaInicioSesion()
        self.ui.setupUi(self)

    def obtenerUsuario(self):
        nombre = self.ui.campoUsuario.text()
        clave_acceso = self.ui.campoContrasena.text()
        return Usuario(nombre,clave_acceso,None)

class VentanaControlAsistencia(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaControlAsistencia()
        self.ui.setupUi(self)
        self.numeroEmpleado = None
        self.nombreEmpleado = None
        self.ui.botonRegistrarLlegada.clicked.connect(self.registrarEntrada)
        self.ui.botonRegistrarSalida.clicked.connect(self.registrarSalida)

    def setEmpleado(self,numeroEmpleado,nombreEmpleado):
        self.numeroEmpleado = int(numeroEmpleado)
        self.nombreEmpleado = nombreEmpleado

    def registrarEntrada(self):
        fecha_actual = datetime.now().date()
        hora_actual = datetime.now().strftime("%H:%M")
        cursor = conexion.cursor()
        consulta = f"SELECT numeroEmpleado FROM asistencias WHERE numeroEmpleado={self.numeroEmpleado} AND fecha='{fecha_actual}'"
        print(consulta)
        cursor.execute(consulta)
        registros = cursor.fetchall()
        if len(registros)>=1:
            QMessageBox.information(self,"Error al registrar la asistencia","Ya existe un registro de entrada para el día de hoy.")
        else:
            cursor.execute(f"INSERT INTO asistencias(numeroEmpleado,nombre,fecha,horaLlegada) VALUES({self.numeroEmpleado},'{self.nombreEmpleado}','{fecha_actual}','{hora_actual}')")
            conexion.commit()
            QMessageBox.information(self,"Asistencia registrada","Se registró la hora de entrada.")
        cursor.close()

    def registrarSalida(self):
        fecha_actual = datetime.now().date()
        hora_actual = datetime.now().strftime("%H:%M")
        cursor = conexion.cursor()
        cursor.execute(f"SELECT numeroEmpleado FROM asistencias WHERE numeroEmpleado={self.numeroEmpleado} AND fecha='{fecha_actual}'")
        registros = cursor.fetchall()
        if len(registros)>=1:
            cursor.execute(f"UPDATE asistencias SET horaSalida='{hora_actual}'")
            QMessageBox.information(self,"Salida registrada","Se registró la hora de salida.")
            conexion.commit()
        else:
            QMessageBox.information(self,"Error al registrar la salida","No existe un registro de entrada para el día de hoy.")
            

class VentanaAdministrador(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaAdministrador()
        self.ui.setupUi(self)
        self.campoBusqueda = self.ui.campoBusqueda
        self.botonBusqueda = self.ui.botonBuscar
        self.tablaEmpleados = self.ui.tablaEmpleados
        self.cargarEmpleados()

        self.botonBusqueda.clicked.connect(self.buscarEmpleados)
        self.campoBusqueda.textChanged.connect(self.reiniciarBusqueda)


    def buscarEmpleados(self):
        cursor = conexion.cursor()
        nombreEmpleado = self.campoBusqueda.text()
        print("Buscando: ",nombreEmpleado)
        cursor.execute(f"SELECT * FROM empleados WHERE nombre LIKE '%{nombreEmpleado}%'")
        resultados = cursor.fetchall()
        self.tablaEmpleados.setRowCount(0)
        for e in resultados:
            fila_actual = self.tablaEmpleados.rowCount()
            self.tablaEmpleados.insertRow(fila_actual)
            self.tablaEmpleados.setItem(fila_actual,0,QTableWidgetItem(f'{e[0]}'))
            self.tablaEmpleados.setItem(fila_actual,1,QTableWidgetItem(f'{e[1]}'))
            self.tablaEmpleados.setItem(fila_actual,2,QTableWidgetItem(f'{e[2]}'))
            self.tablaEmpleados.setItem(fila_actual,3,QTableWidgetItem(f'{e[3]}'))
        cursor.close()

    def cargarEmpleados(self):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM empleados")
        resultados = cursor.fetchall()
        for e in resultados:
            fila_actual = self.tablaEmpleados.rowCount()
            self.tablaEmpleados.insertRow(fila_actual)
            self.tablaEmpleados.setItem(fila_actual,0,QTableWidgetItem(f'{e[0]}'))
            self.tablaEmpleados.setItem(fila_actual,1,QTableWidgetItem(f'{e[1]}'))
            self.tablaEmpleados.setItem(fila_actual,2,QTableWidgetItem(f'{e[2]}'))
            self.tablaEmpleados.setItem(fila_actual,3,QTableWidgetItem(f'{e[3]}'))
        cursor.close()
            
    def reiniciarBusqueda(self):
        nombreBusqueda = self.campoBusqueda.text()
        if len(nombreBusqueda) == 0:
            self.cargarEmpleados()

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
    def __init__(self,nombre,clave,admin):
        self.nombre = nombre
        self.clave = clave
        self.admin = admin

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setClave(self,clave):
        self.clave = clave

    def getClave(self):
        return self.clave
    
    def getAdmin(self):
        return self.admin
    
    def setAdmin(self,admin):
        self.admin = admin

app = QApplication(sys.argv)
ventanaInicioSesion = VentanaInicioSesion()
ventanaInformacionEmpleado = VentanaInformacionEmpleado()
ventanaControlAsistencia = VentanaControlAsistencia()
ventanaAdministrador = VentanaAdministrador()

def iniciarSesion(self):
    usuario = ventanaInicioSesion.obtenerUsuario()
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM administradores WHERE usuario = '{usuario.getNombre()}' and clave = '{usuario.getClave()}'")
    resultados  = cursor.fetchall()
    if len(resultados) == 1:
        ventanaAdministrador.show()
        ventanaInicioSesion.close()
    else:
        cursor.execute(f"SELECT nombre FROM empleados WHERE numeroEmpleado='{usuario.getNombre()}' and clave='{usuario.getClave()}'")
        resultados = cursor.fetchall()
        if len(resultados)==1:
            ventanaControlAsistencia.setEmpleado(usuario.getNombre(),resultados[0][0])
            ventanaControlAsistencia.show()
            ventanaInicioSesion.close()
    cursor.close()


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
