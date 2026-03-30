from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora_desconto():
    valor_desconto = None
    preco_final = None
    erro = None

    if request.method == 'POST':
        try:
            preco = float(request.form['preco'])
            porcentagem = float(request.form['porcentagem'])
            
            valor_desconto = (preco * porcentagem) / 100
            preco_final = preco - valor_desconto
        except ValueError:
            erro = "Por favor, preencha os valores corretamente."

    return render_template('index.html', desconto=valor_desconto, final=preco_final, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)