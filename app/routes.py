from . import app, db
from flask import render_template, request,redirect, url_for, flash
from .models import Medico

@app.route('/medicos')
def all_medicos():
    p = Medico.query.all()
    return render_template('medicos.html', medicos=p)


@app.route('/medicos/<int:id>')
def get_medico(id):
    p = Medico.query.get(id)
    return render_template('medico.html', medico=p)

@app.route('/medicos/create', methods=['GET' , 'POST'])
def create_medico():
    if request.method == 'GET':
        specialities = [
            "Cardiologia", 
            "Ortodoncia"
        ]
        return render_template('medico_form.html', specialities=specialities) 
    elif request.method == 'POST':
        m = Medico(username = request.form[ 'username'], 
                   password = request.form[ 'password'], 
                   email = request.form[ 'email'] ,
                   speciality = request.form[ 'spec' ] 
                   )
        db.session.add(m)
        db.session.commit()
        #return "Medico created successfully created"
        flash('You were successfully logged in')
        return redirect('/medicos')
 