from flask_marshmallow import Marshmallow
from myapp import db, ma


class User(db.Model):
    # __tablename__ = 'user_details'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    website = db.Column(db.String(200))
    company = db.Column(db.String(200))

class UsersSchema(ma.ModelSchema):
    class Meta:
        model = User


class Posts(db.Model):
    __tablename__ = 'posts'
    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    body = db.Column(db.String(5000))

class PostsSchema(ma.ModelSchema):
    class Meta:
        model = Posts

class Comments(db.Model):
    __tablename__ = 'comments'
    postId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    email = db.Column(db.String(100))
    body = db.Column(db.String(5000))

class CommentsSchema(ma.ModelSchema):
    class Meta:
        model = Comments

class Albums(db.Model):
    __tablename__ = 'albums'
    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))

class AlbumsSchema(ma.ModelSchema):
    class Meta:
        model = Albums


class Photos(db.Model):
    __tablename__ = 'photos'
    albumId  = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    url = db.Column(db.String(300))
    thumbnailUrl = db.Column(db.String(300))

class PhotosSchema(ma.ModelSchema):
    class Meta:
        model = Photos
   
        
class Todos(db.Model):
    __tablename__ = 'todos'
    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    completed = db.Column(db.String(10))

class TodosSchema(ma.ModelSchema):
    class Meta:
        model = Todos
       

db.create_all()
from myapp import __init__
