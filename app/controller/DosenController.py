from os import link
from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request, jsonify, abort
import math

def index():
    try:
        dosen = Dosen.query.all()
        data = formatarray(dosen)
        return response.success(data, "success")
    
    except Exception as e:
        print(e)

def formatarray(datas):
    array = []
    for i in datas:
        array.append(singleObject(i))
    return array

def singleObject(data):
    data = {
        'id': data.id,
        'nidn': data.nidn,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat
    }
    return data

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))
        if not dosen:
            return response.badRequest([], "Tidak ada data dosen")
    
        datamahasiswa = formatMahasiswa(mahasiswa)
        data = singleDetailMahasiswa(dosen, datamahasiswa)

    except Exception as e:
        print(e)

    return response.success(data, "success")

def formatMahasiswa(data):
    array = []
    for i in data:
        array.append(singleMahasiswa(i))
    return array

def singleMahasiswa(mahasiswa):
    data = {
        'id': mahasiswa.id,
        'nim': mahasiswa.nim,
        'nama': mahasiswa.nama,
        'phone': mahasiswa.phone,
        'alamat': mahasiswa.alamat
    }
    return data

def singleDetailMahasiswa(dosen, mahasiswa):
    data = {
        'id': dosen.id,
        'nidn': dosen.nidn,
        'nama': dosen.nama,
        'phone': dosen.phone,
        'mahasiswa': mahasiswa
    }
    return data

def save():
    try :
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        dosens = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosens)
        db.session.commit()

        return response.success('', 'Sukses menambahkan data')
    
    except Exception as e:
        print(e)

def update(id):
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')
        
        input = [
            {
                'nidn': nidn,
                'nama': nama,
                'phone': phone,
                'alamat': alamat
            }
        ]

        dosen = Dosen.query.filter_by(id=id).first()
        dosen.nidn = nidn
        dosen.nama = nama
        dosen.phone = phone
        dosen.alamat = alamat
        
        db.session.commit()

        return response.success(input, 'Sukses merubah data')
    
    except Exception as e:
        print(e)

def delete(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        if not dosen:
            return response.badRequest([], 'Data kosong')
        
        db.session.delete(dosen)
        db.session.commit()
        return response.success('', 'Data dihapus')

    except Exception as e:
        print(e)

def get_pagination(input_class, url, start, limit):
    results = input_class.query.all()
    data = formatarray(results)
    count = len(data)
    obj = {}
    if count < start:
        obj['success'] = False
        obj['message'] = "page yang dipilih melewati batas total data !"
        return obj
    
    else:
        obj['success'] = True
        obj['start_page'] = start
        obj['set_page'] = limit
        obj['total_data'] = count
        obj['total_page'] = math.ceil(count/limit)

        # previous link
        if start == 1:
            obj['previous'] = ''
        else:
            start_copy = max(1, start - limit)
            limit_copy = start - 1
            obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)

        # next link
        if start + limit > count:
            start_copy = start + limit
            obj['next'] = ''
        else:
            start_copy = start + limit
            obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
        
        obj['result'] = data[(start - 1) : (start - 1 + limit)]
        return obj

def paginate():
    # example www.google.com?product=baju
    start = request.args.get('start')
    limit = request.args.get('limit')

    try:
        if start == None or limit == None:
            return jsonify(get_pagination(
                Dosen,
                'http://127.0.0.1:5000/dosen/page',
                start = request.args.get('start', 1),
                limit = request.args.get('limit', 3)
            ))
        else:
            return jsonify(get_pagination(
                Dosen,
                'http://127.0.0.1:5000/dosen/page',
                start = int(start),
                limit = int(limit)
            ))

    except Exception as e:
        print(e)
