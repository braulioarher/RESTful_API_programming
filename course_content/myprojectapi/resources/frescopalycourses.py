from flask_restful import Resource, Api, request, abort
from flask import Blueprint


# Se define un bp yn una Api
playcourses_bp = Blueprint('PlayCoursesAPI', __name__)
playcourses_api = Api(playcourses_bp)

#Esta clase contiene los metodo disponibles
class HelloFresco(Resource):
    def get(self):
        return ({'message': 'Welcome to fresco Play!!!'}, 201, {'response_header1': 'some-message'})


# Se crea un metodo para anadir un nuevo recurso, ver un recurso
play_courses = {}

class PlayCourses(Resource):

    #El metodo Post captura el valor de la variable HTTP course_name crea un elemento en el diccionario
    def post(self, course_id):
        #Si course_id ya esta presente en play_courses la peticion se aborta
        if course_id not in play_courses:
            play_courses[course_id] = request.form['course_name']
            return {course_id: play_courses[course_id]}
        abort(404, message=f"Course_Id {course_id} already exits")
    
    #El metodo get regresa lode detalles del curso especificado si course_id es dado o regresa todos los cursos si no
    # si el course_id no se encuentra la peticion se aborta 
    def get(self, course_id=None):
        if course_id is None:
            return play_courses
        if course_id not in play_courses:
            abort(404, message = f"Course_Id {course_id} doesn't exist")
        return play_courses[course_id]

    # El metodo delete elimina la informacion en la peticion course_id
    # si no se encuentra course_id la peticion se aborta
    def delete(self, course_id):
        if course_id in play_courses:
            response_string = f'{play_courses[course_id]} course is deleted'
            del play_courses[course_id]
            return response_string
        abort(404, message=f"Course_Id {course_id} doesn't exist")

    # El metodo PUT se usa para editar contenido de un recurso existente
    # El metodo PUT altera los detalles del curso existente si no se encuentra el curso se aborta
    def put(self, course_id):
        if course_id not in play_courses:
            abort(404, message=f"Course_Id {course_id} doesn't exist")
        play_courses[course_id] = request.form['course_name']
        return {course_id: play_courses[course_id]}

#Se agrega el recurso PlayCourses a la blueprint 'playcourses_api' con la siguiente linea
playcourses_api.add_resource(PlayCourses, '/Courses/', '/Courses/<int:course_id>')