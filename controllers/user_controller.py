from flask import Blueprint,request
from init import db
from models.user import User, UserSchema
from models.resident import Resident, ResidentSchema
from models.staff import Staff, StaffSchema
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
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'user not found with id {id}'}, 404

@user_bp.route('/residents/')
@jwt_required()
def get_all_residents():

    stmt = db.select(Resident)
    residents = db.session.scalars(stmt)
    return ResidentSchema(many= True).dump(residents)


@user_bp.route('/residents/<int:id>/')
@jwt_required()
def get_one_resident(id):
    stmt = db.select(Resident).filter_by(id=id)
    resident = db.session.scalar(stmt)
    if resident:
        return ResidentSchema().dump(resident)
    else:
        return {'error': f'resident is not found with id {id}'}, 404



@user_bp.route('/residents/<int:id>/' , methods=['DELETE'])
@jwt_required()
def delete_one_resident(id):
    authorize()

    stmt = db.select(Resident).filter_by(id = id)
    resident = db.session.scalar(stmt)
    if resident:
        db.session.delete(resident)
        db.session.commit()
        return {'message' : f' {id} id is empty now'}
    else:
        return {'error' : f'Resident not found for id {id} '}




@user_bp.route('/residents/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_resident_info(id):
    authorize()

    stmt = db.select(Resident).filter_by(id=id)
    resident = db.session.scalar(stmt)
    if resident:
        resident.fob_num = request.json.get('fob_num') or resident.fob_num
        resident.car_num = request.json.get('car_num') or resident.car_num
        resident.unit = request.json.get('unit') or resident.unit
        resident.is_owner = request.json.get('is_owner') or resident.is_owner
        db.session.commit()
        return ResidentSchema().dump(resident)
    else:
        return {'error': f'Resident not found with id {id}'}, 404



@user_bp.route('/staffs/')
@jwt_required()
def get_all_staffs():

    stmt = db.select(Staff)
    staffs = db.session.scalars(stmt)
    return StaffSchema(many= True, exclude= ['annoucements']).dump(staffs)



@user_bp.route('/staffs/<int:id>/')
@jwt_required()
def get_one_staff(id):
    stmt = db.select(Staff).filter_by(id=id)
    staff = db.session.scalar(stmt)
    if staff:
        return StaffSchema(exclude= ['annoucements']).dump(staff)
    else:
        return {'error': f'staff is not found with id {id}'}, 404




@user_bp.route('/staffs/<int:id>/' , methods=['DELETE'])
@jwt_required()
def delete_one_staff(id):
    authorize()

    stmt = db.select(Staff).filter_by(id = id)
    staff = db.session.scalar(stmt)
    if staff:
        db.session.delete(staff)
        db.session.commit()
        return {'message' : f' {id} id is empty now'}
    else:
        return {'error' : f'staff not found for id {id} '}



@user_bp.route('/staffs/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_staff_info(id):
    authorize()

    stmt = db.select(Staff).filter_by(id=id)
    staff = db.session.scalar(stmt)
    if staff:
        staff.role = request.json.get('role') or staff.role
        staff.is_admin = request.json.get('is_admin') or staff.is_admin
        db.session.commit()
        return StaffSchema(exclude= ['annoucements']).dump(staff)
    else:
        return {'error': f'Staff not found with id {id}'}, 404
    