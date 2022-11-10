from flask import Blueprint,request
from init import db
from models.user import User, UserSchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorize

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/')
@jwt_required()
def get_all_users():

    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many = True, exclude=['password']).dump(users)


@user_bp.route('/<int:id>/')
@jwt_required()
def get_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(many =True,exclude=['password']).dump(user)
    else:
        return {'error': f'user not found with unit {id}'}, 404



@user_bp.route('/<int:id>/' , methods=['DELETE'])
@jwt_required()
def delete_one_user(id):
    authorize()

    stmt = db.select(User).filter_by(id = id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message' : f' {user.unit} unit is empty now'}
    else:
        return {'error' : f'User not found for id {id} '}




@user_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_user_info(id):
    authorize()

    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        user.f_name = request.json.get('f_name') or user.f_name
        user.l_name = request.json.get('l_name') or user.l_name
        user.email = request.json.get('email') or user.email
        user.fob_num = request.json.get('fob_num') or user.fob_num
        user.car_num = request.json.get('car_num') or user.car_num
        db.session.commit()
        return UserSchema(many= True,exclude=['password']).dump(user)
    else:
        return {'error': f'User not found with id {id}'}, 404