from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>Byah! rpasto.com is the <em>first</em> proud member of the <a href=\"http://superrhino.net/\">SuperRhino</a> website conglomerate to be written in python!</h1>"
if __name__ == "__main__":
    app.run()

