from app import db, create_app

class Post(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    preview_path    = db.Column(db.String)
