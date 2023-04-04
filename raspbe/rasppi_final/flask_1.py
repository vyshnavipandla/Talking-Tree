from flask import*
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(120))
    Answer = db.Column(db.String(120))
    
#with app.app_context():
    #db.create_all()



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
	
	 
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
