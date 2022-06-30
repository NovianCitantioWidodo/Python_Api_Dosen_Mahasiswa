from app.model.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request


def index():
    try:
        mahasiswa = Mahasiswa.query.all()
        data = listObject(mahasiswa)
        return response.success(data, "success")
    
    except Exception as e:
        print(e)

def listObject(data):
    datas = [singleObject(i) for i in data]
    return datas

def singleObject(data):
    datas = {
        'id': data.id,
        'nim': data.nidn,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat,
        'dosen satu': data.dosen_satu,
        'dosen dua': data.dosen_dua
    }
    return datas

def detail(id):
    try:
        mahasiswa = Mahasiswa.query.filter_by(id=id).first()
        if not mahasiswa:
            return response.badRequest([], "Tidak ada data")
        else:
            data = singleObject(mahasiswa)
            return response.success(data, "success")

    except Exception as e:
        print(e)

def add():
    try :
        mahasiswa = Mahasiswa(
            nidn=request.form.get('nidn'),
            nama=request.form.get('nama'),
            phone=request.form.get('phone'),
            alamat=request.form.get('alamat'),
            dosen_satu=request.form.get('dosen_satu'),
            dosen_dua=request.form.get('dosen_dua'))
        
        data = singleObject(mahasiswa)
        db.session.add(mahasiswa)
        db.session.commit()
        return response.success('', 'Sukses menambahkan data')
    
    except Exception as e:
        print(e)

def update(id):
    try:
        mahasiswa = Mahasiswa.query.filter_by(id=id).first()
        mahasiswa.nidn=request.form.get('nidn'),
        mahasiswa.nama=request.form.get('nama'),
        mahasiswa.phone=request.form.get('phone'),
        mahasiswa.alamat=request.form.get('alamat'),
        mahasiswa.dosen_satu=request.form.get('dosen_satu'),
        mahasiswa.dosen_dua=request.form.get('dosen_dua')

        data = singleObject(mahasiswa)
        db.session.commit()
        return response.success(data, 'Sukses merubah data')
    
    except Exception as e:
        print(e)

def delete(id):
    try:
        mahasiswa = Mahasiswa.query.filter_by(id=id).first()
        data = singleObject(mahasiswa)
        db.session.delete(mahasiswa)
        db.session.commit()
        return response.success(data, 'Data telah dihapus')
    
    except Exception as e:
        print(e)