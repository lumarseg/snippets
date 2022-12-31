# Postgresql-101a

## General

PostgreSQL es un sistema de gestión de bases de datos relacionales de código abierto. Fue diseñado para ser robusto, confiable y fácil de usar, y es utilizado ampliamente en muchas aplicaciones empresariales y de datos científicos.

Una de las principales características de PostgreSQL es su soporte extenso para SQL, lo que significa que es compatible con la mayoría de las sentencias y sintaxis del lenguaje estándar. Además, PostgreSQL proporciona una amplia gama de características avanzadas, como índices, vistas, procedimientos almacenados y disparadores, que permiten a los usuarios crear bases de datos altamente personalizadas y optimizadas para sus necesidades específicas.

Otra ventaja de PostgreSQL es su portabilidad y escalabilidad. El sistema puede ser ejecutado en una amplia gama de plataformas y puede manejar grandes cantidades de datos sin problemas. Además, PostgreSQL tiene una comunidad activa y soporte técnico disponible para ayudar a los usuarios a resolver problemas y hacer preguntas.

En general, PostgreSQL es una opción popular y de alto rendimiento para las bases de datos relacionales y es utilizado en una amplia variedad de aplicaciones y entornos empresariales.

Sobre las bases de datos existen tres conceptos:

1. El lenguaje: Es el lenguaje por el que se tiene acceso a los datos de la base de datos que está almacenado en el servidor.
2. El motor: El el que permite estructurar todos los datos dentro del servidor.
3. El Servidor: El servidor es el equipo que tiene una ram, un procesador y donde instala el motor de la base de datos.

## Características

Posgres usa como elemento principal en su nucleo, el objeto relacional en las bases de datos.

Cumple con el estandar ACID.

## ACID

ACID es un acrónimo que se refiere a las propiedades de una transacción en una base de datos. Las transacciones son una secuencia de operaciones que se realizan como una unidad, y deben cumplir con ciertas propiedades para garantizar la integridad y la consistencia de la base de datos. Las propiedades ACID se refieren a cuatro aspectos clave de una transacción:

* Atomicidad: Una transacción es atómica si es una unidad indivisible y no puede ser dividida. Esto significa que, o todas las operaciones de la transacción se realizan correctamente, o ninguna de ellas se realiza. De esta manera, se evita que la base de datos quede en un estado inconsistente.

* Consistencia: Una transacción debe dejar la base de datos en un estado consistente. Esto significa que, al final de la transacción, todas las restricciones y reglas de integridad deben cumplirse.

* Aislamiento: Las transacciones deben ser aisladas entre sí. Esto significa que, mientras una transacción está en curso, no debe ser visible para otras transacciones. De esta manera, se evita que dos transacciones conflicten entre sí y se garantiza que cada transacción se realice de manera independiente.

* Durabilidad: Una vez que una transacción ha sido completada y confirmada, sus cambios deben persistir en la base de datos. Esto significa que, incluso en caso de fallo del sistema, los cambios realizados por la transacción deben quedar guardados de manera permanente.

En resumen, las propiedades ACID garantizan que las transacciones en una base de datos sean consistentes, confiables y seguras, y ayudan a proteger la integridad de la base de datos.
