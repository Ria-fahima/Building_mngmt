from init import db,ma
from marshmallow import fields

class Complain(db.Model):
    __tablename__ = 'complains'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    title = db.Column(db.String)
    message = db.Column(db.String, nullable=False)
    unit = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='complains')

class ComplainSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name','email'])

    class Meta:
        fields = ('id', 'date', 'unit','title', 'message', 'user')
        ordered = True