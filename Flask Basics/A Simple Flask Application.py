from flask import Flask

### WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Hey you, you look damn beautiful!</h1>"

@app.route('/reply')
def reply():
    return "<h1>Hey there, Thanks!</h1>"


if __name__ == '__main__':
    app.run(debug=True)