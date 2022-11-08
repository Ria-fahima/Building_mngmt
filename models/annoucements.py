from init import db,ma


class Annoucement(db.Model):
    __tablename__ = 'annoucements'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text)
    date = db.Column(db.Date)
    
class AnnoucementSchema(ma.Schema):
    class Meta:
        fields = ('id', 'subject', 'message', 'date')
        ordered = True