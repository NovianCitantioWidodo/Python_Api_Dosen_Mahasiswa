from app import db

class Dosen(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nidn = db.Column(db.String(30), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    alamat = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Dosen {}>'.format(self.name)