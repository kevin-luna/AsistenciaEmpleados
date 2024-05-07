class ControladorInformacionEmpleado:
    def __init__(self,vista):
        self.vista = vista
        self.vista.agregarEventos(self)

    def guardarEmpleado(self):
        pass

    def cancelar(self):
        self.vista.close()