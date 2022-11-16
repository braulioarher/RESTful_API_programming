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

## Parsing Requests (Analizando las peticiones)

Ya hemos visto como construir una simple API REST en flask usando la extension de Flask-RESTful, tambien se ha visto como pasar informacion a una API REST con los metodos HTTP POST y PUT.

En este tema veremos como validar la informacion enviada a travez de las peticiones HTTP usando el modulo reqparse de Flask_restful.

Las utilidades del modulo  reqparse estan formadas basandose en el modulo argparse

### Usando 'reqparse'

Para usar reqparse, una instancia de la clase RequestParser se tiene que crear primer, depsues la informacion esperada se debe annadir al analizador parser creado. Muchos parametros como 'type', 'required', 'help' se pueden configurar cuando se agrega un argumento.

El valor asociado con cualquier argumento puede ser accessado usando diccionarios, que regresa el metodo parse_args de la instancia creada

A continuacion se muestra cun ejemplo donde se crea y se anade un argumento

                from flask_restful import reqparse

                parser = reqparse.RequestParser()
                parser.add_argument('argument1', type=int, help='This argument must be an integer')
                args = parser.parse_args() # 'args' is a dictionary

Para entender mejor se define un recurso llamado SimpleInterest en el document simpleinteres.py

### Enviando una peticion POST

Ahora vamos a crear una peticion POST para esto nos dirigiimos al archivo accessing_si_app.py

### Creando RequestParser

Para verificar la informacion pasada por medio de las peticiones HTTP vamos a modificar la definicion del recurso SimpleInterest para esto se crea un nuevo archio llamado simpeinterest_with_reqparse.py donde se detalla como usar reqparse

### Conbinando errores

Por defecto RequestParser se aborta cuando encuentra el primer error de cualquier forma es posible que se convinen todos los error y se envien todos al cliente juntos.

Lo anterior lo podemos lograr configurando a 'True' el parametro 'bundle_errors'  de la clase RequestParser mientras creamos su objeto como se muestra a continuacion:

                parser = reqparse.RequestParser(bundle_errors=True)

Enronce si corremos accessing_si_app.py la respuesta seria mostar dos erroers al mismo tiempo

        400 b'{"message": {"period": "No. of Years must be an integer", "principal_amount": "Principal amount must be a number"}}\n'

### Limitando el valor de un argumento

Si un argumento necesita de tomavar solo un valor de una lista de opciones, esto lo podemos hacer con el parametro choices del metodo 'add_argument'

Un ejemplo de seria asociar cuatro opciones al argumento year como se muestra

                from flask_restful import reqparse

                parser = reqparse.RequestParser()
                parser.add_argument(
                'year',
                choices=('2017', '2018', '2019', '2020'),
                help='Bad choice'
                )

### Herencua de parser o herencia del analizador sintatico

Muchas veces vamos a definir un diferente parser para cada recurso definido
Algunos de los recursos podrian tener argumentos en comun
En tal escenario es buena practica definir un parser padre que contenga los argumentos detallados
El parser padre puede entonce ser extendido usando el metodo 'copy'
Cualquier argumento en el parser padre puede ser sobrescribido usando el metodo 'replace_argument' y puede ser completamente removido usando el metodo 'revome_argument'

En el siguiente ejemplo parser es una instacia de 'RequestParser' y una copia de el, parser_copy se crea

'parser_copy' se amplia al anadir un nuevo argumento (arg2) y configurando 'arg1' al string requerido


                from flask_restful import reqparse

                parser = reqparse.RequestParser()
                parser.add_argument('arg1', type=int)

                parser_copy = parser.copy()
                parser_copy.add_argument('arg2', type=int)

                parser_copy.replace_argument('arg1', required=True)