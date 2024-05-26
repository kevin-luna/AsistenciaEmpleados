drop table if exists empleados;
create table empleados(
   numeroEmpleado INTEGER PRIMARY KEY AUTOINCREMENT,
   nombre text,
   horaEntrada time,
   horaSalida time,
   clave text
);

drop table if exists asistencias;
create table asistencias(
    numeroEmpleado integer,
    nombre text,
    fecha date,
    horaLlegada time,
    horaSalida time,
    retardo text
);

drop table if exists administradores;
create table administradores(
   usuario text primary key,
   clave text
);

INSERT INTO administradores (usuario,clave) VALUES ('admin','admin');
INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES ('Carlos García', '08:00', '17:00', 'CG1234');
INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES ('María López', '09:00', '18:00', 'ML5678');
INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES ('Juan Fernández', '07:30', '16:30', 'JF9101');
INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES ('Ana Martínez', '08:30', '17:30', 'AM1121');
INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES ('Pedro González', '09:00', '18:00', 'PG3141');
INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES ('Laura Pérez', '08:00', '17:0', 'LP5161');
INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES ('Javier Ramírez', '07:00', '16:00', 'JR7181');
INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES ('Sofía Torres', '09:30', '18:30', 'ST9202');
INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES ('Andrés Jiménez', '08:00', '17:00', 'AJ2232');
INSERT INTO empleados (nombre, horaEntrada, horaSalida, clave) VALUES ('Lucía Ortiz', '08:30', '17:30', 'LO4252');
