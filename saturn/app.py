from flask import Flask, render_template
from controllers.controller import projeto

app = Flask (__name__)
app.secret_key = 'saturn'

app.register_blueprint(projeto)

@app.errorhandler(404) #erro de pagina não encontrada
def erro404(e):
    return render_template('404.html'), 404

@app.errorhandler(401) #erro de pagina não encontrada
def erro404(e):
    return render_template('401.html'), 401

if __name__  == '__main__':
    app.run(debug=True)