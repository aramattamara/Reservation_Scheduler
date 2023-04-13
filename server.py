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
    
    user = User.get_user_by_username(username)

    if user:
        session["username"] = username
        # flash(f"Welcome to the MelonWell, {username}!")
        return redirect(url_for('make_reservation'))
    else:
        flash("The username you have entered does not exist.")

    return redirect("/")


@app.route("/logout")
def logout():
    session["username"] = None
    flash("You have been logged out. Please Log In.")
    return redirect("/")



@app.route("/reservations/create", methods=["GET", "POST"])
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
