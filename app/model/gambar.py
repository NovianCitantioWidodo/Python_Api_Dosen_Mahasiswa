from app import db

class Gambar(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    judul = db.Column(db.String(255), nullable=False)
    pathname = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return '<Gambar {}>'.format(self.name)