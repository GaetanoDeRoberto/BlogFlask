from flask import Flask, render_template, flash 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

app = Flask(__name__)
app.config['SECRET_KEY']= "mia secret key"

#creazione classe form 
class NomeForm(FlaskForm):
    nome = StringField("Inserisci il tuo nome", validators=[DataRequired()])
    invia = SubmitField("Invia")

#creazione route decoretor pagina index
@app.route('/')
def index():
    firstName = "Tano"
    pizzePreferite = ["margherita", "marinara", "calzone", 1978]
    return render_template('index.html', firstName=firstName, pizzePreferite=pizzePreferite)
    
#pagina user
@app.route('/user/<nome>')
def user(nome):
    return render_template("user.html", nome=nome )
    #return "<h1>Hello {}!!!</h1>".format(name)

#errore URL invalido
@app.errorhandler(404)
def paginaNonTrovata(e):
    return render_template('404.html'), 404

#errore del server
@app.errorhandler(500)
def paginaNonTrovata(e):
    return render_template('500.html'), 500

@app.route('/nome', methods=['GET', 'POST'])
def nome():
    nome = None
    form = NomeForm()
    #Validazione form 
    if form.validate_on_submit():
        nome = form.nome.data
        form.nome.data = ''
        #messaggio da mostrare dopo il submit del form
        flash("Nome inviato correttamente!")
    return render_template('nome.html', nome=nome, form=form)


