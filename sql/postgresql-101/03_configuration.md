# CONFIGURATION

PostgreSQL utiliza varios archivos de configuración para controlar la configuración del servidor. Los archivos de configuración más importantes son:

1. postgresql.conf: Este es el archivo principal de configuración de PostgreSQL y contiene la mayoría de las opciones de configuración del servidor.

2. pg_hba.conf: Este archivo controla quién tiene acceso a la base de datos y cómo pueden conectarse (Roles y ).

3. pg_ident.conf: Este archivo se utiliza para mapear nombres de usuario de autenticación externa a nombres de usuario de PostgreSQL.

4. recovery.conf: Este archivo se utiliza en las instancias de esclavo de una configuración maestro-esclavo para controlar la recuperación de la base de datos.

Los archivos de configuración se encuentran generalmente en el directorio de configuración de PostgreSQL, que por lo general es /etc/postgresql/. Algunos sistemas también tienen archivos de configuración en el directorio del usuario del usuario postgres, que suele ser ~/.pgsql/.

Es importante tener cuidado al editar estos archivos de configuración, ya que cambios incorrectos pueden afectar el funcionamiento del servidor de base de datos. Es recomendable realizar una copia de seguridad de los archivos de configuración antes de realizar cambios.

# Ubicación de los archivos

Con la siguiente consulta SQL te puestra la ubicación de los archivos:

```sql
SHOW config_file;
```

La respuesta puede ser similar a: "/etc/postgresql/14/main/postgresql.conf"

# Recargar la configuración de PostgreSQL

Desde la consola terminal (sea Linux o Windows), se puede volver a reiniciar el servicio con una nueva configuración, pero tambien mediante una consulta SQL

```sql
SELECT pg_reload_conf();
```

En Ubuntu se puede usar

```bash
sudo service postgresql restart
```

## Mapeo de Usuarios

En el archivo **pg_ident.conf**, se define el mapeo de usarios de sistema y los usarios de Postgres. La primera cadena es el nombre del Mapeo, la segunda es el nombre del usuario del sistema y la tercera es el nombre del usuario de PostgreSQL. Vea un ejemplo

```
# MAPNAME       SYSTEM-USERNAME         PG-USERNAME
mapeo-usuario   usuario                 postgres
```
