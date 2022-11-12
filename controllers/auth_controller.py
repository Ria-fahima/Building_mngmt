from flask import Blueprint,request,abort
from datetime import timedelta
from init import db,bcrypt,jwt
from models.user import User, UserSchema
from models.staff import Staff
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Register new user with certain information to User Model
@auth_bp.route('/register/',methods=['POST'])
def auth_register():
    try:
        
        data = UserSchema().load(request.json)
        #Load the posted user info 
        user = User(
            f_name = data['f_name'],
            l_name = data['l_name'],
            email = data['email'],
            # unit = request.json['unit'],
            password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude = ['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409

# Login as a user with some information by using User Model
@auth_bp.route('/login/',methods=['POST'])
def auth_login():
    stmt = db.select(User).filter_by(email = request.json['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity=str(user.id), expires_delta = timedelta(days=1))
        return {'email': user.email, 'token': token}
    else:
        return {'error': 'Invalid email or password'},401


# authorization in the Staff Model
def authorize():
    user_id = get_jwt_identity()
    stmt = db.select(Staff).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)

    
