"""CRUD operations."""

from model import db, Reservation, connect_to_db

def create_reservation(username, start_time):
    """Create and return reservation"""
    reservation = Reservation(username=username, start_time=start_time)

    return reservation

def get_reservation():
    return Reservation.query.all()

def get_reservation_by_username(username):
    """return all reservation for this user"""
    return Reservation.query.filter(username=username).all()

