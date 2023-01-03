from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/errorPage')
def errorPage():
    return render_template('errorPage.html')


@views.route('/notification')
def notification():
    return render_template('notification.html')


@views.route('/buatPertanyaan')
def buatPertanyaan():
    return render_template('buatPertanyaan.html')


@views.route('/login')
def login():
    return render_template('login.html')


@views.route('/createAccount')
def createAccount():
    return render_template('create-account.html')


@views.route('/forgotPassword')
def forgotPassword():
    return render_template('forgot-password.html')
