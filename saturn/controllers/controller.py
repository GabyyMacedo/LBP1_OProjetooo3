from flask import Blueprint, render_template, request, redirect, url_for, session,flash, abort, make_response
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
    print(1)
    if request.endpoint=='login.login' and 'idUser' in session:
        return redirect(url_for('login.index'))
    print(2)
    if request.endpoint in rotas_publicas:
        return 
    print(3)
    if "idUser" not in session: #verifica se o user ta na sessão
        return redirect(url_for('login.login'))
    print(4)
    return

@projeto.route('/dashboard')
def dashboard():
        return render_template('dash.html')  

@projeto.route('/logout')
def logout():
    response=make_response(redirect(url_for("login.index")))
    session.pop("idUser", None) #"remove" o usuário
    response.set_cookie('nome', '', expires=0)
    response.set_cookie('senha', '', expires=0)
    return response

@projeto.route("/admin")
def admin():
    if session.get("idUser") != 1:
        abort(401)
    return render_template('admin.html')

@projeto.route("/cookie")   
def cookies():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        response=make_response(render_template('fim.html')) #cia os cookies
        if nome == listaUsuarios:
            response.set_cookie('nome', 'Correto', max_age=60 * 60 *24)
        else:
            response.set_cookie('nome', 'Incorreto', max_age=60 * 60 *24)

        if senha == listaUsuarios:
            response.set_cookie('senha', 'Correto', max_age=60 * 60 *24)
        else: 
            response.set_cookie('senha', 'Incorreto', max_age=60 * 60 *24)
        return response
    return render_template('login.html')

