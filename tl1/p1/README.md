### Pasos para la ejecución de los fuentes

#### Requerimientos

Para la ejecución del cliente y servidor es necesario python versión 3 o superior.

#### Ejecución 

Iniciado el servidor, el mismo queda a la espera de conexiones entrantes.

```sh
python server11.py 
```

Para la creación de un cliente que se conecta al servidor anterior

```sh
python client11.py
```



#### Ejecución del servidor en un contendor docker

1. Generar la imagen del contedor para el servidor 

   ```sh
   docker image build . --tag <<nombre_de_la_imagen>>
   ```

2. Corroborar la existencia de la imagen

   ```sh
   docker image ls
   ```

3. Ejecutar el servidor contenerizado

   ```sh
   docker run -p 8080:8080 <<nombre_de_la_imagen>>
   ```
      
   > en donde 8080 es el puerto del host, 
   > 8090 es el puerto definido para el servidor, 
   > y finalmente el nombre de la imagen creada previamente.
 