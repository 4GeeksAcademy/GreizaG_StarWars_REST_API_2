from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

last_id_user = 0
last_id_people = 0
last_id_starships = 0
last_id_planets = 0
    
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    
    def generateId():
        global last_id_user
        last_id_user += 1
        return last_id_user

    def __repr__(self):
        return f"User name: {self.name}"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email
        }
    
class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    heigth = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(20))
    eye_color = db.Column(db.String(20))
    skin_color = db.Column(db.String(20))
    birth_year = db.Column(db.String(20))
    gender = db.Column(db.String(20))

    def generateId():
        global last_id_people
        last_id_people += 1
        return last_id_people

    def __repr__(self):
        return f"Character name: {self.name}"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "heigth": self.heigth,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }
    
class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    model = db.Column(db.String(50))
    starship_class = db.Column(db.String(50))
    length = db.Column(db.Integer)
    crew = db.Column(db.String(20))
    passengers = db.Column(db.Integer)

    def generateId():
        global last_id_starships
        last_id_starships += 1
        return last_id_starships

    def __repr__(self):
        return f"Starship name: {self.name}"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "starship_class": self.starship_class,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    diameter = db.Column(db.Integer)
    gravity = db.Column(db.String(50))
    population = db.Column(db.String(20))
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    surface_water = db.Column(db.Integer)

    def generateId():
        global last_id_planets
        last_id_planets += 1
        return last_id_planets

    def __repr__(self):
        return f"Planet name: {self.name}"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water
        }
    
class FavoritePeople(db.Model):
    __tablename__ = 'favorite_people'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship(User)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    people_id_relationship = db.relationship(People)

    def __repr__(self):
        return f"User: {self.use_id} -> likes character {self.people_id}"
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }
    
class FavoriteStarships(db.Model):
    __tablename__ = 'favorite_starships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship(User)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship_id_relationship = db.relationship(Starships)

    def __repr__(self):
        return f"User: {self.user_id} -> likes starship: {self.starship_id}"
    
    def serialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "starship_id": self.starship_id
        }
    
class FavoritePlanets(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship(User)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_id_relationship = db.relationship(Planets)

    def __repr__(self):
        return f"User: {self.user_id} -> likes planet: {self.planet_id}"
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }