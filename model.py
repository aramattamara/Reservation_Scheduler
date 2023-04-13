"""Models for reservation scheduler app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"

    @classmethod
    def create_user(cls, username: str):
        username = username.lower()
        # noinspection PyArgumentList
        user = cls(username=username)

        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter(cls.username == username).first()

    @classmethod
    def get_user(cls):
        return cls.query.all()


class Reservation(db.Model):
    __tablename__ = "reservations"
    __table_args__ = (db.UniqueConstraint('reservation_date', 'time_slot', name='uc_1'),
                      db.UniqueConstraint('user_id', 'reservation_date', name='uc_2'))

    reservation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    reservation_date = db.Column(db.DateTime(timezone=True))
    time_slot = db.Column(db.String(20), nullable=False)

    user = db.relationship("User", backref="reservations")

    def __repr__(self):
        return f"<Reservation reservation_id={self.reservation_id} user_id={self.user_id} start_time={self.reservation_date}>"

    @classmethod
    def new_reservation(cls, user_id, datetime_object, timeslot):
        """ Create and add a new reservation """
        # noinspection PyArgumentList
        reservation = cls(user_id=user_id, reservation_date=datetime_object, time_slot=timeslot)
        db.session.add(reservation)
        db.session.commit()
        return reservation

    @classmethod
    def get_reseravations(cls, user_id):
        """get all reservations for user"""
        return cls.query.filter(cls.user_id == user_id).all()


def connect_to_db(flask_app, db_uri="postgresql:///reservation", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    print('kuku')
    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
    print("Connected to the db!")
