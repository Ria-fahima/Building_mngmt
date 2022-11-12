from init import db,ma
from marshmallow import fields,validates
from marshmallow.validate import Length, Regexp

# User Model created
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    

# RElationship with the User MODEL 
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete')
    resident = db.relationship('Resident', back_populates='user', cascade='all, delete')
    staff = db.relationship('Staff', back_populates='user', cascade='all, delete')
    complains = db.relationship('Complain', back_populates='user', cascade='all, delete')
   
# USER Schema is created
class UserSchema(ma.Schema):
    complains = fields.List(fields.Nested('ComplainSchema', exclude= ['user']))
    
    comments = fields.List(fields.Nested('CommentSchema', exclude= ['user']))
    f_name = fields.String(required= True, validate= Length(min=2, error = "First name should be at least 2 characters"))
    l_name = fields.String(required= True, validate= Length(min=2, error = "Last name should be at least 2 characters"))
    email = fields.String(required= True, validate= Length(min=2, error= "Email should be at least 2 characters"))
    password = fields.String(required=True, validate= Regexp('^.*(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[@?#$%^&+=]).*$', error = 'Password must be at least 8 characters, one lowercase letter(a-z), one uppercase letter(A-Z) and one special characters(@?#$%^&+=)'))

# validate email address
    @validates('email')
    def validate_email(self, value):
        if '@' not in value:
            raise ValueError("Inappropriate email address")


    class Meta:
        
        fields = ('id', 'f_name', 'l_name', 'email','password','comments', 'complains')
        ordered = True
