from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
  return render_template('home.html')

@views.route('/errorPage')
def errorPage():
  return render_template('errorPage.html')

@views.route('/notification')
def notification():
  return render_template('notification.html')