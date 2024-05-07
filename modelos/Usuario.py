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
