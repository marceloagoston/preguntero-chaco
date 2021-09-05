# CONOCIENDO MI CHACO 

_El sitio contiene un ameno y divertido juego que consiste en una serie de preguntas de cultura general y sus respectivas respuestas que giran entorno a la Provincia del Chaco._

_Se dispone de un cuestionario con opciones multi choise,en dónde el jugador puede elejir niveles de dificultad, pudiendo obtener su calificación y compartir éstos resultados. El administrador por su parte podrá conocer los datos personales de los participantes, como ser nombre, apellido, dirección, email,etc; asimismo podrá disponer de la carga de preguntas y respuestas en una base de datos ._

### Pasos para crear un Proyecto: 📋

_CREAR EL PROYECTO :_ 
Con "pip3 --version" me da la versión de python que utilizo.
Con "pip list" me indica lo que tengo instalado

Crear un entorno virtual: (virtualenv)
 *	C:\User\....\entorno>python -m venv  ve_mientorno  
*	C:\User\....\entorno>ve_mientorno\scripst\activate 
	
 Instalar Django (si no está instalado) en el mismo, con el comando
	-(ve_mientorno) C:\....\entorno>pip install django-_

y luego desde la línea de comando, "cd" a un directorio donde le gustaría almacenar su proyecto cree la carpeta, darle un nombre (preguntero-chaco) y  luego ejecute el siguiente comando:_
	
	- django-admin startproject "nombre_proyecto"           

Esto creará un proyecto :"nombre_proyecto"  en su directorio actual.
y se crearán: 
			nombre_proyecto/          o ( renombrado "src") 
    			nombre_proyecto/       
				    __init__.py
				    settings.py
				    urls.py
				    asgi.py
				    wsgi.py
				  manage.py
Estos archivos son:
_ **El "nombre_proyecto"/directorio raíz externo es un contenedor para su proyecto. Su nombre no le importa a Django; puedes cambiarle el nombre a lo que quieras
*manage.py: 
Una utilidad de línea de comandos que le permite interactuar con este proyecto de Django de varias formas. 
El "nombre_proyecto/*directorio interno es el paquete de Python real para su proyecto. Su nombre es el nombre del paquete de Python que necesitará usar para importar cualquier cosa dentro de él (por ejemplo nombre_proyecto.urls).
*nombre_proyecto/__init__.py:
 Un archivo vacío que le dice a Python que este directorio debe considerarse un paquete de Python.
*nombre_proyecto/settings.py: Ajustes / configuración para este proyecto de Django. La configuración de Django le dirá todo sobre cómo funciona la configuración.
nombre_proyecto/urls.py: Las declaraciones de URL para este proyecto de Django; una "tabla de contenido" de su sitio impulsado por Django. 
*nombre_proyecto/asgi.py: Un punto de entrada para servidores web compatibles con ASGI para servir su proyecto. 
*nombre_proyecto/wsgi.py: Un punto de entrada para servidores web compatibles con WSGI para servir su proyecto.***

Se necesita además crear un archivo view.py (funciones o class en py)
y la carpeta "templates" (html). 

Son conjuntos de componentes que ayudan a desarrollar un sitio web.

_El servidor de desarrollo :_

_Verifiquemos que su proyecto Django funciona._

 Cambie al "nombre_proyecto"  directorio externo , si aún no lo ha hecho y ejecute los siguientes comandos:_
```
         python manage.py runserver
```   
Verá el siguiente resultado en la línea de comando:

_Realización de comprobaciones del sistema ..._

  La verificación del sistema no identificó problemas (0 silenciados).
  
  1 de septiembre de 2021-15: 50:53
  Django versión 3.2, usando la configuración 'nombre_proyecto.settings'
  Iniciando el servidor de desarrollo en http://127.0.0.1:8000/
  Salga del servidor con CONTROL-C._

Ha iniciado el servidor de desarrollo Django, un servidor web ligero escrito exclusivamente en Python

Ahora que el servidor está funcionando, visite http://127.0.0.1:8000/ con su navegador web. Verás un "¡Felicitaciones!" página, con un cohete despegando. ¡Funcionó!

#### Pre-requisitos al utilizar un REPOSITORIO: 📋

Para obtener una copia del proyecto del repositorio, deberás seguir la siguientes instrucciones y tener así la copia en tu máquina local, para ello en la consola ejecuta:

```
  git clone  https://github.com/marceloagoston/preguntero-chaco.git     
```

_Recordemos que con "pip3 --version" me da la versión de python que utilizo_

_Con "pip list" me indica lo que tengo instalado_

_En el caso de utilizar un Repositorio , se hace necesario:_

_Instalar las dependencias del proyecto mediante la carpeta requirements o como la llamemos (contiene archivo base.txt), la cual contiene elementos necesarios para el funcionamiento del sitio: el programa django,conector a la base de datos, libreria,etc,_

```
  (ve_mientorno) C:\....\nombre_proyecto\requirements>pip install -r base.txt 
  ```
  hago un "pip list" para ver lo que tengo instalado.
  _Salgo de la carp. "requirements"y voy a la carpeta "src o como la llame", a partir de alli creo mi carpeta "apps"donde voy a crear mis aplicaciones._

#### Creacion de apps : pasos a seguir: 📋

Las apps nos permiten crear módulos independientes con todo lo referente a un tema.

En el entorno virtual corro el servidor de prueba:
(ve_mientorno) C:\....\nombre_proyecto\src>python manage.py runserver (Para salir del servidor: Ctrl C)

_hago lo siguiente:_

(ve_mientorno) C:\....\src\apps>django-admin startapp nombre_app

con "startapp" creo la app "nombre_app"'.
															_, ,_


Otro tema importante a tener en cuenta es la configuración del archivo local.py que es propio de cada desarrollador. Ahí se deberá tener encuenta los datos propios para conectar la base de datos y el conector correspondiente.

Configuración local.py desde la importación .base *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Nombre_Base_De_Datos',
        'USER': 'Usuario_Base_De_Datos',
        'PASSWORD': 'Contraseña_Base_De_Datos',
        'HOST': 'localhost',
        'PORT': '5432' 
    }
}


## Construido con 🛠️

_ Las herramientas utilizadas para desarrollar el proyecto son las siguientes: _

* [Python](http://www.python.org) - Lenguaje de programación
									empleado
* [Django](https://www.djangoproject.com) -  El framework
											 usado
* [PostgreSQL](https://www.posgresql.org/) - Base de Datos 

* [MySQL](https://www.mysql.com/) - Base de Datos 

* [PyPI](https://www.PyPI.org.com) - Repositorio de 	                                     software oficial pa- 
																		 ra aplicaciones

* [Canva](https://www.canva.com) - Web de diseño gráfico

#### VIDEO PRESENTACION:
   
* [VIDEO](https://drive.google.com/file/d/1pZvI849151bGG3WQM6cZ7m934xRiWRBc/view?usp=drivesdkhttps://www.canva.com) 

 
## Autores ✒️ 

* **Marcelo Agoston** - *Programacion* - [marceloagoston](https://github.com/marceloagoston)
* **Cesar Martinetti** - *Documentación* - [SnkCesar](https://github.com/SnkCesar)
* **Marcos Sanchez** - *Documentación* - [MarkSanch](https://github.com/MarkSanch/Comision4_Grupo3)
* **Gladys Hardy** - *Diagram.MER y Tablas* - [GLADYSHARDY](https://github.com/GLADYSHARDY)
* ** Rodrigo Gomez** - *Documentación* - [rg301190](https://github.com/rg301190)
* ** Jonathan Cáceres** - *Diseño y programación-Video* - [rg301190](https://github.com/Jcaceres88)
