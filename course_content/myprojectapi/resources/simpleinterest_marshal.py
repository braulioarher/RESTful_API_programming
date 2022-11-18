from flask_restful import Resource, Api
import datetime as dt
from flask_restful import fields, marshal_with


from flask_restful import reqparse

# Se crea un parser, un Objeto de la clase RequestParser
parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument('principal_amount', type=float, help='Principal amount must be a number')
parser.add_argument('period', type=int, help='No. of years must be an integer')
parser.add_argument('rate', type=float, help='Rate must be a number')

resorce_fields = {
    'simple_interest': fields.Raw,
    'computed_on': fields.DateTime(dt_format='rfc822')
}

class SimpleInterest(Resource):

    @marshal_with(resorce_fields)
    def post(self):
        args = parser.parse_args()
        p = args['principal_amount']
        n = args['period']
        r = args['rate']

        si = (p*n*r)/100.0

        return {'simple_interest': si, 'computed_on':dt.datetime.now()}


# Los campos formateados 'simple_interes' y 'computed_on' son definidos como un 'raw string' y 'rfc822' 

# Si tratammos de enviar una peticion 'POST' recibiriamos:

# b'{"computed_on": "Thu, 08 Nov 2018 16:39:48 -0000", "simple_interest": 6000.0}\n'