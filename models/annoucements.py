from init import db,ma
from marshmallow import fields


class Annoucement(db.Model):
    __tablename__ = 'annoucements'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)


    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staffs.id'), nullable=False)

    # user = db.relationship('User', back_populates='annoucements')
    staff = db.relationship('Staff', back_populates='annoucements')
    comments = db.relationship('Comment', back_populates='annoucement', cascade='all, delete')

class AnnoucementSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name','email'])
    comments = fields.List(fields.Nested('CommentSchema', exclude=['annoucement']))

    class Meta:
        fields = ('id', 'subject', 'message', 'date', 'user', 'comments')
        ordered = True