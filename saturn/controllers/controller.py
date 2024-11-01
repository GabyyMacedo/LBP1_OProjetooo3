from flask import Blueprint, render_template, request, redirect, url_for, session,flash, abort
from models.Usuario import listaUsuarios

projeto = Blueprint("login", __name__)

@projeto.route('/')
def index():
    return render_template('index.html')

@projeto.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome=request.form.get('nome')
        senha=request.form.get('senha')
        for usuario in listaUsuarios:
            if usuario.nome == nome and usuario.senha==senha:
                session["idUser"] = usuario.id
                return redirect (url_for('login.dashboard'))    #'login.dashboard' --> o login. é o nome dado ao blueprint (está chamando o blueprint)
        flash("Credenciais inválidas", 'error') #flash message
        flash("Tente novamente", 'info')    #flash message
    return render_template('login.html')

rotas_publicas = ["login.login", "login.index"] #rotas que podem ser acessadas sem login

@projeto.before_request #middleware (hooks)
def verificaLogin(): #pergunta se o usuario está logado (para não "gastar" processamento)
    if request.endpoint=='login.login' and 'idUser' in session:
        return redirect(url_for('login.index'))
    
    if request.endpoint in rotas_publicas:
        return 
    
    if "idUser" not in session: #verifica se o user ta na sessão
        return redirect(url_for('login.login'))
    return

@projeto.route('/dashboard')
def dashboard():
        return render_template('dash.html')  


@projeto.route("/admin")
def admin():
    if session.get("idUser") != 1:
        abort(401)
    return render_template('admin.html')

@projeto.route('/logout')
def logout():
    session.pop("idUser", None) #"remove" o usuário
    return redirect (url_for('login.index'))
