from flask import Flask
app=Flask(__name__)
@app.route('/hello')	
def hello():
    return "hello"
@app.route('/hello/<name>')
def helloname(name):
    return F"hello{name}"
if __name__=="__main__":
    app.run(debug=True)
