from app import db
from datetime import datetime

class Paciente(db.Model) :
      #definir los atributos 
    __tablename__="pacientes"
    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(128), nullable = True)
    email = db.Column(db.String(128), nullable = True) 

    citas = db.relationship('Cita', 
                             backref = "paciente", 
                             )

class Medico(db.Model) :
      #definir los atributos 
    __tablename__="medicos"
    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(128), nullable = True)
    email = db.Column(db.String(128), nullable = True)
    speciality = db.Column(db.String(128), nullable = True)

    citas = db.relationship('Cita', 
                             backref = "medico", 
                             )

class Consultorio(db.Model):
    __tablename__="consultorios"
    id = db.Column(db.Integer, primary_key = True )
    numero = db.Column(db.Integer)

    citas = db.relationship('Cita', 
                             backref = "consultorio", 
                             )

    

class Cita(db.Model):
    __tablename__="citas"
    id = db.Column(db.Integer, primary_key = True )
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id')) 
    consultorio_id = db.Column(db.Integer, db.ForeignKey('consultorios.id')) 
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id')) 
    



