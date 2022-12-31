# LET'S START

## PSQL Console | Consola de PostgreSQL

Compandos más utiles de la consola

| Comando | Descripción |
| ----- | -----|
| help | Menu de ayuda |
| \\q | Salir de la consola psql |
| \\? | Ayuda para los comandos psql |
| \\h | Ayuda para los comandos SQL |
| \\h {comando} | Ver como se ejecuta un comando SQL, ejemplo: "\h ALTER" |
| \\l | Listar todas las bases de datos |
| \\dt | Ver las tablas de una base de datos |
| \\c {nombre_db} | Cambiar a otra base de datos |
| \\d {nombre_tabla} | Describir una tabla |
| \\g | Volver a ejecutar la función que acabaste de ejecutar en la consola |
| \timing | Inicializar el contador de tiempo para que la consola diga cuanto se demoró en ejecutar ese comando |
| SELECT version() | Consultar versión de postgres instalada |
| Control + c | Cancela todo lo que hay en pantalla. |
| Control + L | Limpiar pantalla. |

## Creando nuestra primera base de satos con una tabla.

Creamos nuestra primera base de datos
```sql
CREATE DATABASE transporte_masivo;
```

Luegos nos conectamos a la nueva Base de Datos creada
```sql
\c transporte_masivo
```

Creamos nuestra primera tabla llamada "viajeros".
```sql
CREATE TABLE viajeros (
  id_viajero serial PRIMARY KEY,
  nombre character varying,
  fecha_registro date
);
```

```sql
CREATE TABLE viajeros (
  id_viajero serial PRIMARY KEY NOT NULL,
  nombre character varying,
  fecha_registro date DEFAULT CURRENT_DATE
);
```