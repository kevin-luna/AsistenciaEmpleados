# This Python file uses the following encoding: utf-8
import sys
import sqlite3
import traceback


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
        self.botonIniciarSesion = self.ui.botonIniciarSesion
        self.botonIniciarSesion.clicked.connect(self.iniciarSesion)
        self.ventanaControlAsistencia = VentanaControlAsistencia()
        self.ventanaAdministrador = VentanaAdministrador()

    def obtenerUsuario(self):
        nombre = self.ui.campoUsuario.text()
        clave_acceso = self.ui.campoContrasena.text()
        return Usuario(nombre,clave_acceso)
    
    def iniciarSesion(self):
        usuario = self.obtenerUsuario()
        respuesta = usuario.autenticar()
        if respuesta != None:
            if respuesta[0] == 'admin':
                self.ventanaAdministrador.show()
                ventanaInicioSesion.close()
            else:
                self.ventanaControlAsistencia.setEmpleado(usuario.getNombre(),respuesta[1])
                self.ventanaControlAsistencia.show()
                ventanaInicioSesion.close()

class VentanaControlAsistencia(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaControlAsistencia()
        self.ui.setupUi(self)
        self.numeroEmpleado = None
        self.nombreEmpleado = None

        self.botonRegistrarLlegada = self.ui.botonRegistrarLlegada
        self.botonRegistrarSalida = self.ui.botonRegistrarSalida
        self.botonSalir = self.ui.botonSalir

        self.botonRegistrarLlegada.clicked.connect(self.registrarLlegada)
        self.botonRegistrarSalida.clicked.connect(self.registrarSalida)
        self.ui.botonSalir.clicked.connect(self.salir)

    def salir(self):
        self.close()

    def setEmpleado(self,numeroEmpleado,nombreEmpleado):
        self.numeroEmpleado = int(numeroEmpleado)
        self.nombreEmpleado = nombreEmpleado
        self.registroAsistencia = Asistencia(self.numeroEmpleado,self.nombreEmpleado,'','','')

    def registrarLlegada(self):
        status = self.registroAsistencia.registrarLlegada()
        if status == 1:
            QMessageBox.information(self,"Error al registrar la asistencia","Ya existe un registro de entrada para el día de hoy.")
        else:
            QMessageBox.information(self,"Asistencia registrada","Se registró la hora de entrada.")

    def registrarSalida(self):
        status = self.registroAsistencia.registrarSalida()
        if status == 0:
            QMessageBox.information(self,"Salida registrada","Se registró la hora de salida.")
        elif status == 1:
            QMessageBox.information(self,"Error al registrar la salida","No existe un registro de entrada para el día de hoy.")  
        else:
            QMessageBox.information(self,"Error al registrar la salida","Ya hay un registro de salida para el día de hoy.")  

class VentanaAdministrador(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaAdministrador()
        self.ui.setupUi(self)
        self.campoBusqueda = self.ui.campoBusqueda
        self.botonBusqueda = self.ui.botonBuscar
        self.botonAgregarEmpleado = self.ui.botonAgregarEmpleado
        self.botonEditarEmpleado = self.ui.botonEditarEmpleado
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
        self.botonEditarEmpleado.clicked.connect(self.editarEmpleado)
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
        self.cargarAsistencias(Asistencia.obtenerTodas())
        
    def reiniciarBusqueda(self):
        nombreBusqueda = self.campoBusqueda.text()
        if len(nombreBusqueda) == 0:
            self.cargarTodosLosEmpleados()


    def obtenerNumeroEmpleadoSeleccionado(self):
        filaSeleccionada = self.tablaEmpleados.currentRow()
        if filaSeleccionada != -1:
            return int(self.tablaEmpleados.item(filaSeleccionada,0).text())
        return -1
    
    def obtenerEmpleadoSeleccionado(self):
        filaSeleccionada = self.tablaEmpleados.currentRow()
        if filaSeleccionada != -1:
            return Empleado(
                int(self.tablaEmpleados.item(filaSeleccionada,0).text()),
                self.tablaEmpleados.item(filaSeleccionada,1).text(),
                self.tablaEmpleados.item(filaSeleccionada,2).text(),
                self.tablaEmpleados.item(filaSeleccionada,3).text(),
                ''
            )
        return None
    
    def obtenerAsistenciaSeleccionada(self):
        filaSeleccionada = self.tablaAsistencias.currentRow()
        if filaSeleccionada != -1:
            return (int(self.tablaAsistencias.item(filaSeleccionada,0).text()),self.tablaAsistencias.item(filaSeleccionada,2).text())
        return -1
    
    def agregarEmpleado(self):
        self.ventanaInformacionEmpleado.editor = False
        self.ventanaInformacionEmpleado.mostrarVentana()
    
    def eliminarEmpleado(self):
        numeroEmpleado = self.obtenerNumeroEmpleadoSeleccionado()
        if numeroEmpleado != -1:
            if Empleado.eliminar(numeroEmpleado):
                QMessageBox.information(self,"Empleado eliminado","Se eliminó el empleado exitosamente.")
                self.cargarTodosLosEmpleados()
            else:
                QMessageBox.information(self,"Error al eliminar","No se ha podido eliminar el empleado.")
    
    def editarEmpleado(self):
        empleado = self.obtenerEmpleadoSeleccionado()
        if empleado != None:
            self.ventanaInformacionEmpleado.editor = True
            self.ventanaInformacionEmpleado.cargarEmpleado(empleado)
            self.ventanaInformacionEmpleado.show()

    def actualizarAsistencias(self):
        self.cargarTodasLasAsistencias()

    def eliminarAsistencia(self):
        asistencia = self.obtenerAsistenciaSeleccionada()
        if asistencia != -1:
            if Asistencia.eliminar(asistencia):
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
        self.numeroEmpleado = -1
        self.editor = False

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
        if len(nombre)==0 or (len(clave)==0 and self.editor==False):
            QMessageBox.warning(self,"Datos incompletos","No pueden quedar campos vacíos.")
            return None
        if clave != confirmacionClave:
            QMessageBox.warning(self,"Error en las claves","Las claves no coinciden.")
            return None
        return Empleado(self.numeroEmpleado,nombre,entrada,salida,clave)

    def guardarEmpleado(self):
        nuevoEmpleado = self.obtenerEmpleado()
        if nuevoEmpleado != None:
            if self.editor:
                if nuevoEmpleado.actualizar():
                    QMessageBox.information(self,"Empleado actualizado","Se actualizó el empleado exitosamente.")
                    self.close()
                    self.ventanaOrigen.cargarTodosLosEmpleados()
                else:
                    QMessageBox.information(self,"Error al actualizar","No se ha podido actualizar el empleado.")
            else:
                if nuevoEmpleado.guardar():
                    QMessageBox.information(self,"Empleado agregado","Se agregó el empleado exitosamente.")
                    self.close()
                    self.ventanaOrigen.cargarTodosLosEmpleados()
                else:
                    QMessageBox.information(self,"Error al agregar","No se ha podido agregar el empleado.")

    def cargarEmpleado(self,empleado):
        self.numeroEmpleado = empleado.getNumeroEmpleado()
        self.campoNombre.setText(empleado.getNombre())
        self.horaEntrada.setTime(QTime.fromString(empleado.getHoraEntrada(),"HH:mm"))
        self.horaSalida.setTime(QTime.fromString(empleado.getHoraSalida(),"HH:mm"))

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
    
    def actualizar(self):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT numeroEmpleado FROM empleados WHERE numeroEmpleado = ?",(self.numeroEmpleado,))
            resultados = cursor.fetchall()
            if len(resultados)>0:
                if self.clave != '':
                    cursor.execute("UPDATE empleados SET nombre=?,horaEntrada=?,horaSalida=?,clave=? WHERE numeroEmpleado = ?",(self.nombre,self.horaEntrada,self.horaSalida,self.clave,self.numeroEmpleado))
                else:
                    cursor.execute("UPDATE empleados SET nombre=?,horaEntrada=?,horaSalida=? WHERE numeroEmpleado = ?",(self.nombre,self.horaEntrada,self.horaSalida,self.numeroEmpleado))
                cursor.close()
                return True
        except sqlite3.Error as e:
            traceback.print_exc()
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

class Asistencia:
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
            listaAsistencias = list()
            for a in resultados:
                listaAsistencias.append(Asistencia(a[0],a[1],a[2],a[3],a[4]))
                listaAsistencias[-1].setRetrasado(a[5])
            cursor.close()
            return listaAsistencias
        except sqlite3.Error as e:
            return None
        
    def registrarLlegada(self):
        try:
            self.fecha = datetime.now().date()
            self.horaLlegada = datetime.now().strftime("%H:%M")
            cursor = conexion.cursor()
            cursor.execute("SELECT numeroEmpleado FROM asistencias WHERE numeroEmpleado=? AND fecha=?",(self.numeroEmpleado,self.fecha))
            registros = cursor.fetchall()
            if len(registros)>=1:
                cursor.close()
                return 1
            cursor.execute("INSERT INTO asistencias(numeroEmpleado,nombre,fecha,horaLlegada) VALUES(?,?,?,?)",(self.numeroEmpleado,self.nombre,self.fecha,self.horaLlegada))
            conexion.commit()
            cursor.close()
            return 0
        except sqlite3.Error as e:
            return 1
        

    def registrarSalida(self):
        try:
            self.fecha = datetime.now().date()
            cursor = conexion.cursor()
            cursor.execute(f"SELECT numeroEmpleado,horaSalida FROM asistencias WHERE numeroEmpleado=? AND fecha=?",(self.numeroEmpleado,self.fecha))
            registros = cursor.fetchall()
            self.horaSalida = registros[0][1]
            if len(registros)>=1:
                if self.horaSalida == None or self.horaSalida == '':
                    self.horaSalida = datetime.now().strftime("%H:%M")
                    cursor.execute(f"UPDATE asistencias SET horaSalida=?",(self.horaSalida,))
                    conexion.commit()
                    cursor.close()
                    return 0
                cursor.close()
                return 2
            cursor.close()
            return 1
        except sqlite3.Error as e:
            return 1
    
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
    
    def autenticar(self):
        try:
            cursor = conexion.cursor()
            cursor.execute(f"SELECT usuario FROM administradores WHERE usuario = ? and clave = ?",(self.nombre,self.clave))
            resultados  = cursor.fetchall()
            if len(resultados) == 1:
                cursor.close()
                return ('admin',resultados[0][0])
            else:
                cursor.execute(f"SELECT nombre FROM empleados WHERE numeroEmpleado=? and clave=?",(self.nombre,self.clave))
                resultados = cursor.fetchall()
                if len(resultados)==1:
                    cursor.close()
                    return ('empleado',resultados[0][0])
        except sqlite3.Error as e:
            return None 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventanaInicioSesion = VentanaInicioSesion()
    ventanaInicioSesion.show()
    sys.exit(app.exec())
