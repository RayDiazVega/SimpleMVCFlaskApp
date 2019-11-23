## SimpleMVCFlaskApp
Aplicacion web con base de datos hecha en Flask y montada en Docker.
 
Descargar el repositorio como un zip o linea comando 

Pre-requisitos 
* Docker

Instalación 
1. Descargar el repositorio y colocar los archivos dentro de una carpeta
2. Abrir la terminal en la carpeta donde estan los archivos 
3. Se crear una imagen usando docker usando el comando de docker
```
 docker build --tag=nombre_de_la_imagen .
 ```
4. Desplegamos la aplicación usando el comando
```
docker run -p 4000:80 nombre_de_la_imagen
```
5. Abrimos el navegador y en la barra de navegación colocamos http://localhost:4000

