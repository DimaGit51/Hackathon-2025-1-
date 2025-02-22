from flask_sqlalchemy import SQLAlchemy

# Создаем единственный экземпляр SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """
    Инициализация базы данных.
    """
    # Настройка подключения к базе данных
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Используем SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Инициализация базы данных в приложении Flask
    db.init_app(app)