from vistas.VentanaInformacionEmpleado import VentanaInformacionEmpleado
from controladores.ControladorInformacionEmpleado import ControladorInformacionEmpleado

class ControladorVentanaAdministrador:
    def __init__(self,vista):
        self.vista = vista
        self.vista.agregarEventos(self)
        self.ventanaInformacionEmpleado = VentanaInformacionEmpleado()
        self.controladorInformacionEmpleado = ControladorInformacionEmpleado(self.ventanaInformacionEmpleado)

    def agregarEmpleado(self):
        self.ventanaInformacionEmpleado.show()

    def editarEmpleado(self):
        pass

    def eliminarEmpleado(self):
        pass
    