create table if not exists empleados(
   numeroEmpleado INTEGER PRIMARY KEY AUTOINCREMENT,
   nombre TEXT,
   apellidoPaterno TEXT,
   apellidoMaterno TEXT,
   horaEntrada TEXT,
   horaSalida TEXT
);

PRAGMA foreign_keys=ON;

create table asistencias(
    numeroEmpleado integer,
    nombre text,
    horaLlegada text,
    horaSalida text,
    foreign key(numeroEmpleado) references empleados(numeroEmpleado)
);

create table usuarios(
   nombre text primary key,
   clave text,
   admin integer
);
