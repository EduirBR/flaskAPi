import uuid
from sqlalchemy_utils import UUIDType
from project import db

class DbModel:
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise ValueError(str(e))

class Contact(db.Model, DbModel):
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20), unique=True)


    def save(self):
        if not self.email and not self.phone:
            raise ValueError('Email or Phone is required')
        super().save()

    def __repr__(self):
        return f'<Contact {self.name}>'

    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
        }
    
    