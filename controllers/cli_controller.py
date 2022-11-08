from flask import Blueprint
from models.user import User
from models.annoucements import Annoucement
from datetime import date
from init import db,bcrypt


db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User( 
            f_name = 'Mickel',
            l_name = 'Rowston',
            email = 'admin@gmail.com',
            fob_num = '3465',
            car_num = 'WRT-466',
            password = bcrypt.generate_password_hash('eggs').decode('utf-8'),
            is_admin = True
        ),
        User(
            f_name = 'Ron',
            l_name = 'Sharma',
            email = 'ron35@gmail.com',
            fob_num = '3186',
            car_num = 'AZW-BRB',
            password = bcrypt.generate_password_hash('ronty').decode('utf-8'),
        )
    ]

    db.session.add_all(users)
    db.session.commit()


    annoucements = [
        Annoucement(
            subject = 'Christmas Dinner',
            message = 'Buffet Dinner at 5pm in the Royal Lounge. We will love to have you in our party.',
            date = date.today()
        ),
        Annoucement(
            subject = 'Annual Meeting',
            message = 'Meeting will start at 7pm. Everyone needs to be there for further development discussion in the building.',
            date = date.today()
        ),
        Annoucement(
            subject = 'Fire Detector Check',
            message = 'Please book your time for the fire detector check in your apartment. The concierge will help you for the booking.',
            date = date.today()
        )
    ]

    db.session.add_all(annoucements)
    db.session.commit()

    print('Tables seeded')