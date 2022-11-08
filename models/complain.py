from init import db,ma


class Complain(db.Model):
    __tablename__ = 'complains'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    title = db.Column(db.String)
    message = db.Column(db.String, nullable=False)
    unit = db.Column(db.Integer, nullable=False)

class ComplainSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'unit','title', 'message')
        ordered = True