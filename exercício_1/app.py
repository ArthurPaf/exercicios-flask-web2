from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def conversor():
    resultado = None
    erro = None
    
    if request.method == 'POST':
        try:
            # Pega o valor do input 'celsius' do HTML
            celsius = float(request.form['celsius'])
            # Aplica a fórmula: F = C * 1.8 + 32
            fahrenheit = celsius * 1.8 + 32
            resultado = f"{celsius}°C é igual a {fahrenheit:.2f}°F"
        except ValueError:
            erro = "Por favor, digite um número válido!"

    return render_template('index.html', resultado=resultado, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)