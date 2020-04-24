from flask import Flask, render_template, request, url_for, flash, redirect
from flask import Flask
import pickle
import numpy
import csv
import pandas as pd
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#train test splitting

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '605f5a55f1eb7cee41339f2a3a33bb88'
db = SQLAlchemy(app)


#these are the classes which will send the data to databases
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    questions = db.Column(db.Text(), nullable=True)
    content = db.Column(db.Text(), nullable = False)
 
    def __repr__ (self):
        return f"Post('{self.username}' , '{self.date_posted}', '{self.questions}', '{self.content}')"

class Temp(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    temperature = db.Column(db.Text(), nullable=False)
    prob = db.Column(db.Text(), nullable=False)
    number = db.Column(db.Text(), nullable=False)

    def __repr__ (self):
        return f"Temp('{self.fullname}' , '{self.date_posted}', '{self.temperature}', '{self.prob}', '{self.number}')"

file = open('model.pkl', 'rb')
lr = pickle.load(file)
file.close()


# routes which will direct users to different URL's
@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        if(request.form['live'] == "Live-Data"):
            liveDict = request.form.to_dict()
            nation = liveDict['country']
            url = 'https://api.smartable.ai/coronavirus/stats/' + str(nation)
            params = {
            'Cache-Control': 'no-cache',
            'Subscription-Key': 'a5853f4359674b35b373ade277d73e24',
            }
            r = requests.get(url=url, params=params)
            r = r.text
            jsonData = json.loads(r)

            latestData = jsonData['stats']['breakdowns'][0]

            totalConfirmedCases = latestData['totalConfirmedCases']
            newlyConfirmedCases = latestData['newlyConfirmedCases']
            totalDeaths = latestData['totalDeaths']
            newDeaths = latestData['newDeaths']
            totalRecoveredcases = latestData['totalRecoveredCases']   

            return render_template('homepage.html', totalConfirmedCases = totalConfirmedCases, newlyConfirmedCases = newlyConfirmedCases, totalDeaths = totalDeaths, newDeaths= newDeaths, totalRecoveredcases = totalRecoveredcases)
    return render_template('homepage.html')


@app.route('/detector', methods=["GET", "POST"])
def mainfunc():
    if request.method == "POST":
        if (request.form['calculate'] == "Calculate probability"):
            myDict = request.form
            fever = int(myDict['fever'])
            age = int(myDict['age'])
            pain = int(myDict['pain'])
            diffBreathing = int(myDict['diffBreathing'])
            runnyNose = int(myDict['runnyNose'])
            tiredness = int(myDict['tiredness'])

            #Getting the probability
            input_data = [fever, pain, age, runnyNose, diffBreathing, tiredness]
            xy = str(lr.predict_proba([input_data])[0])
            yz = xy.split()[1]
            yz = yz[0:5]
            print(yz)
            return render_template('detector.html', fp = round(float(yz)*100))
    return render_template('detector.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/blog', methods=['GET', 'POST'])
def blogpage():
    posts = Post.query.all()
    return render_template('blog.html', posts = posts)

@app.route('/post', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":  
        form = request.form
        username = form['username']
        questions = form['questions']
        experiences = form['experiences']
        post = Post(username=username, questions = questions, content=experiences)
        db.session.add(post)
        db.session.commit()
    return render_template('post.html')

@app.route('/temp', methods=['GET', 'POST'])
def temp():
    if request.method == "POST":
        form = request.form
        fullname = form['fullname']
        temperature = form['temperature']
        prob = form['prob']
        number = form['number']
        flash(f'Temperature and probability for {fullname} uploaded to database', 'success')
        temp = Temp(fullname=fullname, temperature=temperature, prob=prob, number=number)
        db.session.add(temp)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('temp.html')


#running app
if __name__ == "__main__":
    app.run(debug=True)