from flask import Blueprint
from init import db
from models.annoucements import Annoucement, AnnoucementSchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorize



annoucement_bp = Blueprint('annoucements', __name__, url_prefix='/annoucements')

@annoucement_bp.route('/')
@jwt_required()
def get_all_annoucements():

    stmt = db.select(Annoucement).order_by(Annoucement.date.desc())
    annoucements = db.session.scalars(stmt)
    return AnnoucementSchema(many = True).dump(annoucements)


@annoucement_bp.route('/<int:id>/')
@jwt_required()
def get_one_annoucement(id):
    stmt = db.select(Annoucement).filter_by(id=id)
    annoucement = db.session.scalar(stmt)
    if annoucement:
        return AnnoucementSchema().dump(annoucement)
    else:
        return {'error': f'card not found with id {id}'}, 404



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