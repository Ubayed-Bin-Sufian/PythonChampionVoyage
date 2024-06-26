# Practice from https://www.youtube.com/watch?v=f085KDOy43k

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/blog")
def blog():
    return "This is the blog page"

# @app.route("/blog/<blog_id>")
# def blogpost(blog_id):
#     return "This is the blog post number " + str(blog_id)

# Specifying with datatype
@app.route("/blog/<string:blog_id>")
def blogpost(blog_id):
    return "This is the blog post number " + blog_id

if __name__=="__main__":
    app.run(debug=True)