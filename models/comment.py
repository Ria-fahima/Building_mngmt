from init import db, ma
from marshmallow import fields

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    date = db.Column(db.Date) 

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    annoucement_id = db.Column(db.Integer, db.ForeignKey('annoucements.id'), nullable=False)

    user = db.relationship("User", back_populates="comments")
    annoucement = db.relationship("Annoucement", back_populates="comments")


class CommentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name', 'email'])
    annoucement = fields.Nested('AnnoucementSchema', exclude = ['user', 'comments'])

    class Meta:
        fields = ('id', 'message', 'date', 'annoucement', 'user')
        ordered = True