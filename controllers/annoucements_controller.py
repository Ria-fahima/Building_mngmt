from flask import Blueprint,request
from init import db
from datetime import date
from models.annoucements import Annoucement, AnnoucementSchema
from models.comment import Comment, CommentSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import authorize



annoucement_bp = Blueprint('annoucements', __name__, url_prefix='/annoucements')

# To get all annoucements
@annoucement_bp.route('/')
@jwt_required()
def get_all_annoucements():

    stmt = db.select(Annoucement).order_by(Annoucement.date.desc())
    annoucements = db.session.scalars(stmt)
    return AnnoucementSchema(many= True).dump(annoucements)

# To get a certain annoucement with an annoucement id
@annoucement_bp.route('/<int:id>/')
@jwt_required()
def get_one_annoucement(id):
    stmt = db.select(Annoucement).filter_by(id=id)
    annoucement = db.session.scalar(stmt)
    if annoucement:
        return AnnoucementSchema().dump(annoucement)
    else:
        return {'error': f'annoucement not found with id {id}'}, 404

# add a new annoucement
@annoucement_bp.route('/',methods=['POST'])
@jwt_required()
def create_one_annoucement():
    authorize()

    data = AnnoucementSchema().load(request.json)
    annoucement = Annoucement(
        subject = data['subject'], 
        message = data['message'],
        date = date.today(),
        staff_id = get_jwt_identity()
    )
    db.session.add(annoucement)
    db.session.commit()
    return AnnoucementSchema().dump(annoucement), 201

# delete a Annoucement with id
@annoucement_bp.route('/<int:id>/' , methods=['DELETE'])
@jwt_required()
def delete_one_annoucement(id):
    authorize()

    stmt = db.select(Annoucement).filter_by(id = id)
    annoucement = db.session.scalar(stmt)
    if annoucement:
        db.session.delete(annoucement)
        db.session.commit()
        return {'message' : f'Annoucement on {annoucement.subject} topic is deleted successfully'}
    else:
        return {'error' : f'Annoucement is not found for id {id} '}

# update any information of the annoucement with id
@annoucement_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_annoucement(id):
    authorize()

    stmt = db.select(Annoucement).filter_by(id=id)
    annoucement = db.session.scalar(stmt)
    if annoucement:
        annoucement.subject = request.json.get('subject') or annoucement.subject
        annoucement.message = request.json.get('message') or annoucement.message
        annoucement.date = request.json.get('date') or annoucement.date
        db.session.commit()
        return AnnoucementSchema().dump(annoucement)
    else:
        return {'error': f'Annoucement is not found with id {id}'}, 404


# Create a new comment in the existing annoucements with certain announcement id
@annoucement_bp.route('/<int:id>/comments',methods=['POST'])
@jwt_required()
def create_comment(id):
    stmt = db.select(Annoucement).filter_by(id=id)
    annoucement = db.session.scalar(stmt)
    if annoucement:
        comment = Comment(
            message = request.json['message'],
            user_id = get_jwt_identity(),
            annoucement = annoucement,
            date = date.today()
        )
        db.session.add(comment)
        db.session.commit()
        return CommentSchema().dump(comment), 201
    else:
        return {'error': f'annoucement not found with id {id}'}, 404
    