from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def verificador():
    resultado_paridade = None
    resultado_sinal = None
    numero_digitado = None
    erro = None

    if request.method == 'POST':
        try:
            # Pegamos o número do formulário
            n = int(request.form['numero'])
            numero_digitado = n

            # 1. Verificação de Paridade (usando o resto da divisão %)
            if n % 2 == 0:
                resultado_paridade = "Par"
            else:
                resultado_paridade = "Ímpar"

            # 2. Verificação de Sinal
            if n > 0:
                resultado_sinal = "Positivo"
            elif n < 0:
                resultado_sinal = "Negativo"
            else:
                resultado_sinal = "Zero"

        except ValueError:
            erro = "Por favor, digite um número inteiro válido!"

    return render_template('index.html', 
                           n=numero_digitado, 
                           paridade=resultado_paridade, 
                           sinal=resultado_sinal, 
                           erro=erro)

if __name__ == '__main__':
    app.run(debug=True)