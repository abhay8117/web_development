from flask import Flask,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)

# class students(db.Model):
#     id = db.Column('student_id', db.Integer, primary_key = True)
#     name = db.Column(db.String(100))
#     city = db.Column(db.String(50))
#     addr = db.Column(db.String(200)) 
#     pin = db.Column(db.Integer(6))

# def __init__(self, name, city, addr,pin):
#    self.name = name
#    self.city = city
#    self.addr = addr
#    self.pin = pin

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    # db.create_all(app)
    app.run(debug=True)