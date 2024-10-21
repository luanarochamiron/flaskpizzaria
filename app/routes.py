from app import app
from flask import render_template, redirect, url_for, request
import requests
import json

link = "https://flakstintluana-default-rtdb.firebaseio.com/"

@app.route('/')
@app.route('/index')
def index():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        pizzas = requisicao.json()
        
        if not pizzas:
            message = "Não há pizzas disponíveis no momento."
            return render_template('index.html', titulo="Página Inicial", message=message, pizzas=None)
        
        return render_template('index.html',titulo="Página Inicial", pizzas=pizzas)
    except Exception as e:
        return f'Ocorreu um erro\n{e}'

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastrar pizza")

@app.route('/atualizar')
def atualizar():
    return render_template('atualizar.html', titulo="Atualizar pizza")

@app.route('/excluir')
def excluir():
    return render_template('excluir.html', titulo="Excluir pizza")

@app.route('/pizza/cadastrar', methods=['POST'])
def cadastrarPizza():
    try:
        nome = request.form.get("nome")
        preco = int(request.form.get("preco"))
        pedacos = int(request.form.get("pedacos"))
        
        dados = {
            "nome": nome,
            "preco": preco,
            "pedacos": pedacos
        }
        
        requests.post(f'{link}/cadastro/.json', data = json.dumps(dados))
        
        return redirect(url_for("index"))
    except Exception as e:
        return f'Ocorreu um erro\n{e}'

@app.route('/pizza/excluir', methods=['POST'])
def excluirPizza():
    try:
        id = request.form.get("id")
        
        requests.delete(f'{link}/cadastro/{id}/.json')
        
        return redirect(url_for("index"))
    except Exception as e:
        return f'Ocorreu um erro\n{e}'
    
@app.route('/pizza/atualizar', methods=['POST'])
def atualizarPizza():
    try:
        id = request.form.get("id")
        nome = request.form.get("nome")
        preco = int(request.form.get("preco"))
        pedacos = int(request.form.get("pedacos"))
        
        dados = {
            "id": id,
            "nome": nome,
            "preco": preco,
            "pedacos": pedacos
        }
        
        requests.patch(f'{link}/cadastro/{id}/.json', data=json.dumps(dados))
        
        return redirect(url_for("index"))
    except Exception as e:
        return f'Ocorreu um erro\n{e}'
