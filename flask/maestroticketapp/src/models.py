from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Band(db.Model):
    __tablename__ = 'bands'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

bands_concerts_table = db.Table(
    'bands_concerts',
    db.Column(
        'band_id', db.Integer,
        db.ForeignKey('bands.id'),
        primary_key=True
    ),

    db.Column(
        'concert_id', db.Integer,
        db.ForeignKey('concerts.id'),
        primary_key=True
    ),

)




class Concert(db.Model):
    __tablename__ = 'concerts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
        }

concerts_venues_table = db.Table(
    'concerts_venues',
    db.Column(
        'concert_id', db.Integer,
        db.ForeignKey('concerts.id'),
        primary_key=True
    ),

    db.Column(
        'venue_id', db.Integer,
        db.ForeignKey('venues.id'),
        primary_key=True
    ),

)

class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    city = db.Column(db.String(128), unique=False, nullable=False)
    state = db.Column(db.String(128), unique=False, nullable=False)

class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    concert_id = db.Column(db.Integer, db.ForeignKey('concerts.id'))
    tickets_purchased = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id: int, concert_id: int, tickets_purchased: int):
        self.user_id = user_id
        self.concert_id = concert_id
        self.tickets_purchased = tickets_purchased

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'concert_id': self.concert_id,
            'tickets_purchased': self.tickets_purchased
        }



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), unique=False, nullable=False)
    last_name = db.Column(db.String(128), unique=False, nullable=False)
    tickets = db.relationship('Ticket', backref='user', lazy=True, cascade="all,delete")



