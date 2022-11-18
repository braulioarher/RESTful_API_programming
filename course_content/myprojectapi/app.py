from flask import Flask
from flask_restful import Api
from .resources.hellofresco import HelloFresco
from .resources.frescopalycourses import PlayCourses
from .resources.simpleinterest_marshal import SimpleInterest

from .resources.frescopalycourses import playcourses_bp


def create_app(testing_config=None):
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
    ) 

    if testing_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(testing_config)

    api = Api(app)
    api.add_resource(HelloFresco, '/')
    api.add_resource(PlayCourses, '/Courses/', '/Courses/<int:course_id>')
    api.add_resource(SimpleInterest, '/simpleinterest/')
    api.init_app(app)

    app.register_blueprint(playcourses_bp)
    
    @app.route('/home')
    def home():
        return 'Applcation working Status :' + app.config['SECRET_KEY']

    return app


# La app Flask 'app' esta asociada a 'api' dentro del metodo create_app