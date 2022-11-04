from urllib import request, parse, error
import urllib

#METODO GET
request1 = request.Request("http://127.0.0.1:5000/blogs/")

try:
    response1 = request.urlopen(request1)
    print(response1.read())
except error.HTTPError as e:
    print(e.code, e.read())

#METODO POST
blog = {'title': 'hola mundo', 'article_text': 'sometext'}
data  =  urllib.parse.urlencode(blog)
data = data.encode('ascii')
request2 = request.Request('http://127.0.0.1:5000/blogs/1/', data=data, method='POST')
try:
    response2 = request.urlopen(request2)
    print(response2.read())
except error.HTTPError as e:
    print(e.code, e.read())

#METODO PUT
blog = {'title': 'hola mundo por dos', 'article_text': 'othersometext'}
data  =  urllib.parse.urlencode(blog)
data = data.encode('ascii')
request3 = request.Request('http://127.0.0.1:5000/blogs/1/', data=data, method='PUT')
try:
    response3 = request.urlopen(request3)
    print(response3.read())
except error.HTTPError as e:
    print(e.code, e.read())

#METODO GET
request1 = request.Request("http://127.0.0.1:5000/blogs/")

try:
    response1 = request.urlopen(request1)
    print(response1.read())
except error.HTTPError as e:
    print(e.code, e.read())

#METODO DELETE
request4 = request.Request("http://127.0.0.1:5000/blogs/1/", method='DELETE')
try:
    response4 =request.urlopen(request4)
    print(response4.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

#METODO GET
request1 = request.Request("http://127.0.0.1:5000/blogs/")

try:
    response1 = request.urlopen(request1)
    print(response1.read())
except error.HTTPError as e:
    print(e.code, e.read())