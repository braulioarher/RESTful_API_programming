from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
import datetime as datetime

app = Flask(__name__)
api = Api(app)

# Define a variable 'blogsParser', an instance of 'reqparse.RequestParser' and
# add the arguments 'title', and 'article_text'
# 'title' must be a string and a required argument.
# 'article_text' must be a string and a required argument.

blogsParser = reqparse.RequestParser()   
blogsParser.add_argument('title', type=str, required=True)
blogsParser.add_argument('article_text', type=str, required=True)

blogs = {}

class BlogsAPI(Resource):
    def get(self, blog_id=None):
        '''Return 'blogs' dictionary if 'blog_id' is None.
        
           if blog_id is provided,
           Abort the request if 'blog_id' and not in keys of 'blogs' dictionary, or else
           Return the blog corresponding to given 'blog_id'
        '''
        if blog_id is None:
          return blogs
        if blog_id not in blogs:
          abort(404)
        return(blogs[blog_id])
        
    
    def post(self, blog_id):
        '''
        If 'blog_id' is not in keys of 'blogs' dictionary, create a new dictionary object
        'blog', with three keys 'title', 'article_text', and 'created_at'.
        The values of 'title', and 'article_text' to be captured from http form varaibles :
        'title', 'article_text.
        The value of 'created_at' must be current date time string represented by format '%Y-%m-%d %H:%M:%S'
        
        Add the created dictionary object to 'blogs' dictionary with key corresponding to given 'blog_id',
        and Return the created dictionary object.
        
        If 'blog_id' is in keys of 'blogs' dictionary, abort the request.
        
        use 'blogsParser' to parse arguments in input form.
        '''
        args = blogsParser.parse_args()
        if blog_id not in blogs:  
          created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          blogs[blog_id] = {'title': args['title'], 'article_text': args['article_text'], 'created_at': created}
          return blogs[blog_id]
        abort(404)
        
    
    def put(self, blog_id):
        '''
        If given 'blog_id' not in 'blogs' dictionary abort the request with 404 status code and message like shown below.
        
        Sample Error message : "Blog_Id 2 doesn't exist"
        
        Else, update the details of blog, identified by given 'blog_id', and return the updated blog details.
        
        use 'blogsParser' to parse arguments in input form.
        '''
        if blog_id not in blogs:
            abort(404, message="Blog_Id {} doesn't exist".format(blog_id))
        else:
          blogs[blog_id] = {'title': request.form['title'], "article_text": "This article talks about Python and illustrates how Python is used in application programming, with examples."}
          #, 'article_text': request.form['article_text']
          return blogs[blog_id]    
    
    def delete(self, blog_id):
        '''
        If 'blog_id' not in keys of 'blogs' dictionary, abort the request with 404 status code and message like shown below.
        
        Sample Error message : "Blog_Id 2 doesn't exist"
        
        Else delete the blog corresponding to given 'blog_id' from 'blogs' dictionary and respond with a message like shown below.
        
        Sample Delete response message : "Blog with Id 3 is deleted"
        '''
        if blog_id in blogs:
            response_string = "Blog with Id {} is deleted".format(blog_id)
            del blogs[blog_id]
            return response_string
        abort(404, message="Blog_Id {} doesn't exist".format(blog_id))
    
api.add_resource(BlogsAPI, '/blogs/',
                              '/blogs/<int:blog_id>/')

if __name__ == '__main__':
    app.run()