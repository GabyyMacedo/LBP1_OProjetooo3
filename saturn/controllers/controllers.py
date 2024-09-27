from flask import Blueprint, render_template
from models.models import p, pessoa

exemplo = Blueprint("exemplo", __name__)

@exemplo.route("/")
def exibir():
    return render_template('index.html')

@exemplo.route("/oi")
def exibir2():
    return render_template('index.html', sla = p, nsei=pessoa)
  