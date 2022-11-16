from urllib import request, response
import urllib

request1 = request.Request('http://127.0.0.1:5000/index/')

try:
    response1 = request.urlopen(request1)
    print(response1.read())
    print('STATUS :',response1.status)
    print(response1.info())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

# El codigo seguiente manda tres peticiones Post

course = {'course_name' : 'Machine Learning'}
data = urllib.parse.urlencode(course)
data = data.encode('ascii')

request2 = request.Request('http://127.0.0.1:5000/Courses/1', data=data, method='POST')
try:
    response2 = request.urlopen(request2)
    print(response2.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

course = {'course_name' : 'Artificial Intelligence'}
data = urllib.parse.urlencode(course)
data = data.encode('ascii')
request3 = request.Request('http://127.0.0.1:5000/Courses/2', data=data, method='POST')
try:
    response3 = request.urlopen(request3)
    print(response3.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

course = {'course_name' : 'Cloud Computing'}
data = urllib.parse.urlencode(course)
data = data.encode('ascii')
request4 = request.Request('http://127.0.0.1:5000/Courses/3', data=data, method='POST')
try:
    response4 = request.urlopen(request4)
    print(response4.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

# El siguiente codigo manda dos peticiones GET 
# el primer request regresa todos los cursos registrados mientras que el segundo solo el course_id == 1

request5 = request.Request('http://127.0.0.1:5000/Courses/')
try:
    response5 = request.urlopen(request5)
    print(response5.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

request6 = request.Request('http://127.0.0.1:5000/Courses/1')
try:
    response6 = request.urlopen(request6)
    print(response6.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

# Se crean dos peticiones una para eliminar y la segunda para obtener datos

request7 = request.Request('http://127.0.0.1:5000/Courses/2', method='DELETE')
try:
    response7 = request.urlopen(request7)
    print(response7.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())
    
request8 = request.Request('http://127.0.0.1:5000/Courses/')
try:
    response8 = request.urlopen(request8)
    print(response8.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

## Se crean dos peticiones para una para modificar la informacion mediante el metodo PUT y la otra muestra los cursos

course = {'course_name' : 'Microservices'}
data = urllib.parse.urlencode(course)
data = data.encode('ascii')
request9 = request.Request('http://127.0.0.1:5000/Courses/3', data=data, method='PUT')
try:
    response9 = request.urlopen(request9)
    print(response9.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())
    
request10 = request.Request('http://127.0.0.1:5000/Courses/')
try:
    response10 = request.urlopen(request10)
    print(response10.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())  