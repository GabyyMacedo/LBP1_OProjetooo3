# Projeto_LBP

1. Criar umas pasta
2. Abrir terminal da pasta (ou abrir um terminal e ir até a pasta -> cd 'nome da pasta'
3. ----TERMINAL----
4. Criar abriente virtual -> python3 -m venv 'criar nome do ambiente virtual'
5. abrir ambiente virtual -> source 'nome do ambiente virtual'/bin/activate
6. instalar dependências (pip intall flask
7. ----VS CODE----
8. Abrir a primeira pasta no visual studio code
9. Criar outra pasta para iniciar o projeto
10. ***o projeto deve ser feito do LADO do ambiente virtual e NÃO dentro dele
11. Criar arquivos para realizar o projeto
12. CRTL + SHIFT + P
13. --> Python: select interpreter
14. --> Colocar opção recomendada
15. ----CONTROLLERS----
16. ***importa o Blueprint e faz rotas
17. pasta 'controllers' -> arquivo 'controllers.py'
18. -> from flask import Blueprint, render_template
19. -> exemplo = Blueprint("exemplo", __name__) ***o '"exemplo"' foi definido no models
20. -> @exemplo.route("/")
       def exibir():
          return render_template('index.html')
21. ----MODELS----
22. ***cria classes e funções
23. pasta 'models' -> arquivo 'models.py'
24. ----STATIC----
25. pasta 'static' -> arquivo 'style.css'
26. ----TEMPLATES----
27. pasta 'templates' -> arquivo 'index.html'
28. ***linkar css no html ->  <head>
                                <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}" media="screen" />
                              </head>      
30. ----APP.PY----
31. ***importa o flask e as dependências
32. -> from flask import Flask
33. -> from controllers import exemplo
34. -> app = Flask (__name__)
35. -> app.register_blueprint(exemplo) ***o 'exemplo' foi nomeado no controllers
36. -> if __name__  == '__main__':
          app.run(debug=True)
