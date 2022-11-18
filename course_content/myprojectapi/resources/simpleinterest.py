from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class SimpleInterest(Resource):

    # El metodo post del recurso captura de HTML variables: 'principal_amout', 'period' y 'rate
    # despues regresa un diccionario con la key 'simple_interest'
    def post(self):
        p = float(request.form['principal_amount'])
        n = int(request.form['period'])
        r = float(request.form['rate'])

        si = (p*n*r)/100.0

        return {'simple_interest':si}

# El recurso 'SimpleInteret' esta mapeado en el URL '/simpleinterest/'
api.add_resource(SimpleInterest, '/simpleinterest/')

if __name__ == '__main__':
    app.run()