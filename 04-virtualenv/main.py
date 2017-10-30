import flask

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask! (flask v.{})".format(flask.__version__)
    
if __name__ == '__main__':
    app.run()
