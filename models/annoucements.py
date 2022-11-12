from init import db,ma
from marshmallow import fields

# Annoucement Model is created
class Annoucement(db.Model):
    __tablename__ = 'annoucements'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)


   # Foreign key for annoucement model 
    staff_id = db.Column(db.Integer, db.ForeignKey('staffs.id'), nullable=False)

   # Relationships with the Annoucement model
    staff = db.relationship('Staff', back_populates='annoucements')
    comments = db.relationship('Comment', back_populates='annoucement', cascade='all, delete')
    
# Annoucement Schema
class AnnoucementSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name','email'])
    comments = fields.List(fields.Nested('CommentSchema', exclude=['annoucement']))

    class Meta:
        fields = ('id', 'subject', 'message', 'date', 'user', 'comments')
        ordered = True