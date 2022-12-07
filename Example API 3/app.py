from flask import Flask,render_template,url_for,request

app=Flask(__name__)

 
@app.route('/')
@app.route('/index.html')
def Home():
    return render_template('index.html')

# @app.route('/<string : page_name>')
# def pages(page_name):
#     return render_template('page_name')


if __name__=='__main__':
    app.run(debug=True)