from init import db,ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    fob_num = db.Column(db.Integer)
    car_num = db.Column(db.String)
    unit = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_owner = db.Column(db.Boolean, default=False)

    annoucements = db.relationship('Annoucement', back_populates='user', cascade='all, delete')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete')
    complains = db.relationship('Complain', back_populates='user', cascade='all, delete')

class UserSchema(ma.Schema):
    annoucements = fields.List(fields.Nested('AnnoucementSchema', exclude= ['user']))
    comments = fields.List(fields.Nested('CommentSchema', exclude= ['user']))

    class Meta:
        fields = ('id', 'f_name', 'l_name', 'email', 'fob_num','car_num','unit', 'password', 'is_admin', 'is_owner','annoucements')
        ordered = True
