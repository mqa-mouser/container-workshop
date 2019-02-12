from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mouser!"

@app.route("/raude")
def raude():
    return "Hi boss!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
