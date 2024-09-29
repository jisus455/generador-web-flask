from flask import Flask, redirect, session, render_template, send_from_directory, request
from os import path

app = Flask(__name__, template_folder="templates")
app.secret_key = '1234'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':      
        return render_template("generate.html")

    if request.method == 'POST':
        genero = request.form["genero"]
        dni = request.form["dni"]
        return render_template("result.html", cuil=dni)    


@app.route("/generate.css")
def styleGenerate():
    return send_from_directory(path.join(app.root_path, 'static', 'css'), 'generate.css')

@app.route("/result.css")
def styleResult():
    return send_from_directory(path.join(app.root_path, 'static', 'css'), 'result.css')

@app.route("/favicon.ico")
def icon():
    return send_from_directory(path.join(app.root_path, 'static', 'image'), 'baloncesto.ico', mimetype='image/vnd.microsoft.icon')


app.run(host="localhost", port=8080, debug=True)