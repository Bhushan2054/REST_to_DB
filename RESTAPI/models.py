from RESTAPI import db

class User(db.Model):
    __tablename__ = 'user_details'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    website = db.Column(db.String(200))
    company = db.Column(db.String(200))

class Posts(db.Model):
    __tablename__ = 'posts'
    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    body = db.Column(db.String(5000))

class Comments(db.Model):
    __tablename__ = 'comments'
    postId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    email = db.Column(db.String(100))
    body = db.Column(db.String(5000))

class Albums(db.Model):
    __tablename__ = 'albums'
    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))

class Photos(db.Model):
    __tablename__ = 'photos'
    albumId  = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    url = db.Column(db.String(300))
    thumbnailUrl = db.Column(db.String(300))

class Todos(db.Model):
    __tablename__ = 'todos'
    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    completed = db.Column(db.String(10))

