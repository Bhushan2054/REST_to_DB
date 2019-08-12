from flask import jsonify
import json
from RESTAPI import db,app
from RESTAPI.models import User,UsersSchema

@app.route('/')
def index():
    users = User.query.all()
    users_details = UsersSchema(many=True)
    output_details = users_details.dump(users).data
    return jsonify(output_details)

