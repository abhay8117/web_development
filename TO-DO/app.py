# from crypt import methods
# from email.policy import default
from turtle import title
from flask import Flask, render_template, url_for, redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    des=db.Column(db.String(500), nullable=False)
    date_c=db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return  f"{self.sno} - {self.title}"

# @app.route('/')
# def index():
#     todo = Todo(title='First',des='I love u')
#     db.session.add(todo)
#     db.session.commit()

#     return render_template('index.html')


 
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        des = request.form['des']
        todo = Todo(title=title, des=des)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method ==  'POST':
        title = request.form['title']
        des = request.form['des']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.des = des   
        db.session.add(todo)
        db.session.commit()
        redirect('/')
    
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ =='__main__':
    app.run(debug=True)
