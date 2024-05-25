from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return f"User name: {self.name}"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email
        }