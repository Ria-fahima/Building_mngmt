from init import db,ma
from marshmallow import fields
from marshmallow.validate import Length

#Complain Model is created
class Complain(db.Model):
    __tablename__ = 'complains'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    unit = db.Column(db.Integer)
    title = db.Column(db.String)
    message = db.Column(db.String, nullable=False)

# Foreign key(user_id) for Complain model is created
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    

#  Relationship with the Complain Model
    user = db.relationship('User', back_populates='complains')

# Complain Schema is created
class ComplainSchema(ma.Schema):
    
    message = fields.String(required= True, validate= Length(min=8, error = "Message should be well explained."))
    user = fields.Nested('UserSchema', only=['f_name', 'l_name','email'])

    class Meta:
        fields = ('id', 'date', 'unit','title', 'message',  'user')
        ordered = True