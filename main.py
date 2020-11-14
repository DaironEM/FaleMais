from flask import Flask, render_template, request
from talk_more import TalkMore
from function import fill_area_code, correct_lenght
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', titulo='FaleMais')


@app.route('/resultado', methods=['POST',])
def resultado():
    origin = fill_area_code(request.form['origem'])
    destination = fill_area_code(request.form['destino'])
    length = correct_lenght(request.form['tempo'])
    plan = request.form['select']
    talk_more = TalkMore(origin, destination, float(length), plan)

    return render_template('resultado.html', titulo='FaleMais', fale_mais=talk_more)


app.run(debug=True)
