
from flask import Flask,render_template,url_for
from flask.json import jsonify
import requests
import os

app=Flask(__name__,template_folder='templates')

url= f'https://jsonplaceholder.typicode.com/'

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

# @app.route('/table')
# def table():
#     response=requests.get(url)
#     data=response.json()
#     return render_template('table.html',  data=data)


@app.route('/table/<endpoint_name>')
def table(endpoint_name):
    url1=os.path.join(url,endpoint_name)
    response=requests.get(url1)
    data=response.json()
    return render_template('table.html',  data=data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)

