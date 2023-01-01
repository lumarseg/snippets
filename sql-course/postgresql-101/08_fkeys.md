# Forein Keys

Las llaves foráneas son una característica de la base de datos que se utilizan para establecer y mantener la integridad referencial. Esto significa que aseguran que las relaciones entre las tablas de la base de datos se mantengan de manera coherente y consistente.

Cuando se agrega una llave foránea a una tabla, se establece una relación con otra tabla. Esto significa que los valores en la columna de la llave foránea deben coincidir con los valores en la columna de la tabla relacionada que se establece como la llave primaria. De esta manera, se evita la introducción de datos inconsistentes o incorrectos en la base de datos.

Por ejemplo, si tienes una tabla de "clientes" y otra tabla de "pedidos", puedes utilizar una llave foránea para asegurarte de que cada pedido esté asociado a un cliente válido. Esto se logra estableciendo la columna "id_cliente" de la tabla "pedidos" como una llave foránea que hace referencia a la columna "id" de la tabla "clientes".

En el contexto del estándar ACID, las llaves foráneas juegan un papel importante en la parte de la integridad de la base de datos. Ayudan a garantizar que los datos se mantengan consistentes y coherentes, lo que a su vez ayuda a cumplir con las demás partes del estándar ACID (atomicidad, aislamiento y durabilidad).

## Creando las relacionas de las tablas (Forein Keys)

Repasemos el modelo relacional...

<img src="img/pic1.png" width="400">

Aplicamos las relaciones entre la tabla routes con las tablas stations y trains.

**Tabla #4: Routes**
```sql
ALTER TABLE IF EXISTS public.routes
    ADD CONSTRAINT routes_stations_fkey FOREIGN KEY (id_station)
    REFERENCES public.stations (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS public.routes
    ADD CONSTRAINT routes_trains_fkey FOREIGN KEY (id_train)
    REFERENCES public.trains (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
```

Aplicamos las relaciones entre la tabla trips con las tablas passangers y trips.

**Tabla #5: Trips**
```sql
ALTER TABLE IF EXISTS public.trips
    ADD CONSTRAINT trips_passengers_fkey FOREIGN KEY (id_passenger)
    REFERENCES public.passengers (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS public.trips
    ADD CONSTRAINT trips_routes_fkey FOREIGN KEY (id_route)
    REFERENCES public.routes (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
```

