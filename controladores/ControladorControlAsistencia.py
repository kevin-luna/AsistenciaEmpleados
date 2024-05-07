class ControladorControlAsistencia:
    def __init__(self,vista):
        self.vista = vista
        self.vista.agregarEventos(self)
        
    def salir(self):
        self.vista.close()