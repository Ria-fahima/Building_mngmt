from init import db,ma
from marshmallow import fields

class Resident(db.Model):
    __tablename__ = 'residents'

    id = db.Column(db.Integer, primary_key=True)
    fob_num = db.Column(db.Integer)
    car_num = db.Column(db.String)
    unit = db.Column(db.Integer, nullable=False)
    is_owner = db.Column(db.Boolean, default=False)


    # code valid
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staffs.id'), nullable=False)
    
    user = db.relationship('User', back_populates='resident', cascade='all, delete')
    staff = db.relationship('Staff', back_populates='residents')
    complains = db.relationship('Complain', back_populates='resident', cascade='all, delete')
    # code valid

class ResidentSchema(ma.Schema):
    complain = fields.List(fields.Nested('ComplainSchema', exclude= ['resident']))
    user = fields.Nested('UserSchema', only = ['f_name', 'l_name'])

    class Meta:
        fields = ('id', 'fob_num','car_num','unit', 'is_owner', 'user','complain')
        ordered = True
