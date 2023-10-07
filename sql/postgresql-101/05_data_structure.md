# Data Structure

La estructura relacional de una base de datos se refiere a cómo se organizan y relacionan los datos en una base de datos. En una base de datos relacional, los datos se organizan en tablas, que son conjuntos de filas y columnas que contienen información. Cada tabla tiene un conjunto de campos o columnas, que representan diferentes tipos de información, y cada fila de la tabla contiene un registro o un conjunto de valores para cada campo.

La estructura relacional también incluye la forma en que las tablas se relacionan entre sí. Esto se hace a través de llaves foráneas, que son campos en una tabla que se refieren a campos en otra tabla. Por ejemplo, una tabla de pedidos podría tener una llave foránea que se refiera a una tabla de clientes. Esto permite a las tablas relacionarse entre sí y permite que se realicen consultas que involucren múltiples tablas.

La estructura relacional de una base de datos es importante porque permite que los datos se almacenen de manera eficiente y se recuperen de manera rápida y sencilla. También permite que los datos se actualicen y se eliminen de manera consistente y segura.

En resumen, la estructura relacional de una base de datos se refiere a cómo se organizan y relacionan los datos en tablas y a través de llaves foráneas, y es esencial para el funcionamiento eficiente y seguro de una base de datos.

Toda jerarquía de base de datos se basa en los siguientes elementos:

1. Servidor de base de datos: Computador que tiene un motor de base de datos instalado y en ejecución.
2. Motor de base de datos: Software que provee un conjunto de servicios encargados de administrar una base de datos.
3. Base de datos: Grupo de datos que pertenecen a un mismo contexto.
4. Esquemas de base de datos en PostgreSQL: Grupo de objetos de base de datos que guarda relación entre sí (tablas, funciones, relaciones, secuencias).
5. Tablas de base de datos: Estructura que organiza los datos en filas y columnas formando una matriz.


## Practica de proyecto

La siguiente estructura relacional corresponde el proyecto para este curso.

<img src="img/pic1.png" width="400">

**Estructura del la base de datos del proyecto**

La base de datos se llamará transporte, usaremos su esquema predeterminado public.

El esquema public contendrá las siguientes tablas:

1. station: Contiene la información de las estaciones de nuestro sistema, incluye datos de nombre con tipo de dato texto y dirección con tipo de dato texto, junto con un número de identificación único por estación.
2. passenger: Es la tabla que contiene la información de las personas que viajan en nuestro sistema de transporte masivo, sus columnas son nombre tipo de dato texto con el nombre completo de la persona, direccion_residencia con tipo de dato texto que indica dónde vive la persona, fecha_nacimiento tipo de dato texto y un ID único tipo de dato numérico para identificar a cada persona.
3. train: Almacena la información de los trenes de nuestro sistema, cada tren tiene un modelo con tipo de dato texto y una capacidad con tipo de dato numérico que representa la cantidad de personas que puede llevar ese tren, también tiene un ID único por tren.

Y las tablas de relaciones entre cada uno de los elementos anteriores son:

1. route: Relaciona los trenes con las estaciones, simula ser las rutas que cada uno de los trenes pueden desarrollar entre las estaciones
2. trip: Relaciona Trayecto con Pasajero ilustrando la dinámica entre los viajes que realizan las personas, los cuales parten de una estación y se hacen usando un tren.

