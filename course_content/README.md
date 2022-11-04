# Restful API Programming

En la actualidad todos tratamos con sitios web y servicios web, en general interactuamos con sitios web usando un navegador web por donde se manda una peticion a travez del navegador y este muestra la respuesta.

Por otra parte los servicios web ofrecen servicios a algunas aplicaciones, Tu puedes mandar una peticion de diferentes maneras y esta maneja una respuesta la cual podria no ser leida por los humanos

En este curso tu vas a aprender a construir una aplicacion de servicio RESTful usando el framework Flask, este curso usa la extension Flask-RESTful para contruir apis REST

Se espera tener conocimientos en:

    -HTML basico y CSS
    -JavaScript
    -Flask - Pyrhon Web Framework
    -Flask Modular programing

## Que es REST

Las siglas REST significal Representational State Tranfer para formar una aplicacion REST se necesita de:

        -Separar cliente y servidor
        -REST no depende de una plataforma o lenguaje "Se puede usar cualquier lenguaje"
        -Flexibilidad y escalabilidad
        -No esta obligado a regresar solo un formato de datos puede regresar XML, JSON etc
        -Puede tomar ventajes del cache HTTP
        -Es facil de usar

## Que es una API

API significa Aplication Programing Interface que usar servidores para manejar peticiones y respuetas se usa para distribuir la naturalez de los sistemas

## Resticciones de REST

Exiten seis diferentes restricciones:

    -Cliente-Servidor: debe tener una plataforma Cliente-Servidor por separado, evoluciona idependientemente el servidor y cliente, el cliente no sabe como es la logica del servidor
    -Sin estado: No debe almacenar nada de informacion relacionada con el cliente, toda la informacion debe esta contenida dentro de la peticion, mejora la escalabilidad
    -Cache: las respuestas se debe de almacer en el cache si es posible, reduce la latencia
    -Interfase Uniforme: se debe identificar los recursos por medio de un URL, la manipulacion de los recurso se debem hacer mediante reprensetaciones por ejemplo JSON, mensajes que se describan por si solos, debe inclur links por cada respues HETEOS
    -Sitema de capas: Nos dice que el sistema se debe construir por varias capas, cada capa no sabe nada de la siguiente o anterios, tiene la desventaja de latencia pues tiene que acceder a varias capaz 
    -Codigo bajo demanda: es opcional aparte de informacion la aplicacion puede responder con codigo ejecutable lo que puede producir una reduccion en la comprension de la respuesta

## Flask-RESTful

Flask-RESTful es una extensionde Flask que nos ayuda a desarrollar REST APIs en flask, en este curso se veran ejemplos usando la extension de Flask-RESTful para contruir REST APIs. Esta extension se puede installar usando pip:

        pip install flask-restful

Construir una REST API en flask puede ser facil, los pasos son:

        -Definir un clase que se derive de la clase Resource esta es la myor parte al contruir un REST API
        -Definir uno o mas metodos considerando los metodos HTTP dentro de la clase derivada, Los petodos permitidos son get, put, post y delete
        -Mapear la clase resource con uno o mas URLs usando la funcion add_resource

Crearemos un ejemplo que define la clase HelloFresco que se deriva de la clase Resource y se mapea en la URL /

Antes de acceder a la API corremoes la aplicacion Flask y ponemos la API disponible para usarse se puede iniciar el servidor web con el comando:

        python3 hellofresco.py

Tambien se puede acceder a la REST API usando el modulo request del paquete urllib para esto creamos un script accesing_hellofresco_app.py

### Mapeando multiples URLs

Un simple Resource puede ser mapeado a una o mas URL's, multiples URLSm pueden ser pasadas al metodo add_resouce del objeto Api,

        api.add_resource(HelloFresco, '/', '/home/', '/index/')

### Configurando los headears y Response Status

Se pueden configurar los estados y los header de respuesta con los valores de return en ele ejemplo se modifica la definicion del metodo get y se establece response_header1 al valor some-message

                class HelloFresco(Resource):
                def get(self):
                return {'message': 'Welcome to Fresco Play!!!'}, 201, {'response_header1': 'some-message'}

## Creado un recurso basico CRUD

Veremos como crear un nuevo recurso para ver, editar y eliminar un recurso creado, Para entender esto crearemos un recurso PlayCourses en el erchivo frescoplaycourses.py

Se annadiran nuevos cursos al diccionario play_courses. Cada curso de Fresco play se identifica con su respectivo ID como llave
