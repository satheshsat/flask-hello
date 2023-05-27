from flask import Blueprint, render_template, session,abort

app1 = Blueprint('hi',__name__)

@app1.route("/hi")
def hi():
    return [{"hi":"hello"}]
