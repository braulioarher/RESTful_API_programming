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

## Usando el modulo 'fields'

Por defecto si un iterable regresado por cualquier metodo definido en una clase Resource es una estructura de datos de python y se renderiza como tal

De cualquier forma si otro objeto es regresado el renderizado no podria ser el esperado

Por esta razon Flask-RESTful contiene el modulo fields para especificar la estructura de la respuesta

La estructura de la respuesta debe ser o un diccionario o un diccionario ordenado

Algunos de los tipos de field disponicles son:

        fields.Raw              -Basado en clase field del cual fields personalizados son etregados
        fields.String           -Da una estring como salida
        fields.Float            -Da un flotante como salida
        fields.Integer          -Da un entero como salida
        fields.Boolean          -Da un booleano como salida
        fields.Url              -Da una URL en forma de string como salida
        fields.DateTime         -Regresa una string formateada en UTC

### Usando metodos 'marshal'

Flask-RESTful tambien viene con metodos como marshal, marshal_with y marshal_with_field, los cuales son utiles para filtrar la informacion de respuesta de los valores regresados de los metodos.

el metodo 'marshal' de paquete Flask-RESTful nos da la habilidad de filtrar informacion de campos especificos en el formato deseado
el metodo 'marshal' toma cualquier diccionario, lista u objeto como informacion de entrada y un diccionario o field, para que este dispnible a la salida y filtra la informacion basandose en dichos fields o campos

Un ejemplo de usar 'marshal' en la shell de flask se muestra a continuacion, esta filtra siki ek nombre del campo del diccionario data

        >>> from flask_restful import marshal
        >>> data = {'age':36, 'name':'Philiphs'}
        >>> from flask_restful import fields
        >>> required_fields = {'name':fields.Raw}
        >>> marshal(data, required_fields)
        OrderedDict([('name', 'Philiphs')])

### Usando 'marshal_with'

Adicionamente al metodo 'marshal' tambien se puede usar el decorador 'marshal_with' para clasificar el objeto regresado de un metodo con fields especificados. En el siguiente ejemplo se decora el metodo 'get' con 'marshal_with'

        >>> from flask_restful import fields, marshal_with
        >>> required_fields = { 'name': fields.Raw }
        >>> @marshal_with(required_fields)
        ... def get():
        ...     return { 'age': 36, 'name': 'Philips' }
        ...
        >>> get()
        OrderedDict([('name', 'Philips')])

### Usando 'marshal_with_field'

'marshal_with_field' es otro decoradorel cual formatea los valores regresados de los metodos con un solo campo. En el siguiente ejemplo, marshal_with_field convierte todos los valores a enteros

        >>> from flask_restful import marshal_with_field, fields
        >>> @marshal_with_field(fields.Integer)
        ... def get():
        ...     return '2', 3.0, 5
        ...
        >>> get()
        (2, 3, 5)

### Formateando un ejemplo de salida

Ahora entederemos como formatear un respuesta usando fields y marshal_with en el archivo simpleinterest_marshal.py

### Renombrando atributos

Cualquier nombre de campo que se muestra al usuario puede ser cambiado desde su campo interno al ser renombrado. Re nombrar un campo interno se puede lograe al configurar el valor del parametro 'attribute' o cualquier tipo de campo al nuevo nombre publico del campo

Un ejemplo de usar 'attribute' se muestra a continuacion, este renombra el campo 'private_name' a 'public_name'

        fields = {
        'public_name': fields.String(attribute='private_name'),
        'address': fields.String,
        'age':fields.Integer,
        }

### Campos personalizados

El modulo 'fields' tambien se puede usar para crear fields personalizados
Un field personalizado tiene que ser derivado de la clase 'fields.Raw' y debe de contener una definicion del metodo 'format'

En el siguiente ejemplo la clase 'LowerCase' se deriva de la clase 'fields.Raw' y su metodo 'format' tranforma el valor de una entrada en letras minusculas:

        class LowerCase(fields.Raw):
        def format(self, value):
                return value.lower()

## Organizando nuestra app Flask-RESTful

Una aplicacion Flask-RESTful puede ser organizada de multiples formas
En este capitulo veremos una forma de organizar un app la cual es escalable tambien con aplicaciones grandes
En general un app de projecto se divide en tres secciones: 'routes', 'resources' y 'common'
Los archivos en 'routes; contiene la aplicacion y las definiciones de varias rutas
Los archivos en la seccion'resources' contienen definiciones de varios recursos
Finalmente los archivos en la seccion 'common' contiene definiciones de funciones usadas a travez de la aplicacion

### Estructurando nuestra app

Ahora vamos a organizar los archivos hellofresco.py, frescoplaycourses.py y simpleinterest.py en la estructura que se muestra a continuacion:

        myprojectapi/
        __init__.py
        app.py
        resources/
                __init__.py 
                hellofresco.py 
                frescoplaycourses.py
                simpleinterest.py
        common/
                __init__.py
                utils.py

La reccion 'routes' contiene el archivo app.py. Y debajo se muestra el contenido de ella, la cual define la aplicacion Flask, app y la api resful 'Api'. La api esta ligaada a la aplicacion app. Mas recurso son importados desde la carpeta 'resources' y se anaden a la aplicacion

        from flask import Flask
        from flask_restful import Api
        from myprojectapi.resources.hellofresco import HelloFresco
        from myprojectapi.resources.frescoplaycourses import PlayCourses
        from myprojectapi.resources.simple_interest import SimpleInterest

        app = Flask(__name__)

        api = Api(app)
        api.add_resource(HelloFresco, '/')
        api.add_resource(PlayCourses, '/Courses/', '/Courses/<int:course_id>')
        api.add_resource(SimpleInterest, '/simpleinterest/')

### Entendiendo la seccion 'resources'

Los archivos que contienen la definicion de los recursos viven dentro de la carpeta 'myprojectapi/resources'

Se remueven las siguientes lineas de los tres archivos en resouces:

        -Lineas donde se definen la aplicacion flask ejemplo app = Flask(__name__)
        -Lineas donde se define a la api flsak restful ejemplo api = Api(app)
        -Lineas que anaden a la ai el recurso por ejemplo el metodo add_resource
        -El bloque de lineas usadas para correr la aplicacion ejemplo app.run().

Los recursor requeridos pueden ser importados en 'myprojectapi/app.py' y ser usados

Cualquier recurso puede ser anadido directamente en la carpeta 'resources'

Ahora podemos correr nuestro web server usando el comando 'flask run' despues de exportar la variable FLASK_APP

### Usando App Factory

Para usar la funcion de Flask App Factory basta definir un metodo llamado 'create_app' en el cual se define la aplicacion, se instancia la variable api, y se registan las blueprint y por ultimo se regresa la aplicacion para mas detalles de como hacer lo anterior revisar el documento 'app.py'

### Usando Blueprints

Ahora vamos a entender como asociar una Api con una Blueprint

Primeramente definimos una blueprint llamada 'playcourses_bp' u una Api llamada 'playcourses_api' dentro de nuestro archivo 'resouces/frescoplatcourses.py' como se muestra en seguida

Una vez registrata nuestra blueprint en nuestro archivo y dada de alta a nuestra api podemos registrar dicha blueprint con nuestra aplicacion  modifcando lo sigionete en el archivo app.py

### Definiendo parametros contructores

En caso de que un recurso tenga dependencias externas, dichas dependencias se pueden pasar al metod constructor de un recurso

En el siguinte ejemplo se muestra ka definicion de un Recurso ejemplo llamado 'Task'. El metodo __init__.py inicializa seld.db a un objeto de conexion basede datos y un metodo 'get' que usa el metodo 'execute' asociado al objeto de conexion

        from flask_restful import Resource

        class Task(Resource):
        def __init__(self, **kwargs):
                self.db = kwargs['dbconnection']

        def get(self):
                return self.db.execute()

La forma en pasar el objeto de conexion a base de datos a 'Task' se muestra en seguida

        db_connection = db.Connection()

        api.add_resource(TodoNext, '/next',
        resource_class_kwargs={ 'dbconnection': db_connection })

## Resumen

En este curso hemos aprendifo los siguientes temas:

        - Acerca de RESTful Web Services
        - Definir un 'Resource' usando utilidades de la extension Flask-RESTful
        - Realizar operaciones basicas CRUD en recursos al definir los metodos get, post, delete y put
        - Validar la informacion de los argumentos enviados via peticiones POST o PUT
        - Formatear las respuestas de salida de las pesticiones REST api
        - Organizar el proyecto REST API
