from flask import Flask, render_template 

#creazione istanza FLask

app = Flask(__name__)

#creazione route docrator
@app.route('/')
def index():
    firstName = "Tano"
    pizzePreferite = ["margherita", "marinara", "calzone", 1978]
    return render_template('index.html', firstName=firstName, pizzePreferite=pizzePreferite)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name )
    #return "<h1>Hello {}!!!</h1>".format(name)

#errore URL invalido
@app.errorhandler(404)
def paginaNonTrovata(e):
    return render_template('404.html'), 404

#errore del server
@app.errorhandler(500)
def paginaNonTrovata(e):
    return render_template('500.html'), 500