from flask import Flask, redirect, session, render_template, send_from_directory, request, send_file
from os import path

from business.CuilGenerate import CuilGenerate
from business.DataDownload import DataDownload

from data.HistoryData import HistoryData

app = Flask(__name__, template_folder="templates")
app.secret_key = '1234'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':   
        return render_template("index.html")

    if request.method == 'POST':
        genero = request.form["genero"]
        dni = request.form["dni"]
        cuil, error = None, None
        try:
            logicCuil = CuilGenerate(dni, genero)
            logicCuil.validate()
            cuil = logicCuil.calculate()

            data = {'genero': genero, 'dni': dni, 'cuil':cuil}
            HistoryData().addHistory(data)

            logicData = DataDownload(data)
            logicData.write()
        except Exception as e:
            error = e.args[0]

        return render_template("index.html", cuil=cuil, error=error)

@app.route("/index.css")
def styleIndex():
    return send_from_directory(path.join(app.root_path, 'static', 'css'), 'index.css')

@app.route("/history")
def history():
    history = HistoryData().getHistory()  
    column =  HistoryData().getColumn()  
    print(column)
    return render_template("history.html", history=history, column=column)    
    
@app.route("/history.css")
def styleHistory():
    return send_from_directory(path.join(app.root_path, 'static', 'css'), 'history.css')

@app.route("/favicon.ico")
def icon():
    return send_from_directory(path.join(app.root_path, 'static', 'image'), 'formulario.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/download")
def downloadFile():
    pathFile = path.join(app.root_path, 'static', 'result', 'data.txt')
    return send_file(pathFile, as_attachment=True)

app.run(host="localhost", port=8080, debug=True)