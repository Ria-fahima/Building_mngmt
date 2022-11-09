from flask import Blueprint
from models.user import User
from models.complain import Complain
from models.annoucements import Annoucement
from models.comment import Comment
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
            fob_num = 3465,
            car_num = 'WRT-466',
            password = bcrypt.generate_password_hash('eggs').decode('utf-8'),
            is_admin = True,
            unit = 100
        ),
        User(
            f_name = 'Ron',
            l_name = 'Sharma',
            email = 'ron35@gmail.com',
            fob_num = 3186,
            car_num = 'AZW-BRB',
            unit = 304,
            password = bcrypt.generate_password_hash('ronty').decode('utf-8'),
            is_owner = True
        )
    ]

    db.session.add_all(users)
    db.session.commit()


    annoucements = [
        Annoucement(
            subject = 'Christmas Dinner',
            message = 'Buffet Dinner at 5pm in the Royal Lounge. We will love to have you in our party.',
            user = users[0],
            date = date.today()
        ),
        Annoucement(
            subject = 'Annual Meeting',
            message = 'Meeting will start at 7pm. Everyone needs to be there for further development discussion in the building.',
            user = users[1],
            date = date.today()
        ),
        Annoucement(
            subject = 'Fire Detector Check',
            message = 'Please book your time for the fire detector check in your apartment. The concierge will help you for the booking.',
            user = users[0],
            date = date.today()
        )
    ]

    db.session.add_all(annoucements)
    db.session.commit()

    comments = [
        Comment(
            message = 'Comment 1',
            user = users[0],
            annoucement = annoucements[0],
            date = date.today()
        ),
        Comment(
            message = 'Comment 2',
            user = users[0],
            annoucement = annoucements[1],
            date = date.today()
        ),
        Comment(
            message = 'Comment 3',
            user = users[1],
            annoucement = annoucements[1],
            date = date.today()
        )
    ]

    db.session.add_all(comments)
    db.session.commit()

    complains = [
        Complain(
            date = date.today(),
            unit = 304,
            user = users[0],
            title = 'Water hose pipe defect',
            message = 'Unit 504 bathroom water pipe is defected. Need to repair it urgently.'
        ),
        Complain(
            date = date.today(),
            unit = 402,
            user = users[1],
            title = 'noise from unit 603',
            message = 'Loud noise is coming from unit 603 after midnight.'
        )
    ]

    db.session.add_all(complains)
    db.session.commit()

    print('Tables seeded')