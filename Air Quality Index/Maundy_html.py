
from flask import Flask,render_template,url_for
import requests
import time
app=Flask(__name__,template_folder='template')



token='9621d4bafe1ffbc165e7439c4601e38ae45af49f'
base_url='https://api.waqi.info/feed'
country='india'

 
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')




@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/a.html')
def content():
    return render_template('a.html')


if __name__=='__main__':
    app.run()