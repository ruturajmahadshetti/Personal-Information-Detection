from flask import Flask,render_template

app= Flask(__name__)


@app.route('/')
def index():
    return "Ruturaj"

if __name__=="__main":
    app.run(debug=True)