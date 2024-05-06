class RegistroAsistencia:
    def __init__(self,no_empleado,nombre,hora_llegada,hora_salida,retrasado):
        self.no_empleado = no_empleado
        self.nombre = nombre
        self.hora_llegada = hora_llegada
        self.hora_salida = hora_salida
        self.retrasado = retrasado

    def set_no_empleado(self,no_empleado):
        self.no_empleado = no_empleado

    def get_no_empleado(self):
        return self.no_empleado

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_hora_llegada(self,hora_llegada):
        self.hora_llegada = hora_llegada

    def get_hora_llegada(self):
        return self.hora_llegada

    def set_hora_salida(self,hora_salida):
        self.hora_salida = hora_salida

    def get_hora_salida(self):
        return self.hora_salida

    def set_retrasado(self,retrasado):
        self.retrasado = retrasado

    def get_retrasado(self):
        return self.retrasado
