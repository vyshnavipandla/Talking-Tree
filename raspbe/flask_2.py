


from flask import*
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from polly_mmap import*
import RPi.GPIO as GPIO
import pywhatkit
from openai_1 import*
from weather_1 import*
from currency_1 import*
from time_1 import*
import boto3
import pyaudio
import mmap
import time
import io
import os
import webbrowser


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(120))
    Answer = db.Column(db.String(120))
pa = pyaudio.PyAudio()

    
    
#with app.app_context():
    #db.create_all()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
@app.route('/',methods=['GET','POST'])
def welcome_template():
	if request.method=='POST':
		Title=request.form['title']
		Title=Title.lower()
		Description=request.form['desc']
		todo=User(Question=Title.strip(),Answer=Description)
		db.session.add(todo)
		db.session.commit()
	Allwork=User.query.all()
	return render_template('index.html',data=Allwork)

@app.route('/delete/<int:id>')
def delete(id):
	Allwork=User.query.filter_by(id=id).first()
	db.session.delete(Allwork)
	db.session.commit()
	return redirect('/')
	
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
	if request.method=='POST':
		Title=request.form['title']
		Description=request.form['desc']
		Allwork=User.query.filter_by(id=id).first()
		Allwork.Question=Title
		Allwork.Answer=Description
		db.session.add(Allwork)
		db.session.commit()
		return redirect('/')
	Allwork=User.query.filter_by(id=id).first()
	return render_template('update.html',Allwork=Allwork)
	
@app.route('/voice')
def voice():
	return render_template('test.html')
	
@app.route('/submit', methods=['POST'])
def submit():
	data = request.get_json()
	text = data['text']
	text_1=text.lower()
	qa= User.query.filter_by(Question=text_1).first()
	if qa is not None:
		answer =qa.Answer
		#sample=qa[0]
		print(answer)
		mapy(answer)
	elif 'show me the images of' in text_1:
            text_1=text_1.replace('show me the images of'," ")
            webbrowser.open("https://www.google.com/search?q="+text+"&tbm=isch")
            GPIO.output(18, GPIO.LOW)
            return "As you wish"
	elif 'play' in text_1:
            text_1=text_1.replace('play'," ")
            pywhatkit.playonyt(text)
            GPIO.output(18, GPIO.LOW)
            return "As you wish"
	elif 'come back' in text_1:
            os.system("killall chromium-browser")
            GPIO.output(18, GPIO.LOW)
            return "As you wish"
	elif 'what is the weather' in text_1:
			weather=text_1.replace("what is the weather"," ")
			GPIO.output(18, GPIO.LOW)
			mapy(weath(weather))
	elif 'what is the currency value' in text_1:
			cur1=text_1.replace("what is the currency value"," ")
			GPIO.output(18, GPIO.LOW)
			mapy(kurr(cur1))
	elif 'what is the time' in text_1:
            GPIO.output(18, GPIO.LOW)
            mapy(tyme(text))
	else:
            GPIO.output(18, GPIO.LOW)
            mapy(intel(text_1))
	return jsonify({'text': text})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False,ssl_context=('cert.pem','key.pem'))



