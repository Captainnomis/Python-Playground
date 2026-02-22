from flask import Blueprint, render_template, url_for


main = Blueprint('main', __name__)  #create blueprint called main

@main.route('/') #route for homepage (root)

def index():
    return render_template('index.html')  #when someone visits root, show this

@main.route('/profile')
def profile():
    return render_template('profile.html')