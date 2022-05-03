from flask import render_template
from application import main

@main.route("/")
def home():
    return render_template("index.html")

@app.route("/test", methods=['GET'])
def test():
nome = request.arg['meuparametro']

@app.route("/usuario", methods=['GET', 'POST'])
def inserir():
dados_post = request.data

@app.route("/usuario", methods=['GET', 'POST'])
def inserir():
