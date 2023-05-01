from twitter.src import create_app
from twitter.src.models import db,Band, Concert, Venue, User, Ticket, bands_concerts_table, concerts_venues_table

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create bands
    radiohead = Band(name='Radiohead')
    pink_floyd = Band(name='Pink Floyd')
    arcade_fire = Band(name='Arcade Fire')
    db.session.add_all([radiohead, pink_floyd, arcade_fire])
    db.session.commit()

    # Create concerts
    msg = Concert(date='2023-05-01')
    animals = Concert(date='2023-06-01')
    reflektor = Concert(date='2023-07-01')
    db.session.add_all([msg, animals, reflektor])
    db.session.commit()

    # Create venues
    msg_venue = Venue(name='Madison Square Garden', city='New York', state='NY')
    animals_venue = Venue(name='Staples Center', city='Los Angeles', state='CA')
    reflektor_venue = Venue(name='The O2', city='London', state='UK')
    db.session.add_all([msg_venue, animals_venue, reflektor_venue])
    db.session.commit()

    # Associate concerts with venues
    db.session.execute(concerts_venues_table.insert().values([
        {'concert_id': msg.id, 'venue_id': msg_venue.id},
        {'concert_id': animals.id, 'venue_id': animals_venue.id},
        {'concert_id': reflektor.id, 'venue_id': reflektor_venue.id},
    ]))
    db.session.commit()

    # Associate bands with concerts
    db.session.execute(bands_concerts_table.insert().values([
        {'band_id': radiohead.id, 'concert_id': msg.id},
        {'band_id': pink_floyd.id, 'concert_id': animals.id},
        {'band_id': arcade_fire.id, 'concert_id': reflektor.id},
    ]))
    db.session.commit()

    # Create users and tickets
    user1 = User(first_name='John', last_name='Doe')
    user2 = User(first_name='Jane', last_name='Smith')
    db.session.add_all([user1, user2])
    db.session.commit()

    ticket1 = Ticket(user_id=user1.id, concert_id=msg.id, tickets_purchased=2)
    ticket2 = Ticket(user_id=user2.id, concert_id=animals.id, tickets_purchased=1)
    ticket3 = Ticket(user_id=user2.id, concert_id=reflektor.id, tickets_purchased=4)
    db.session.add_all([ticket1, ticket2, ticket3])
    db.session.commit()
