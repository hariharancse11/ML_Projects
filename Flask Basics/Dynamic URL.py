from flask import Flask,redirect,url_for

### Variable Rules and Url Building
app = Flask(__name__)

@app.route('/')
def welcome():
    return("Welcome to the Home Page!")

@app.route('/success/<int:score>')
def success(score):
    return("The Person has Passed and the score is : "+str(score))

@app.route('/fail/<int:score>')
def fail(score):
    return("The person has Failed and the score is : "+str(score))

@app.route('/results/<int:score>')
def results(score):
    res = ""
    if score<50:
        res = "fail"
    else:
        res = "success"
    return redirect(url_for(res,score=score))

if __name__ == '__main__':
    app.run(debug=True)