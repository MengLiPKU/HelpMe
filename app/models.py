from app import db


class User(db.Model):
    id = db.Column()


class Help(db.Model):
    id = db.Column()