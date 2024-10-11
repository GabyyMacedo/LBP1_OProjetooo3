from flask import Blueprint, render_template, session, redirect, url_for, request
from models.models import Users

projeto = Blueprint("exemplo", __name__)

@projeto.route("/")
def index():
    if 'username' in session:
        return f'Bem-vindo, {session["username"]}!'
    return 'Você não está logado'

@projeto.route("/login", methods=['POST', 'GET'])
def login():
    if request.method =='POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return render_template("index.html")
    
@projeto.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

#projeto = Blueprint("exemplo", __name__)

#@app.route("/")
#def index():
    #return render_template('index.html')

#@app.route("/oi")
#def exibir2():
    #return render_template('index.html', sla = p, nsei=pessoa)
