from flask import Flask, jsonify, render_template, request, flash, session, redirect, url_for
from jinja2 import StrictUndefined
from model import connect_to_db, Reservation, User, db
import sqlalchemy
import os
from datetime import datetime

app = Flask(__name__)

app.secret_key = "dev"
connect_to_db(app)
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    username = request.form.get("username")
    user = User.get_user_by_username(username)

    if user:
        session["username"] = username
        flash(f"Welcome to the MelonWell, {username}!")
        return redirect(url_for('make_reservation'))
    else:
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        session['username'] = username
        return redirect(url_for('make_reservation'))

    return redirect("/")


@app.route("/logout")
def logout():
    """ Delete user from the session """

    session["username"] = None
    flash("You have been logged out. Please Log In.")
    return redirect("/")


@app.route("/reservations/create", methods=["GET", "POST"])
def make_reservation():
    if "username" not in session:
        flash("You have been logged out. Please log in")
        return redirect("/")

    timeslots = ['9:00-9:30', '9:30-10:00',
                 '10:00-10:30', '10:30-11:00',
                 '11:00-11:30', '11:30-12:00',
                 '12:00-12:30', '12:30-13:00',
                 '1:00-1:30', '1:30-2:00',
                 '2:00-2:30', '2:30-3:00',
                 '3:00-3:30', '3:30-4:00',
                 '4:00-4:30', '4:30-5:00',
                 ]

    username = session["username"]
    user = User.get_user_by_username(username)

    if request.method == "POST":
        reservation_date = request.form.get("date")
        timeslot = request.form.get("timeslot")
        booked_timeslots = set(Reservation.get_timeslots_for_date(reservation_date))

        if not timeslot:
            flash("Please select time slot")
            return render_template(
                "make_reservation.html",
                username=session["username"],
                timeslots=timeslots,
                booked_timeslots=booked_timeslots,
            )

        try:
            Reservation.new_reservation(user.id, reservation_date, timeslot)
        except sqlalchemy.exc.IntegrityError:
            flash("You can choose one testing per day.")
            return render_template(
                "make_reservation.html",
                username=session["username"],
                timeslots=timeslots,
                booked_timeslots=booked_timeslots
            )

        flash("Reservation successfully added!")
        return redirect(url_for('show_reservations'))

    else:
        reservation_date = datetime.strftime(datetime.utcnow(), "%Y/%m/%d")
        booked_timeslots = set(Reservation.get_timeslots_for_date(reservation_date))
        return render_template(
            "make_reservation.html",
            username=session["username"],
            timeslots=timeslots,
            booked_timeslots=booked_timeslots,
        )


@app.route("/reservations", methods=["GET"])
def show_reservations():
    if "username" not in session:
        flash("You have been logged out. Please log in")
        return redirect("/")

    username = session['username']
    user = User.get_user_by_username(username)

    all_reservations = Reservation.get_reseravations(user.id)
    return render_template('reservation.html', username=username, all_reservations=all_reservations)


@app.route("/reservations/delete/<id>", methods=['DELETE'])
def delete_reservation(id):
    if "username" not in session:
        return jsonify({ 'success': False }), 500

    try:
        Reservation.delete_reservation(id)
        return jsonify({ 'success': True })

    except AttributeError as e:
        return jsonify({ 'success': False }), 500


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
