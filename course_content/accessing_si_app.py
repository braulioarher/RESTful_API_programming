import urllib
from urllib import request, parse

data = {
    'principal_amount' : 15000.0,
    'period' : 5,
    'rate' : 8
}

data = parse.urlencode(data)
data = data.encode('ascii')

request1 = request.Request('http://127.0.0.1:5000/simpleinterest/', method='POST', data=data)

try:
    response1 = request.urlopen(request1)
    print(response1.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

# El ejemplo anterior pasa una peticion POST al recurso SimpleInterest
# Despues el recurso procesa la informacion y regreza la siguiente respuesta

    #b'{"simple_interest": 6000.0}\n'

## A continuacion se envia otra peticion POST con pequenas diferecncia en la informacion

data = {
    'principal_amount' : 'hello',
    'period': 5,
    'rate' : 8
}
data = parse.urlencode(data)
data = data.encode('ascii')

request2 = request.Request('http://127.0.0.1:5000/simpleinterest/', method='POST', data=data)
try:
    response2 = request.urlopen(request2)
    print(response2.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

# La peticion anterior asigna una string a 'principal_amount'
# Dado que hello no se puede convertir a tipo flotante la respuesta regresara un error como se muestra:

        # 500 b'{"message": "Internal Server Error"}\n'