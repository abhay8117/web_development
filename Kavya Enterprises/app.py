from enum import unique
from urllib import request
from flask import Flask,render_template,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class visitors(db.Model):
   id = db.Column('visitor_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   email= db.Column(db.String(50),unique = True, nullable= False)
   phone = db.Column(db.Integer)
   sub = db.Column(db.String(200))
   msg = db.Column(db.String(500))

   def __init__(self, name, email,phone,sub,msg):
        self.name = name
        self.email = email
        self.phone = phone
        self.sub = sub
        self.msg = msg

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST' :
        if not request.form['name'] or not request.form['email'] or not request.form['phone']:
            flash('Please enter all fields')
        else:
            visitor = visitors(request.form['name'], request.form['email'], request.form['phone'], request.form['sub'], request.form['msg'])
            flash('Thank you for your visiting')

            db.session.add(visitor)
            db.session.commit()
            flash("Succesfully")

    return render_template('contact.html', title='Contact')

@app.route('/services')
def services():
    return render_template('services.html',title='Services')

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)