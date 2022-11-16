from flask import Flask,redirect,url_for,render_template,request

# Integrating HTML with Flask
app = Flask(__name__)



@app.route('/')
def welcome():
    return render_template('submit.html')

@app.route('/result/<int:score>')
def result(score):
    res_txt = ""
    if score>=50:
        res_txt = "Pass"
    else:
        res_txt = "Fail"
    return render_template('result.html',result = res_txt)


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        science = float(request.form['science'])
        history = float(request.form['history'])
        wildlife = float(request.form['wildlife'])
        datascience = float(request.form['datascience'])
        maths = float(request.form['maths'])
        res = (science+history+wildlife+datascience+maths)/5
        return redirect(url_for('result',score=res))

'''
@app.route('/')
def welcome():
    return render_template('index.html')

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
    return redirect(url_for(res,score=score))'''

if __name__ == '__main__':
    app.run(debug=True)