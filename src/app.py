"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Starships, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Traer todos los usuarios
@app.route('/users', methods=['GET'])
def get_all_users():
    all_users = User.query.all()
    users_serialized = []
    for user in all_users:
        users_serialized.append(user.serialize())
    print(users_serialized)
    return jsonify({"data": users_serialized}), 200

# Traer sólo un usuario
@app.route('/user/<int:id>', methods=['GET'])
def get_single_user(id):
    single_user = User.query.get(id)
    if single_user is None:
        return jsonify({"msg": "User with id: {}, not found".format(id)}), 400
    return jsonify({"data": single_user.serialize()}), 200

@app.route('/user', methods=['POST'])
def new_user():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "You should send info in body"}), 400
    if "name" not in body:
        return jsonify({"msg": "Name is needed"}), 400
    if "last_name" not in body:
        return jsonify({"msg": "Last name is needed"}), 400
    if "email" not in body:
        return jsonify({"msg": "email is needed"}), 400
    if "password" not in body:
        return jsonify({"msg": "Password is needed"}), 400
    
    new_user = User()
    new_user.id = body.get("id", User.generateId())
    new_user.name = body["name"]
    new_user.last_name = body["last_name"]
    new_user.email = body["email"]
    new_user.password = body["password"]
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"data": new_user.serialize()}), 201

# Traer todos los personajes
@app.route('/people', methods=['GET'])
def get_all_people():
    all_people = People.query.all()
    people_serialized = []
    for people in all_people:
        people_serialized.append(people.serialize())
    print(people_serialized)
    return jsonify({"data": people_serialized}), 200

# Traer un sólo personaje
@app.route('/people/<int:id>', methods=['GET'])
def get_single_people(id):
    single_people = People.query.get(id)
    if single_people is None:
        return jsonify({"msg": "People with id: {}, not found".format(id)}), 400
    return jsonify({"data": single_people.serialize()}), 200

# Crear nuevo personaje
@app.route('/people', methods=['POST'])
def new_people():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "You should send info in body"}), 400
    if  "name" not in body:
        return jsonify({"msg": "Name is needed"}), 400
    if "heigth" not in body:
        return jsonify({"msg": "Heigth is needed"}), 400
    if "mass" not in body:
        return jsonify({"msg": "Mass is needed"}), 400
    if "hair_color" not in body:
        return jsonify({"msg": "Hair color is needed"}), 400
    if "eye_color" not in body:
        return jsonify({"msg": "Eye color is needed"}), 400
    if "skin_color" not in body:
        return jsonify({"msg": "Skin color is needed"}), 400
    if "birth_year" not in body:
        return jsonify({"msg": "Birth year is needed"}), 400
    if "gender" not in body:
        return jsonify({"msg": "Gender is needed"}), 400
    
    new_people = People()
    new_people.id = body.get("id", People.generateId())
    new_people.name = body["name"]
    new_people.heigth = body["heigth"]
    new_people.mass = body["mass"]
    new_people.hair_color = body["hair_color"]
    new_people.eye_color = body["eye_color"]
    new_people.skin_color = body["skin_color"]
    new_people.birth_year = body["birth_year"]
    new_people.gender = body ["gender"]
    db.session.add(new_people)
    db.session.commit()
    
    return jsonify({"data": new_people.serialize()}), 201

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
