from flask import Flask 

app=Flask(__name__)

@app.route('/')
def index():
    return 'This Page has been created by python using flask'


if __name__ =="__main__":
    app.run(debug=True)