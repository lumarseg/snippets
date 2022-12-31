# LET'S START

## PSQL Console | Consola de PostgreSQL

Comandos más utiles de la consola

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

## Practicando consultas SQL

En base al siguiente codigo, deberá indicar que objetivo se persigue.

```sql
CREATE DATABASE transporte;
```

```sql
\c transporte
```

```sql
CREATE TABLE tren ( id serial NOT NULL,
      modelo character varying,
      capacidad integer,
      CONSTRAINT tren_pkey PRIMARY KEY (id) 
      );
```

```sql
\dt
```

```sql
\d tren
```

```sql
INSERT INTO tren( modelo, capacidad ) VALUES ('Volvo 1', 100);
```

```sql
SELECT * FROM tren;
```

```sql
UPDATE tren SET modelo = 'Honda 0726' Where id = 1;
```

```sql
SELECT * FROM tren;
```

```sql
DELETE FROM tren WHERE id = 1;
```

```sql
SELECT * FROM tren;
```

```sql
\timing
```

```sql
SELECT MD5('Este mensaje está encriptado');
```

La respuesta:

Este código es un script de SQL que se ejecuta en una instancia de PostgreSQL para realizar diferentes operaciones en una base de datos y una tabla.

1. Crea una base de datos llamada "transporte".
2. Se conecta a la base de datos "transporte" utilizando el comando "\c".
3. Crea una tabla llamada "tren" con tres columnas: "id", "modelo" y "capacidad". La columna "id" es una llave primaria y tiene el tipo de datos "serial", lo que significa que se genera automáticamente un valor único para cada nueva fila.
4. Utiliza el comando "\dt" para mostrar todas las tablas en la base de datos "transporte".
5. Utiliza el comando "\d tren" para mostrar la estructura de la tabla "tren".
6. Utiliza el comando "INSERT INTO" para insertar una nueva fila en la tabla "tren" con los valores "Volvo 1" y 100 para las columnas "modelo" y "capacidad", respectivamente.
7. Utiliza el comando "SELECT" para mostrar todas las filas en la tabla "tren".
8. Utiliza el comando "UPDATE" para actualizar el valor de la columna "modelo" de la fila con "id" igual a 1 a "Honda 0726".
9. Utiliza el comando "SELECT" para mostrar todas las filas en la tabla "tren" después de la actualización.
10. Utiliza el comando "DELETE" para eliminar la fila con "id" igual a 1 de la tabla "tren".
11. Utiliza el comando "SELECT" para mostrar todas las filas en la tabla "tren" después de la eliminación.
12. Habilita el temporizador para medir el tiempo que tarda en ejecutarse la siguiente consulta.
13. Utiliza la función de hash MD5 para encriptar el mensaje "Este mensaje está encriptado".