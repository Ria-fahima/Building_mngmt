from flask import Blueprint,request
from init import db
from datetime import date
from models.user import User
from models.complain import Complain, ComplainSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import authorize

complain_bp = Blueprint('complains', __name__, url_prefix='/complains')

@complain_bp.route('/')
@jwt_required()
def get_all_complains():

    stmt = db.select(Complain).order_by(Complain.date.desc())
    complains = db.session.scalars(stmt)
    return ComplainSchema(many = True).dump(complains)


@complain_bp.route('/<int:id>/')
@jwt_required()
def get_one_complain(id):
    stmt = db.select(Complain).filter_by(id=id)
    complain = db.session.scalar(stmt)
    if complain:
        return ComplainSchema().dump(complain)
    else:
        return {'error': f'No complain is found with {id}'}, 404



@complain_bp.route('/',methods=['POST'])
@jwt_required()
def create_one_complain():

    data = ComplainSchema().load(request.json)
    complain = Complain(
        date = date.today(),
        unit = data['unit'],
        title = data['title'], 
        message = data['message'],
        user_id = get_jwt_identity()
        
    )
    db.session.add(complain)
    db.session.commit()
    return ComplainSchema().dump(complain), 201



@complain_bp.route('/<int:id>/' , methods=['DELETE'])
@jwt_required()
def delete_one_complain(id):

    stmt = db.select(Complain).filter_by(id = id)
    complain = db.session.scalar(stmt)
    if complain:
        db.session.delete(complain)
        db.session.commit()
        return {'message' : f'Complain from Unit {id} is deleted successfully'}
    else:
        return {'error' : f'No complain is found with id {id} '}


@complain_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_complain(id):

    stmt = db.select(Complain).filter_by(id = id)
    complain = db.session.scalar(stmt)
    if complain:
        complain.date = request.json.get('date') or complain.date
        complain.title = request.json.get('title') or complain.title
        complain.message = request.json.get('message') or complain.message
        complain.unit = request.json.get('unit') or complain.unit
        db.session.commit()
        return ComplainSchema().dump(complain)
    else:
        return {'error': f'No Complain is found from Unit {id}'}, 404