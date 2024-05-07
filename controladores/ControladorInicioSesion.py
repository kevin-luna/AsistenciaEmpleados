from vistas.VentanaAdministrador import VentanaAdministrador
from vistas.VentanaControlAsistencia import VentanaControlAsistencia
from controladores.ControladorVentanaAdministrador import ControladorVentanaAdministrador
from controladores.ControladorControlAsistencia import ControladorControlAsistencia

class ControladorInicioSesion:
    def __init__(self,vista):
        self.vista = vista
        self.vista.agregarEventos(self)
        self.ventanaAdministrador = VentanaAdministrador()
        self.ventanaControlAsistencia = VentanaControlAsistencia()
        self.controladorVentanaAdministrador = ControladorVentanaAdministrador(self.ventanaAdministrador)
        self.controladorControlAsistencia = ControladorControlAsistencia(self.ventanaControlAsistencia)

    def iniciarSesion(self):
        print("Hiciste click al boton")
        usuario = self.vista.obtenerUsuario()
        nombre = usuario.getNombre()
        clave = usuario.getClave()
        if nombre == 'admin' and clave == 'admin':
            print('Cargando el panel de administrador')
            self.vista.close()
            self.ventanaAdministrador.show()

        elif nombre == 'empleado' and clave == 'empleado':
            print('Cargando el panel del empleado')
            self.vista.close()
            self.ventanaControlAsistencia.show()