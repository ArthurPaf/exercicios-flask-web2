from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para Juros Simples (Padrão)
@app.route('/', methods=['GET', 'POST'])
def juros_simples():
    dados = None
    erro = None
    if request.method == 'POST':
        try:
            c = float(request.form['capital'])
            i = float(request.form['taxa'])
            t = int(request.form['tempo'])

            if c <= 0 or t <= 0:
                erro = "Capital e Tempo devem ser maiores que zero!"
            else:
                juros = c * (i / 100) * t
                dados = {"capital": c, "juros": juros, "montante": c + juros, "tipo": "Simples"}
        except ValueError:
            erro = "Valores inválidos!"
    return render_template('index.html', dados=dados, erro=erro, aba='simples')

# Rota BÔNUS: Juros Compostos
@app.route('/compostos', methods=['GET', 'POST'])
def juros_compostos():
    dados = None
    erro = None
    if request.method == 'POST':
        try:
            c = float(request.form['capital'])
            i = float(request.form['taxa']) / 100
            t = int(request.form['tempo'])

            if c <= 0 or t <= 0:
                erro = "Capital e Tempo devem ser maiores que zero!"
            else:
                # Fórmula: M = C * (1 + i)^t
                montante = c * (1 + i)**t
                juros = montante - c
                dados = {"capital": c, "juros": juros, "montante": montante, "tipo": "Compostos"}
        except ValueError:
            erro = "Valores inválidos!"
    return render_template('index.html', dados=dados, erro=erro, aba='compostos')

if __name__ == '__main__':
    app.run(debug=True)