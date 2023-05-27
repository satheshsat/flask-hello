from flask import Flask
from hi import app1

app = Flask(__name__)
app.register_blueprint(app1)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
