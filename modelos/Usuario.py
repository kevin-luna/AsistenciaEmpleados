class Usuario:
    def __init__(self,nombre,clave_acceso):
        self.nombre = nombre
        self.clave_acceso = clave_acceso

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_clave_acceso(self,clave_acceso):
        self.clave_acceso = clave_acceso

    def get_clave_acceso(self):
        return self.clave_acceso
