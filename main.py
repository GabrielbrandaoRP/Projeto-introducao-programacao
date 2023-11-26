import os
import csv
from flask import Flask

app = Flask(__name__)

# Preparação para o ambiente Flask em desenvolvimento
os.environ['FLASK_DEBUG'] = 'True'
app.debub = os.environ.get('FLASK_DEBUG') == 'True'

# Rotas do Projeto
@app.route('/')
def index():

    # criação de lista vazia
    glossario_de_termos = []

    # Abrir o arquivo e colocá-lo
    with open(
            'bd_glossario.csv',
            newline='',
            enconding='utf-8') as arquivo:

        leitor = csv.reader(arquivo, delimiter=';')

        for linha in leitor:
            glossario_de_termos.append(linha)

    return render_template(
        'index.html'
        glossario_de_termos=glossario_de_termos
    )

if __name__ == '__main__':
    app.run()