# This Python file uses the following encoding: utf-8
import sys
import sqlite3


from PyQt5.QtCore import Qt,QTime
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QColor
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
        self.botonAgregarEmpleado = self.ui.botonAgregarEmpleado
        self.botonEliminarEmpleado = self.ui.botonEliminarEmpleado
        self.tablaEmpleados = self.ui.tablaEmpleados
        self.tablaAsistencias = self.ui.tablaAsistencias
        self.botonActualizarAsistencias = self.ui.botonActualizarAsistencias
        self.botonEliminarAsistencia = self.ui.botonEliminarAsistencia
        self.ventanaInformacionEmpleado = VentanaInformacionEmpleado(self)
        self.cargarTodosLosEmpleados()
        self.cargarTodasLasAsistencias()

        self.botonBusqueda.clicked.connect(self.buscarEmpleados)
        self.campoBusqueda.textChanged.connect(self.reiniciarBusqueda)
        self.botonAgregarEmpleado.clicked.connect(self.agregarEmpleado)
        self.botonEliminarEmpleado.clicked.connect(self.eliminarEmpleado)
        self.botonActualizarAsistencias.clicked.connect(self.actualizarAsistencias)
        self.botonEliminarAsistencia.clicked.connect(self.eliminarAsistencia)



    def buscarEmpleados(self):
        nombreEmpleado = self.campoBusqueda.text()
        if nombreEmpleado != "":
            self.tablaEmpleados.setRowCount(0)
            resultados = Empleado.buscarPorNombre(nombreEmpleado)
            if resultados != None:
                self.cargarEmpleados(resultados)

    def cargarEmpleados(self,listaEmpleados):
        if listaEmpleados != None:
            self.tablaEmpleados.setRowCount(0)
            for e in listaEmpleados:
                fila_actual = self.tablaEmpleados.rowCount()
                self.tablaEmpleados.insertRow(fila_actual)
                self.tablaEmpleados.setItem(fila_actual,0,QTableWidgetItem(f'{e.getNumeroEmpleado()}'))
                self.tablaEmpleados.setItem(fila_actual,1,QTableWidgetItem(f'{e.getNombre()}'))
                self.tablaEmpleados.setItem(fila_actual,2,QTableWidgetItem(f'{e.getHoraEntrada()}'))
                self.tablaEmpleados.setItem(fila_actual,3,QTableWidgetItem(f'{e.getHoraSalida()}'))
    
    def cargarAsistencias(self,listaAsistencias):
        if listaAsistencias != None:
            self.tablaAsistencias.setRowCount(0)
            for a in listaAsistencias:
                fila_actual = self.tablaAsistencias.rowCount()
                self.tablaAsistencias.insertRow(fila_actual)
                self.tablaAsistencias.setItem(fila_actual,0,QTableWidgetItem(f'{a.getNumeroEmpleado()}'))
                self.tablaAsistencias.setItem(fila_actual,1,QTableWidgetItem(f'{a.getNombre()}'))
                self.tablaAsistencias.setItem(fila_actual,2,QTableWidgetItem(f'{a.getFecha()}'))
                self.tablaAsistencias.setItem(fila_actual,3,QTableWidgetItem(f'{a.getHoraLlegada()}'))
                self.tablaAsistencias.setItem(fila_actual,4,QTableWidgetItem(f'{a.getHoraSalida()}'))
                retrasado = a.getRetrasado()
                self.tablaAsistencias.setItem(fila_actual,5,QTableWidgetItem(f'{retrasado}'))
                if retrasado == 'Sí':
                    self.tablaAsistencias.item(fila_actual,5).setBackground(QColor(255, 0, 0))
                else:
                    self.tablaAsistencias.item(fila_actual,5).setBackground(QColor(0, 255, 0))

    def cargarTodosLosEmpleados(self):
        self.cargarEmpleados(Empleado.obtenerTodos())

    def cargarTodasLasAsistencias(self):
        self.cargarAsistencias(RegistroAsistencia.obtenerTodas())
        
    def reiniciarBusqueda(self):
        nombreBusqueda = self.campoBusqueda.text()
        if len(nombreBusqueda) == 0:
            self.cargarTodosLosEmpleados()


    def obtenerEmpleadoSeleccionado(self):
        filaSeleccionada = self.tablaEmpleados.currentRow()
        if filaSeleccionada != -1:
            return int(self.tablaEmpleados.item(filaSeleccionada,0).text())
        return -1
    
    def obtenerAsistenciaSeleccionada(self):
        filaSeleccionada = self.tablaAsistencias.currentRow()
        if filaSeleccionada != -1:
            return (int(self.tablaAsistencias.item(filaSeleccionada,0).text()),self.tablaAsistencias.item(filaSeleccionada,2).text())
        return -1
    
    def agregarEmpleado(self):
        self.ventanaInformacionEmpleado.mostrarVentana()
    
    def eliminarEmpleado(self):
        numeroEmpleado = self.obtenerEmpleadoSeleccionado()
        if numeroEmpleado != -1:
            if Empleado.eliminar(numeroEmpleado):
                QMessageBox.information(self,"Empleado eliminado","Se eliminó el empleado exitosamente.")
                self.cargarTodosLosEmpleados()
            else:
                QMessageBox.information(self,"Error al eliminar","No se ha podido eliminar el empleado.")
    
    def actualizarAsistencias(self):
        self.cargarTodasLasAsistencias()

    def eliminarAsistencia(self):
        asistencia = self.obtenerAsistenciaSeleccionada()
        if asistencia != -1:
            if RegistroAsistencia.eliminar(asistencia):
                QMessageBox.information(self,"Asistencia eliminada","Se ha eliminado el registro de asistencia con éxito.")
                self.cargarTodasLasAsistencias()
            else:
                QMessageBox.warning(self,"Error al eliminar","No se ha podido eliminar el registro de asistencia.")

class VentanaInformacionEmpleado(QWidget):
    def __init__(self,ventanaOrigen,parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaInformacionEmpleado()        
        self.ui.setupUi(self)
        self.ventanaOrigen = ventanaOrigen
        self.campoNombre = self.ui.campoNombre
        self.campoClave = self.ui.campoClave
        self.campoConfirmacionClave = self.ui.campoConfirmacionClave
        self.horaEntrada = self.ui.tiempoEntrada
        self.horaSalida = self.ui.tiempoSalida
        self.botonGuardar = self.ui.botonGuardarEmpleado
        self.botonCancelar = self.ui.botonCancelar

        self.botonGuardar.clicked.connect(self.guardarEmpleado)
        self.botonCancelar.clicked.connect(self.cerrarVentana)

    def limpiar(self):
        self.campoNombre.setText("")
        self.campoClave.setText("")
        self.campoConfirmacionClave.setText("")
        self.horaEntrada.setTime(QTime(0,0))
        self.horaSalida.setTime(QTime(0,0))

    def obtenerEmpleado(self):
        nombre = self.campoNombre.text()
        clave = self.campoClave.text()
        confirmacionClave = self.campoConfirmacionClave.text()
        entrada = self.horaEntrada.time().toString("HH:mm")
        salida = self.horaSalida.time().toString("HH:mm")
        if len(nombre)==0 or len(clave)==0:
            QMessageBox.warning(self,"Datos incompletos","No pueden quedar campos vacíos.")
            return None
        if clave != confirmacionClave:
            QMessageBox.warning(self,"Error en las claves","Las claves no coinciden.")
            return None
        return Empleado(0,nombre,entrada,salida,clave)

    def guardarEmpleado(self):
        nuevoEmpleado = self.obtenerEmpleado()
        if nuevoEmpleado != None and nuevoEmpleado.guardar():
            QMessageBox.information(self,"Empleado agregado","Se agregó el empleado exitosamente.")
            self.close()
            self.ventanaOrigen.cargarTodosLosEmpleados()

    def cargarEmpleado(self):
        pass

    def mostrarVentana(self):
        self.limpiar()
        self.show()

    def cerrarVentana(self):
        self.close()

class Empleado:
    def __init__(self,numeroEmpleado,nombre,horaEntrada,horaSalida,clave):
        self.numeroEmpleado = numeroEmpleado
        self.nombre = nombre
        self.horaEntrada = horaEntrada
        self.horaSalida = horaSalida
        self.clave = clave
    
    def setNumeroEmpleado(self,numeroEmpleado):
        self.numeroEmpleado = numeroEmpleado

    def getNumeroEmpleado(self):
        return self.numeroEmpleado

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setHoraEntrada(self,horaEntrada):
        self.horaEntrada = horaEntrada

    def getHoraEntrada(self):
        return self.horaEntrada

    def setHoraSalida(self,horaSalida):
        self.horaSalida = horaSalida

    def getHoraSalida(self):
        return self.horaSalida
    
    def setClave(self,clave):
        self.clave = clave

    def getClave(self):
        return self.clave
    
    @staticmethod
    def obtenerTodos():
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT numeroEmpleado,nombre,horaEntrada,horaSalida FROM empleados")
            resultados = cursor.fetchall()
            listaEmpleados = list()
            for empleado in resultados:
                listaEmpleados.append(Empleado(empleado[0],empleado[1],empleado[2],empleado[3],''))
            cursor.close()
            return listaEmpleados
        except sqlite3.Error as e:
            return None
        
    @staticmethod
    def buscarPorNombre(nombreEmpleado):
        try:
            cursor = conexion.cursor()
            cursor.execute(f"SELECT numeroEmpleado,nombre,horaEntrada,horaSalida FROM empleados WHERE nombre LIKE '%{nombreEmpleado}%'")
            resultados = cursor.fetchall()
            listaEmpleados = list()
            for empleado in resultados:
                listaEmpleados.append(Empleado(empleado[0],empleado[1],empleado[2],empleado[3],''))
            cursor.close()
            return listaEmpleados
        except sqlite3.Error as e:
            print(e)
            return None
    
    def guardar(self):
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES(?,?,?,?)",(self.nombre,self.horaEntrada,self.horaSalida,self.clave))
            conexion.commit()
            return True
        except sqlite3.Error as e:
            return False
        return False
    
    @staticmethod
    def eliminar(numeroEmpleado):
        if numeroEmpleado != -1:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT numeroEmpleado FROM empleados WHERE numeroEmpleado = ?",(numeroEmpleado,))
                resultados = cursor.fetchall()
                if len(resultados)>0:
                    cursor.execute("DELETE FROM empleados WHERE numeroEmpleado = ?",(numeroEmpleado,))
                    conexion.commit()
                    return True
                cursor.close()
            except sqlite3.Error as e:
                return False
        return False

class RegistroAsistencia:
    def __init__(self,numeroEmpleado,nombre,fecha,horaLlegada,horaSalida):
        self.numeroEmpleado = numeroEmpleado
        self.nombre = nombre
        self.fecha = fecha
        self.horaLlegada = horaLlegada
        self.horaSalida = horaSalida

    def setNumeroEmpleado(self,numeroEmpleado):
        self.numeroEmpleado = numeroEmpleado

    def getNumeroEmpleado(self):
        return self.numeroEmpleado

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setFecha(self,fecha):
        self.fecha = fecha

    def getFecha(self):
        return self.fecha

    def setHoraLlegada(self,horaLlegada):
        self.horaLlegada = horaLlegada

    def getHoraLlegada(self):
        return self.horaLlegada

    def setHoraSalida(self,horaSalida):
        self.horaSalida = horaSalida

    def getHoraSalida(self):
        return self.horaSalida

    def setRetrasado(self,retrasado):
        self.retrasado = retrasado

    def getRetrasado(self):
        return self.retrasado
    
    @staticmethod
    def obtenerTodas():
        try:
            cursor = conexion.cursor()
            cursor.execute("""
            SELECT 
                asistencias.*,
                CASE 
                    WHEN strftime('%H:%M', asistencias.horaLlegada) > strftime('%H:%M', empleados.horaEntrada) THEN 'Sí'
                    ELSE 'No'
                END AS retraso
            FROM 
                asistencias
            JOIN 
                empleados ON asistencias.numeroEmpleado = empleados.numeroEmpleado
            """)
            resultados = cursor.fetchall()
            print("se encontraron ",len(resultados)," asistencias")
            listaAsistencias = list()
            for a in resultados:
                listaAsistencias.append(RegistroAsistencia(a[0],a[1],a[2],a[3],a[4]))
                listaAsistencias[-1].setRetrasado(a[5])
            cursor.close()
            return listaAsistencias
        except sqlite3.Error as e:
            return None
    
    @staticmethod
    def eliminar(asistencia):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT numeroEmpleado FROM asistencias WHERE numeroEmpleado = ? AND fecha = ?",asistencia)
            resultados = cursor.fetchall()
            if len(resultados)>0:
                cursor.execute("DELETE FROM asistencias WHERE numeroEmpleado = ? AND fecha = ?",asistencia)
                conexion.commit()
                return True
        except sqlite3.Error as e:
            return False
        return False

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


def salirVentanaAsistencia():
    ventanaControlAsistencia.close()

    
ventanaInicioSesion.ui.botonIniciarSesion.clicked.connect(iniciarSesion)
ventanaControlAsistencia.ui.botonSalir.clicked.connect(salirVentanaAsistencia)

if __name__ == "__main__":
    ventanaInicioSesion.show()
    sys.exit(app.exec())
