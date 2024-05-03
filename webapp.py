import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if "scientificName" in session:
        return render_template('error.html')
    else:
        session["scientificName"]=request.form['scientificName']
        return render_template('page2.html')


@app.route('/page3', methods=['GET', 'POST'])
def renderPage3():
    if "questionThree" in session:
        return render_template('error.html')
    else:
        session["questionTwo"]=request.form['questionTwo']
        return render_template('page3.html')

@app.route('/page10',methods=['GET','POST'])
def renderPage10():
    if "questionThree" in session:
        return render_template('error.html')
    else:
        session["1questionThree"]=request.form['1questionThree']
        session["2questionThree"]=request.form['2questionThree']
        q1 = "incorrect"
        q2 = "incorrect"
        q3_1 = "incorrect"
        q3_2 = "incorrect"
        if session["scientificName"] == "Bellis Perennis":
            q1 = "correct"
        if session["questionTwo"] == "the evaporation of water from a plant's leaves, stem, or flowers.":
            q2 = "correct"
        if  session["1questionThree"] == "Xylem" or session["1questionThree"] == "xylem":
            q3_1 = "correct"
        if session["2questionThree"] == "Phloem" or session["2questionThree"] == "phloem":
            q3_2 = "correct"
        return render_template('page10.html', q1=q1, q2=q2, q3_1=q3_1, q3_2=q3_2)
    
    '''
    if session["scientificName"] == "Bellis Perennis":
        q1 = correct
    else:
        (make the text red and show the correct answer under it)
      '''  
    
@app.route('/error')
def renderError():
    return render_template('error.html')
    
if __name__=="__main__":
    app.run(debug=False)