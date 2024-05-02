from app import db

class User(db.Model)
    __tablename__ = 'User'

    id = db.Column(*args:db.Integer, primary_key=True)
    username= db.Column(*args:db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at =db.Column(db.DateTime, default=datetime.utcnow)
    age = db.Column(db.Integer, nullable=False)
    region = db.Column(db.String(50), nullable=False)
    bmi = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.name}, 