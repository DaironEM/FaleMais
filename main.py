from flask import Flask, render_template, request
from fale_mais import FaleMais
from funcoes import completa_codigo_de_area
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', titulo='FaleMais')


@app.route('/resultado', methods=['POST',])
def resultado():
    origem = completa_codigo_de_area(request.form['origem'])
    destino = completa_codigo_de_area(request.form['destino'])
    duracao = request.form['tempo']
    plano = request.form['select']
    fale_mais = FaleMais(origem, destino, float(duracao), plano)

    return render_template('resultado.html', titulo='FaleMais', fale_mais=fale_mais)


app.run(debug=True)
