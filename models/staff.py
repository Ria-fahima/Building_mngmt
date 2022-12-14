from init import db,ma
from marshmallow import fields
from marshmallow.validate import Length

#Staff Model is created
class Staff(db.Model):
    __tablename__ = 'staffs'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)

#Foreign key in the staff model
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

# Relationships with the Staff Model
    user = db.relationship('User', back_populates='staff', cascade='all, delete')
    annoucements = db.relationship('Annoucement', back_populates='staff', cascade='all, delete')
    residents = db.relationship('Resident', back_populates='staff')
    
# Staff Schema is created
class StaffSchema(ma.Schema):
    annoucements = fields.List(fields.Nested('AnnoucementSchema', exclude= ['staff']))
    role = fields.String(required= True, validate= Length(min=4, error = "Role should be at least 4 characters"))

    class Meta:
        fields = ('id', 'role', 'is_admin', 'annoucements')
        ordered = True
