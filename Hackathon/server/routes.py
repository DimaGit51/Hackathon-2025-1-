from flask import Blueprint, request, jsonify, Flask

from db import db
from models import User, Course, Teacher, Review, db
from cenz import ProfanityFilter
import datetime

import logging


app = Flask(__name__)
api = Blueprint("api", __name__)
profanity_filter = ProfanityFilter()

# Добавление пользователя
@api.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data.get("login") or not data.get("password"):  # Проверяем наличие логина и пароля
        return jsonify({"error": "Логин и пароль обязательны"}), 400

    new_user = User(
        login=data["login"],
        password=data["password"],  # Убедитесь, что пароль передается
        role=data.get("role", 0)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Пользователь добавлен!"}), 201

# Получение всех пользователей
@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    users_list = [{"login": user.login,"password":user.password, "role": user.role} for user in users]
    return jsonify(users_list), 200

# Получение пользователя по логину
@api.route("/users/<string:login>", methods=["GET"])
def get_user(login):
    user = User.query.get_or_404(login)
    return jsonify({"login": user.login, "role": user.role}), 200

# Добавление курса
@api.route("/courses", methods=["POST"])
def add_course():
    data = request.get_json()
    new_course = Course(
        description=data["description"],
        rating=data.get("rating", 0.0),
        year=data["year"],  # Новое поле
        institutes=data["university_id"],
        directions=data["direction_id"]
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify({"message": "Курс добавлен!"}), 201

#Получение всех курсов
@api.route("/courses", methods=["GET"])
def get_courses():
    institute_name = request.args.get('institute', '')
    direction_name = request.args.get('direction', '')
    print(institute_name)
    print(direction_name)
    courses = Course.query.filter(Course.institutes == institute_name, Course.description == direction_name).all()

    #     institute_name = request.args.get('institute', '')
    # direction_name = request.args.get('direction', '')
    # print(institute_name)
    # print(direction_name)
    # courses = Course.query.filter(Course.institutes == institute_name, Course.directions == direction_name).all()
    # print(courses)
    courses_list = [{"id": course.id, "description": course.description, "rating": course.rating,"year": course.year,"institutes":course.institutes,"directions":course.directions} for course in courses]
    # courses_list = [
    #     {
    #         "id": course.id,
    #         "description": course.description,
    #         "rating": course.rating,
    #         "year": course.year,
    #         "institutes": course.institutes,
    #         "directions": course.directions
    #     }
    #     for course in courses
    #     if course.id % 2 == 0  # Оставляем только четные course.id
    # ]

    return jsonify(courses_list), 200  #?





# Получение курса по ID
@api.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify({"id": course.id, "description": course.description, "rating": course.rating,"year": course.year,"institutes":course.institutes,"directions":course.directions}), 200

# Добавление преподавателя
@api.route("/teachers", methods=["POST"])
def add_teacher():
    data = request.get_json()
    new_teacher = Teacher(
        description=data["description"],
        rating=data.get("rating", 0.0),
        year=data["year"],  # Новое поле
        institutes=data["university_id"],
        directions=data["direction_id"]
    )
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({"message": "Преподаватель добавлен!"}), 201

# Получение всех преподавателей
@api.route("/teachers", methods=["GET"])
def get_teachers():
    teachers = Teacher.query.all()
    teachers_list = [{"id": teacher.id, "description": teacher.description, "rating": teacher.rating,"year": teacher.year,"institutes":teacher.institutes,"directions":teacher.directions} for teacher in teachers]
    return jsonify(teachers_list), 200

# Получение преподавателя по ID
@api.route("/teachers/<int:teacher_id>", methods=["GET"])
def get_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    return jsonify({"id": teacher.id, "description": teacher.description, "rating": teacher.rating,"year": teacher.year,"institutes":teacher.institutes,"directions":teacher.directions}), 200

# Вспомогательная функция для пересчета рейтинга
def update_rating(entity):
    """Пересчитывает рейтинг для курса или преподавателя на основе отзывов."""
    if entity.reviews:
        entity.rating = round(sum(r.rating for r in entity.reviews) / len(entity.reviews), 1)
    else:
        entity.rating = 0.0
    db.session.commit()





# Добавление отзыва
@api.route("/add_reviews", methods=["POST"])
def add_review():
    data = request.get_json()
    print("LOGGGGGIIIII: ", data)
    
    # Проверка рейтинга
    if not (0 <= float(data["rating"]) <= 5):
        return jsonify({"error": "Рейтинг должен быть от 0 до 5"}), 400
    
    
    # Создание отзыва с текущей датой и временем
    new_review = Review(
        text=data["text"],
        rating=int(data["rating"]),
        created_at=datetime.datetime.now(),
        course_id=0,
        teacher_name=data.get("teacher_name"),
        direction=data.get("direction"),
        login=data["login"] # Используем login вместо user_id     
        
    )
    #
    #Проверка на запрещенные слова
    filtered_text = profanity_filter.filter_profanity(data["text"])
    if filtered_text:
        return jsonify({"error": "Текст содержит запрещённые слова"}), 400
    
    db.session.add(new_review)
    db.session.commit()

    

    return jsonify({"message": "Отзыв добавлен!"}), 201



# Получение всех отзывов
@api.route("/reviews", methods=["GET"])
def get_reviews():
    direction_name = request.args.get('direction', '')
    # print(direction_name)
    reviews = Review.query.filter(Review.direction == direction_name).all()
    

    reviews_list = [{
        "text": review.text,
        "rating": review.rating,
        "login": review.login,  # Исправлено user_login → login
        "teacher_name": review.teacher_name,
        "created_at": review.created_at.isoformat()
        } for review in reviews]    
   #0 print(reviews_list)
    return jsonify(reviews_list), 200

# Получение отзыва по ID
@api.route("/reviews/<int:review_id>", methods=["GET"])
def get_review(review_id):
    review = Review.query.get_or_404(review_id)
    return jsonify({
        "id": review.id,
        "text": review.text,
        "rating": review.rating,
        "login": review.login,  # Исправлено
        "course_id": review.course_id,
        "teacher_id": review.teacher_id,
        "created_at": review.created_at.isoformat()
    }), 200





#Достаём данные пользователя
@api.route("/auth", methods=["POST","GET"])
def authenticate():
    data = request.get_json()
    
    print("Получены данные:", data)  # Показываем, что пришло от клиента

    login = data.get("login")
    password = data.get("password")

    user = User.query.filter_by(login=login, password=password).first()

    if user:
        print("Я все отправил!/auth")
        return jsonify({"login": user.login, "prefix": user.role}), 200
    else:
        print("Ошибка/auth ")
        return jsonify({"error": "Неверные логин или пароль"}), 401




#Достаём направления с помощью Института
@api.route("/directions/<int:institute_id>", methods=["GET"])
def get_directions(institute_id):
    # Найдем название института по его id
    institutes_map = {
        1: "ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ",
        2: "ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК",
        3: "ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ",
        4: "СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ",
        5: "ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК",
        6: "ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ",
        7: "ЮРИДИЧЕСКИЙ ИНСТИТУТ"
    }

    institute_name = institutes_map.get(institute_id)
    if not institute_name:
        return jsonify({"error": "Институт не найден"}), 404

    # Получаем курсы, связанные с этим институтом
    courses = Course.query.filter_by(institutes=institute_name).all()

    # Формируем список направлений
    directions = [{"id": course.id, "name": course.description} for course in courses]

    return jsonify(directions)



# Удаление отзыва
@app.route('/delete_review', methods=['DELETE'])
def delete_review():
    try:
        data = request.get_json()
        review_text = data.get("text")

        if not review_text:
            return jsonify({"error": "Текст отзыва обязателен"}), 400

        # Удаляем ОДИН отзыв (но могут быть дубликаты!)
        review = Review.query.filter_by(text=review_text).first()
        if not review:
            return jsonify({"error": "Отзыв не найден"}), 404

        db.session.delete(review)
        db.session.commit()

        return jsonify({"message": "Отзыв удалён!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500









#что пытаешься сделать?
#Достаём дисциплины с помощью Института и Направления
logging.basicConfig(level=logging.DEBUG)

@app.route('/api/courses', methods=['GET'])
def get_courses():
    institute_name = request.args.get('institute', '')
    direction_name = request.args.get('direction', '')

    logging.debug("Institute: %s, Direction: %s", institute_name, direction_name)

    # Фильтрация по институту и направлению
    # courses = Course.query.filter(Course.institutes == institute_name, Course.directions == direction_name).all()
    courses = Course.query.filter(
            Course.institutes.contains(institute_name),  # Поиск подстроки в institutes
            Course.directions.contains(direction_name)   # Поиск подстроки в directions
        ).all()
    logging.debug("Courses: %s", courses)

    # Преобразуем в JSON
    result = [{"id": c.id, "description": c.description, "year": c.year} for c in courses]
    
    logging.debug("Result: %s", result)

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)



