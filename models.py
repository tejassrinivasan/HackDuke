from sqlalchemy import sql, orm, CheckConstraint, ForeignKeyConstraint
from app import db
from sqlalchemy import sql, orm, CheckConstraint
from app import db
from flask_login import UserMixin

class Teachers(UserMixin, db.Model):
    __tablename__ = 'teachers'
    username = db.Column('username', db.String(30), primary_key=True)
    password = db.Column('password', db.String(100))
    location = db.Column('location', db.String(800))
    subjects = db.Column('subjects', db.String(100))
    education_level = db.Column('education_level', db.String(100))
    bio = db.Column('bio', db.String(200))
    maiden = db.Column('maiden', db.String(800))
    def get_id(self):
        return (self.username)

class Resources(db.Model):
    __tablename__ = 'Resources'
    resource_id = db.Column('resource_id', db.String(30), primary_key=True)
    teacher_id = db.Column('teacher_id', db.String(30), primary_key=True)
    resource_name = db.Column('resource_name', db.String(500))
    category = db.Column('category', db.String(100))
    subject = db.Column('subject', db.String(100))
    file = db.Column('file', db.String(1000))
    description = db.Column('description', db.String(2000))
    date_posted = db.Column('date_posted', db.String(100))

class Reviews(db.Model):
    __tablename__ = 'reviews'
    review_id = db.Column('review_id', db.Integer, autoincrement=True, primary_key=True)
    resource_id = db.Column('resource_id', db.String(30))
    teacher_id = db.Column('teacher_id',db.String(30))
    reviewer_username = db.Column('reviewer_username', db.String(30))
    item_rating = db.Column('item_rating', db.Integer,CheckConstraint('rating >= 1 AND rating <= 5'))
    comments = db.Column('comments', db.String(2000))
    __table_args__ = (ForeignKeyConstraint((resource_id, teacher_id),
                                           [Resources.resource_id, Resources.teacher_id]), {})
