from init import db,ma
from marshmallow import fields

class Complain(db.Model):
    __tablename__ = 'complains'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    title = db.Column(db.String)
    message = db.Column(db.String, nullable=False)

    # code valid
    resident_id = db.Column(db.Integer, db.ForeignKey('residents.id'), nullable=False)

    resident = db.relationship('Resident', back_populates='complains')
    # code valid

class ComplainSchema(ma.Schema):
    resident = fields.Nested('ResidentSchema', exclude=['fob_num', 'car_num', 'complain'])

    class Meta:
        fields = ('id', 'date', 'unit','title', 'message', 'resident')
        ordered = True