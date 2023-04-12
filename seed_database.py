"""Script to seed database"""
import os
import json

import model 
import server

os.system("dropdb ratings")
os.system("createdb ratings")

with server.app.app_context():
    model.connect_to_db(server.app)
    model.db.create_all()

# with open ('user.json') as f:
#     user_data = json.loads(f.read())

    model.db.session.commit()