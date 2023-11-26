from flask import Flask, render_template, flash 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#aggiunta database
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///utenti.db'
#secret key
app.config['SECRET_KEY']= "mia secret key"
#inzizializzazione database
db = SQLAlchemy(app)

#crazione model
class Utenti(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    data_Inserimento = db.Column(db.DateTime, default=datetime.utcnow)
 
    # create a string  
    def __repr__(self):
        return '<Nome %r>' % self.nome

#creazione classe form 
class UtenteForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    invia = SubmitField("Invia")

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
    
#pagina add_user    
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    nome = None
    form = UtenteForm()
    if form.validate_on_submit():
        utente = Utenti.query.filter_by(email=form.email.data).first()
        if utente is None:
            utente = Utenti(nome=form.nome.data, email=form.email.data)
            db.session.add(utente)
            db.session.commit()
        nome = form.nome.data
        form.nome.data = '' 
        form.email.data = ''
        flash("Utente aggiunto!")
    gliUtenti = Utenti.query.order_by(Utenti.data_Inserimento)    
    return render_template('add_user.html', form=form, nome=nome, gliUtenti=gliUtenti)


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
def paginaErroreServer(e):
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
