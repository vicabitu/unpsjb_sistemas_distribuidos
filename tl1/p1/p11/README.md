Para la ejecución del cliente y servidor es necesario python versión 3 o superior.

Ejecutando en la línea de comandos:
   python server11.py 
se inicializa el servidor, quedando a la espera de clientes.

Por otro lado, mediante:
	python client11.py
se crea un cliente que se conecta al servidor y envía un saludo.


-----------------------
Para ejecutar el servidor en un contenedor docker, 
mediante el comando:
        docker image build . --tag <<nombre_de_la_imagen>>
se genera una imagen con el fuente del servidor11.py.

Seguidamente, para corroborar la existencia de la imagen:
        docker image ls
mostrará en pantalla las imagenes disponibles.


Para ejecutar el servidor:
        docker run -p 8090:8080 <<nombre_de_la_imagen>>

   - en donde 8090 es el puerto del host, 
   - 8080 es el puerto definido para el servidor, 
   - y finalmente el nombre de la imagen creada previamente.
 
Konstantinoff Pedro. 18/08/2020.
