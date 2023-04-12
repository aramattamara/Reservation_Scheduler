from flask import Flask, jsonify, render_template, request, flash, session, redirect, url_for
from jinja2 import StrictUndefined
from model import connect_to_db, Reservation, User,  db
import crud
import sqlalchemy
import os

app = Flask(__name__)

app.secret_key = "dev"
connect_to_db(app)
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/login")
def login():
    username = request.form.get("username")



@app.route("/reservations")
def all_reservations_by_user():
    return crud.get_reservation_by_username
    

@app.route("/create_reservation", methods=["POST"])
def save_reservation():
    username=request.form.get("username")
    datetime_str = request.form['datetime']
    datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
    new_reservation = Reservation(username=username, start_time = datetime_obj)
    db.session.add(new_reservation)
    db.session.commit()
    return True

    



    


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
