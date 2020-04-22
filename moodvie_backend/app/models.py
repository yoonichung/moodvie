from app import db

class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    release_year = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Title {}>'.format(self.title)