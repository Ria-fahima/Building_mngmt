from flask import Blueprint,request
from init import db
from models.user import User, UserSchema
from models.resident import Resident, ResidentSchema
from models.staff import Staff, StaffSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import authorize

user_bp = Blueprint('users', __name__, url_prefix='/users')

# To get all the users
@user_bp.route('/')
@jwt_required()
def get_all_users():

    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many = True, exclude=['password']).dump(users)

# To get a certain user with the user id
@user_bp.route('/<int:id>/')
@jwt_required()
def get_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'user not found with id {id}'}, 404

# To get all residents list
@user_bp.route('/residents/')
@jwt_required()
def get_all_residents():

    stmt = db.select(Resident)
    residents = db.session.scalars(stmt)
    return ResidentSchema(many= True).dump(residents)

# To get only one resident at a time with resident id
@user_bp.route('/residents/<int:id>/')
@jwt_required()
def get_one_resident(id):
    stmt = db.select(Resident).filter_by(id=id)
    resident = db.session.scalar(stmt)
    if resident:
        return ResidentSchema().dump(resident)
    else:
        return {'error': f'resident is not found with id {id}'}, 404

# To add a user to the resident list by providing user_id
@user_bp.route('/residents/<int:id>',methods=['POST'])
@jwt_required()
def add_one_resident(id):
    authorize()

    data = ResidentSchema().load(request.json)
    resident = Resident(
        fob_num = data['fob_num'],
        unit = data['unit'],
        car_num = data['car_num'], 
        is_owner = data['is_owner'],
        user_id = id,
        staff_id = get_jwt_identity()
        
    )
    db.session.add(resident)
    db.session.commit()
    return ResidentSchema().dump(resident), 201

# To delete a resident from the residents list by providing the resident id
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



# To update any information of the existing resident list with resident id
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


# To get all the staffs
@user_bp.route('/staffs/')
@jwt_required()
def get_all_staffs():

    stmt = db.select(Staff)
    staffs = db.session.scalars(stmt)
    return StaffSchema(many= True, exclude= ['annoucements']).dump(staffs)


# to get a staff info with certain staff id
@user_bp.route('/staffs/<int:id>/')
@jwt_required()
def get_one_staff(id):
    stmt = db.select(Staff).filter_by(id=id)
    staff = db.session.scalar(stmt)
    if staff:
        return StaffSchema(exclude= ['annoucements']).dump(staff)
    else:
        return {'error': f'staff is not found with id {id}'}, 404

# to add a user to the staff list by providing the user id
@user_bp.route('/staffs/<int:id>',methods=['POST'])
@jwt_required()
def add_one_staff(id):
    authorize()
    
    data = StaffSchema().load(request.json)
    staff = Staff(
        role = data['role'],
        is_admin = data['is_admin'],
        user_id = id
        
    )
    db.session.add(staff)
    db.session.commit()
    return StaffSchema().dump(staff), 201

# To delete a staff info by providing staff_id
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


# To change a staff information by providing certain id
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
    