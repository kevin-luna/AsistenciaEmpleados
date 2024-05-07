class Empleado:
    def __init__(self,no_empleado,nombre,apellido_paterno,apellido_materno,hora_entrada,hora_salida):
        self.no_empleado = no_empleado
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
    
    def set_no_empleado(self,no_empleado):
        self.no_empleado = no_empleado

    def get_no_empleado(self):
        return self.no_empleado

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_apellido_paterno(self,apellido_paterno):
        self.apellido_paterno = apellido_paterno

    def get_apellido_paterno(self):
        return self.apellido_paterno

    def set_apellido_materno(self,apellido_materno):
        self.apelllido_materno = apellido_materno

    def get_apellido_materno(self):
        return self.apellido_materno

    def set_hora_entrada(self,hora_entrada):
        self.hora_entrada = hora_entrada

    def get_hora_entrada(self):
        return self.hora_entrada

    def set_hora_salida(self,hora_salida):
        self.hora_salida = hora_salida

    def get_hora_salida(self,hora_salida):
        return self.hora_salida
