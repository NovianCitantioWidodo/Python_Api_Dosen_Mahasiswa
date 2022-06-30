from app import app, response
from app.controller import DosenController, UserController, MahasiswaController
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required


@app.route('/')
def index():
    return "Welcome"

@app.route('/protected', methods=['GET'])
@jwt_required() #https://flask-jwt-extended.readthedocs.io/en/stable/v4_upgrade_guide/
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, "Sukses")

# @app.route('/admin', methods=['POST'])
# def admin():
#     return UserController.buatAdmin()

@app.route('/upload-file', methods=['POST'])
def upload():
    return  UserController.upload()

@app.route('/dosen', methods=['GET', 'POST'])
def dosen():
    if request.method == 'GET':
        return DosenController.index()
    elif request.method == 'POST':
        return DosenController.save()

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def dosenDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'PUT':
        return DosenController.update(id)
    elif request.method == 'DELETE':
        return DosenController.delete(id)

@app.route('/dosen/page', methods=['GET'])
def dosen_page():
    return DosenController.paginate()

@app.route('/login', methods=['POST'])
def login():
    return UserController.login()


@app.route('/mahasiswa', methods=['GET', 'POST'])
def mahasiswa():
    if request.method == 'GET':
        return MahasiswaController.index()
    elif request.method == 'POST':
        return MahasiswaController.add()

@app.route('/mahasiswa/<id>', methods=['GET', 'PUT', 'DELETE'])
def mahasiswaDetail(id):
    if request.method == 'GET':
        return MahasiswaController.detail(id)
    elif request.method == 'PUT':
        return MahasiswaController.update(id)
    elif request.method == 'DELETE':
        return MahasiswaController.delete(id)