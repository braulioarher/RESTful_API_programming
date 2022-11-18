from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

from flask_restful import reqparse

# Se crea un parser, un Objeto de la clase RequestParser
parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument('principal_amount', type=float, help='Principal amount must be a number')
parser.add_argument('period', type=int, help='No. of years must be an integer')
parser.add_argument('rate', type=float, help='Rate must be a number')
# Mediante el argumento 'choices' se puede seleccionar solo uno de los cuatro elementos
parser.add_argument('year', choices=('2017', '2018', '2019', '2020'), help='Bad choice')

class SimpleInterest(Resource):

    def post(self):
        args = parser.parse_args()
        p = args['principal_amount']
        n = args['period']
        r = args['rate']

        si = (p*n*r)/100.0

        return {'simple_interest' : si}

api.add_resource(SimpleInterest, '/simpleinterest/')

if __name__ == '__main__':
    app.run()

# Los tres argumentos 'principal_amount', 'period' and 'rate' se anaden al parser como argumentos
# con validaciones de sus respectivos tipos
# Ahora si enviamos requeste2 del arcivo accessing_siapp.py nos arroja un error con un mensaje de ayuda

        ## 400 b'{"message": {"principal_amount": "Principal amount must be a number"}}\n'