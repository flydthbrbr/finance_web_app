from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Note
from . import helpers
from . import db
import json


views = Blueprint('views', __name__)
    
@views.route('/',methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Great Success!', category='succes')
    return render_template("home.html", user=current_user)

@views.route('/stocks', methods=['GET','POST'])
@login_required
def stocks():
    stock = helpers.get_ticker_data('AAPL')
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        stock = helpers.get_ticker_data(ticker)
        data = request.form 
        print(data)
        print(stock.info)
        #return render_template("stocks.html", user=current_user, stock=stock, data=data)
    return render_template("stocks.html", user=current_user, stock=stock)

@views.route('/delete-note', methods=['POST']) 
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})


@views.route('/dashboard',methods=['GET', 'POST'])
@login_required
def user():
    
    return render_template("dashboard.html", user=current_user)
