from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from pymongo import MongoClient
from fpdf import FPDF
import os
import tempfile
import io


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ht ht'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/htUniversite'
mongo = PyMongo(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['htuniversite']
users_collection = db['giris']

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, username, email_host, password):
        self.username = username
        self.email_host = email_host
        self.password = password
        self.id = f"{username}@{email_host}"

    @staticmethod
    def get(user_id):
        username, email_host = user_id.split('@')
        user_data = mongo.db.giris.find_one({'username': username, 'emailHost': email_host})
        if user_data:
            return User(user_data['username'], user_data['emailHost'], user_data['password'])
        return None

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email_host = request.form['emailHost']
        password = request.form['password']
        user_data = mongo.db.giris.find_one({'username': username, 'emailHost': email_host})

        if user_data and user_data['password'] == password:
            user = User(username, email_host, password)
            login_user(user)
            return redirect(url_for('dersec'))
        else:
            flash('Geçersiz kullanıcı adı veya şifre')
    return render_template('login.html')




@app.route('/dersec')
@login_required
def dersec():
    return render_template('dersec.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
 

@app.route('/misafir', methods=['GET', 'POST'])
def misafir():
    if request.method == 'POST':
        username = request.form['username']
        email_host = request.form['emailHost']
        password = request.form['password']
        existing_user = mongo.db.giris.find_one({'username': username, 'emailHost': email_host})

        if existing_user is None:
            mongo.db.giris.insert_one({'username': username, 'emailHost': email_host, 'password': password})
            flash('Misafir kullanıcı başarıyla eklendi!')
            return redirect(url_for('login'))
        else:
            flash('Kullanıcı zaten mevcut!')

    return render_template('misafir.html')


@app.route('/')
def anasayfa():
    return render_template('anasayfa.html')

@app.route('/global')
def globall():
    return render_template('globall.html')

@app.route('/onay')
def onay():
    return render_template('onay.html')


@app.route('/kutup')
def kutup():
    return render_template('kutup.html')




if __name__ == '__main__':
    app.run(debug=True)