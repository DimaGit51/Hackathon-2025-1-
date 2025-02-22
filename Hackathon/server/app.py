from flask import Flask, render_template
from db import db, init_db
from routes import api  # ✅ Подключаем маршруты
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Инициализируем базу данных
init_db(app)  # 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 ВАЖНО: теперь база данных привязывается к `app`
#with app.app_context():
    # Удаляем все таблицы🔥
 #   db.drop_all()🔥
  #  print("Все таблицы удалены.")🔥
#🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
    # Создаем все таблицы заново🔥
   # db.create_all()🔥
    #print("База данных создана заново.")🔥
# Подключаем маршруты API🔥
app.register_blueprint(api)
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
