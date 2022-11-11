from init import db,ma
from marshmallow import fields
from marshmallow.validate import Length
class Resident(db.Model):
    __tablename__ = 'residents'

    id = db.Column(db.Integer, primary_key=True)
    fob_num = db.Column(db.Integer)
    car_num = db.Column(db.String)
    unit = db.Column(db.Integer, nullable=False)
    is_owner = db.Column(db.Boolean, default=False)


    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staffs.id'), nullable=False)
    
    user = db.relationship('User', back_populates='resident', cascade='all, delete')
    staff = db.relationship('Staff', back_populates='residents')
    

class ResidentSchema(ma.Schema):
    
    user = fields.Nested('UserSchema', only = ['f_name', 'l_name'])
    unit = fields.String(required= True, validate= Length(min=3, error = "Each Unit field has 3 characters"))

    class Meta:
        
        fields = ('id', 'fob_num','car_num','unit', 'is_owner', 'user')
        ordered = True
