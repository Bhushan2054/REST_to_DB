from flask import jsonify,request
import json
from myapp import db, app
from myapp.models import User, UsersSchema, Photos, PhotosSchema, Albums, AlbumsSchema, Comments, CommentsSchema, Posts, PostsSchema, Todos, TodosSchema



@app.route('/users')
def user():
    users = User.query.all()
    users_details = UsersSchema(many=True)
    output_details = users_details.dump(users).data
    return jsonify(output_details)


@app.route('/posts')
def post():
    posts = Posts.query.all()
    postss_details = PostsSchema(many=True)
    output_details = postss_details.dump(posts).data
    return jsonify(output_details)


@app.route('/users', methods=['POST'])
def posts():
    post = User.query.all()
    postss_details = UsersSchema(many=True)
    output_details = postss_details.dump(post).data
    new_id = request.json['id']
    new_name = request.json['name']
    new_username = request.json['username']
    new_email = request.json['email']
    new_address = request.json['address']
    new_phone = request.json['phone']
    new_website = request.json['website']
    new_company = request.json['company']
    add_json_data = {'id': new_id, 'name': new_name,
                     'username': new_username, 'email': new_email, 'address': new_address, 'phone': new_phone, 'website': new_website, 'company': new_company}
    output_details.append(add_json_data)
    return jsonify(output_details)

