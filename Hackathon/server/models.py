from sqlalchemy import JSON, CheckConstraint
from db import db  # Импортируем db из db.py

class User(db.Model):
    login = db.Column(db.String(32), primary_key=True)  # логин 32 символа
    password = db.Column(db.String(32), nullable=False)  # пароль 32 символа
    role = db.Column(db.Integer, default=0)  # 0 - обычный пользователь, 1 - модератор, 2 - админ
    reviews = db.relationship("Review", backref="author", lazy=True)

    __table_args__ = (
        CheckConstraint('role IN (0, 1, 2)', name='check_user_role'),#поменять на 3 2 1
    )  # Проверка корректности роли


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id отзыва
    text = db.Column(db.String(301), nullable=False)  # текст отзыва (макс. 301 символ)
    rating = db.Column(db.Integer, nullable=False)  # рейтинг 0-5 (целое)
    created_at = db.Column(db.DateTime, nullable=False)  # дата и время создания отзыва
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=True)  # курс айди предмета
    teacher_name = db.Column(db.String, db.ForeignKey("teacher.description"), nullable=True)  # преподаватель
    direction = db.Column(db.String(500), nullable=False, default="") 
    login=db.Column(db.String(32), db.ForeignKey("user.login"))#юзер связь
    __table_args__ = (
        CheckConstraint('rating >= 0 AND rating <= 5', name='check_rating_range'),
    )  # Контроль границ рейтинга

#да чт
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    description = db.Column(db.Text, nullable=False) #направления
    rating = db.Column(db.Float, default=0.0)
    year = db.Column(db.Integer, nullable=False)
    institutes = db.Column(db.String(500), nullable=False, default="")  # Строка
    directions = db.Column(db.String(500), nullable=False, default="")  # предметы

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)  #имя
    rating = db.Column(db.Float, default=0.0)
    year = db.Column(db.Integer, nullable=False)
    institutes = db.Column(db.String(500), nullable=False, default="")  # Строка
    directions = db.Column(db.String(500), nullable=False, default="")  # предметы