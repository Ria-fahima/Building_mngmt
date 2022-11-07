from init import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    fob_num = db.Column(db.Integer)
    car_num = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
