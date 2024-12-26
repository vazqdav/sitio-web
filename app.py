from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/comprar')
def comprar():
    return render_template('comprar.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    greeting = f"¡Hola, {name}!"
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
