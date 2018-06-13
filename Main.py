from flask import Flask,request,render_template
import Controller, Objects

app = Flask(__name__)
app.secret_key = 'admin'

@app.route('/')
def indexPage():
    Controller.Controller()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
