from flask import Flask
from controllers.controllers import exemplo

app = Flask (__name__)
app.register_blueprint(exemplo)

if __name__  == '__main__':
    app.run(debug=True)