create table empleados(
   numeroEmpleado INTEGER PRIMARY KEY AUTOINCREMENT,
   nombre TEXT,
   horaEntrada TEXT,
   horaSalida TEXT,
   clave TEXT
);


create table asistencias(
    numeroEmpleado integer,
    nombre text,
    fecha text,
    horaLlegada text,
    horaSalida text,
    retardo text
);

create table administradores(
   usuario text primary key,
   clave text
);
