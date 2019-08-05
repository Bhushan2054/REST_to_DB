from  RESTAPI import db
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
