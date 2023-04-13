"""Models for reservation scheduler app."""
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
          return f"<User id={self.id} username={self.username}>"
    
    @classmethod
    def create_user(cls, username):
         username = username.lower()
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

     reservation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
     reservation_date = db.Column(db.DateTime(timezone=True))
     time_slot = db.Column(db.String(20), nullable=False)

     user = db.relationship("User", backref="reservations")

     def __repr__(self):
          return f"<Reservation reservation_id={self.reservation_id} username={self.username} start_time={self.start_time}>"
     

     @classmethod
     def new_reservation(cls, user_id, datetime_object, timeslot):
        """ Create and add a new reservation """

        reservation = cls(user_id=user_id, reservation_date=datetime_object, time_slot=timeslot)

        db.session.add(reservation)
        db.session.commit()
        return reservation

    



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