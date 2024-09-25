from flask import Flask, redirect, session, render_template, send_from_directory, request
from os import path

app = Flask(__name__, template_folder="templates")
app.secret_key = '1234'

@app.route("/")
def index():
    # obtener el metodo que se esta utilizando
    # if request.method == "GET":
        # settear una variable de session en el servidor
        # session["logged"] = True
        # session["name"] = "jesus"        
    return render_template("login.html")

    # if request.method == "POST":
    #     # acceder a los valores enviados por formulario
    #     request.form["username"]
    #     request.form["password"]
    #     error = 'sos un crack'
    #     return render_template("login.html", error=error)

@app.route("/cuil", methods=['POST'])
def data():
    # acceder a los valores enviados por formulario
    genero = request.form["genero"]
    dni = request.form["dni"]
    return render_template("login.html", cuil=f'23-{dni}-1')    


@app.route("/favicon.ico")
def icon():
    return send_from_directory(path.join(app.root_path, 'static', 'image'), 'baloncesto.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/login.css")
def style():
    return send_from_directory(path.join(app.root_path, 'static', 'css'), 'login.css')

app.run(host="localhost", port=8080, debug=True)