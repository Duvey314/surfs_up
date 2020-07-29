from flask import Flask

# create a flask instance
app = Flask(__name__)

# set flask route
@app.route('/')

def hello_world():
    return 'Hello World'