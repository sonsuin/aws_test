from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def good():
    return render_template('good.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route("/hello2")
def hello2():
    return render_template("hello2.html")



if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)