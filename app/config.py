class Config:
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:admin@localhost:3310/flask_shopy'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = 'hola'