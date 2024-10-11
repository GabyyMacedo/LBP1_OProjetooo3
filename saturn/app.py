from flask import Flask, redirect, url_for, render_template
from controllers.controllers import projeto

app = Flask (__name__)
app.secret_key = 'chave_secreta'

app.register_blueprint(projeto)

if __name__  == '__main__':
    app.run(debug=True)
