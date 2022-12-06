from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from . import helpers
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, current_user, logout_user
import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    date = datetime.datetime.today()
    this_year = str(date).split('-')[0]
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfuly", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorect email or password', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user, year=this_year)

@auth.route('/logout')
@login_required
def lougout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('User already exists', category='error') 
        elif len(email) < 4:
            flash('Email must be greater than 4 Charachters', category="error")
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character', category="error")
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character', category="error")
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category="error")
        elif password1 != password2:
            flash('Passwords do not match', category="error")
        else:
            # Add user to database
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('User added', category="success")
            return redirect(url_for('views.login'))

    data = request.form 
    print(data)
    return render_template("sign_up.html", user=current_user)