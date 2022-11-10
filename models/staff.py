from init import db,ma
from marshmallow import fields

class Staff(db.Model):
    __tablename__ = 'staffs'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    user = db.relationship('User', back_populates='staff', cascade='all, delete')
    annoucements = db.relationship('Annoucement', back_populates='staff', cascade='all, delete')
    residents = db.relationship('Resident', back_populates='staff')
    

class StaffSchema(ma.Schema):
    annoucements = fields.List(fields.Nested('AnnoucementSchema', exclude= ['staff']))

    class Meta:
        fields = ('id', 'role', 'is_admin', 'annoucements')
        ordered = True
