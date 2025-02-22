from datetime import datetime
from db import db
from app import app  # Импортируем Flask приложение
from models import User, Course, Teacher, Review  # Подключаем модели

# Функция для заполнения базы
def seed_database():
    with app.app_context():
        # Удаляем всё и создаем таблицы заново (ОСТОРОЖНО!)
        db.drop_all()
        db.create_all()

        # Добавляем пользователей
        users = [
            User(login="user", password="123", role=0),
            User(login="moderator", password="123", role=1),
            User(login="administrator", password="123", role=2),
            
        ]
        db.session.add_all(users)

        # Добавляем курсы
        courses = [
            # ЗАПОЛНЕНО
            Course(id=1, description="Анализ и компьютерное моделирование аэрокосмических систем", rating=4.5, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Моделирование технологических процессов"),
            Course(id=2, description="Анализ и компьютерное моделирование аэрокосмических систем", rating=4.5, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="САПР технологических процессов"),
            Course(id=3, description="Астродинамика и механика космических систем", rating=4.5, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Управление движением космических аппаратов"),
            Course(id=4, description="Астродинамика и механика космических систем", rating=4.5, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Теория оптимального управления"),
            Course(id=5, description="IT в машиностроении", rating=4.5, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="VR технологии в проектировании"),
            Course(id=6, description="IT в машиностроении", rating=4.5, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Работа в PDM системах"),

            # ЗАПОЛНЕНО
            Course(id=7, description="Энергетическое машиностроение", rating=4.8, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Агрегаты и системы управления"),
            Course(id=8, description="Энергетическое машиностроение", rating=4.8, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Основы программирования ПЛК"),
            Course(id=9, description="Автоматизация технологических процессов и производств", rating=4.8, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Основы робототехники"),
            Course(id=10, description="Автоматизация технологических процессов и производств", rating=4.8, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Гидропривод и средства автоматики"),
            Course(id=11, description="Конструкторско-технологическое обеспечение машиностроительных производств", rating=4.8, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Виртуальная разработка изделий"),
            Course(id=12, description="Конструкторско-технологическое обеспечение машиностроительных производств", rating=4.8, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Метрология"),
            
            # ЗАПОЛНЕНО
            Course(id=13, description="Экономика", rating=4.8, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Профиль «Банки, финансы и инвестиции»"),
            Course(id=14, description="Экономика", rating=4.8, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Организация деятельности коммерческого банка"),
            Course(id=15, description="Менеджмент", rating=4.8, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Профиль «Цифровой маркетинг и рыночная аналитика»"),
            Course(id=16, description="Менеджмент", rating=4.8, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Эконометрические методы анализа и прогнозирования продаж"),
            Course(id=17, description="Управление персоналом", rating=4.8, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="HR-аналитика"),
            Course(id=18, description="Управление персоналом", rating=4.8, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="HR-проектирование"),
            
            # ЗАПОЛНЕНО
            Course(id=19, description="Психология", rating=4.8, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Общая психология"),
            Course(id=20, description="Психология", rating=4.8, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Экспериментальная психология"),
            Course(id=21, description="Социология", rating=4.8, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="История социологии"),
            Course(id=22, description="Социология", rating=4.8, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Общая социология"),
            Course(id=23, description="Социальная работа", rating=4.8, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Социальная безопасность"),
            Course(id=24, description="Социальная работа", rating=4.8, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Философия прав человека"),
          
            # ЗАПОЛНЕНО
            Course(id=25, description="Интеллектуальные вычисления в механике", rating=4.8, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Методы вычислений и пакеты прикладных программ"),
            Course(id=26, description="Интеллектуальные вычисления в механике", rating=4.8, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Метод конечных элементов и МКЭ-пакеты (SIMULIAAbaqus, ANSYS, Логос, CAE-Fidesys)"),
            Course(id=27, description="Математические методы моделирования и управления", rating=4.8, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Моделирование систем"),
            Course(id=28, description="Математическое обеспечение и администрирование информационных систем", rating=4.8, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Устойчивость и управление движением"),
            Course(id=29, description="Математика и компьютерные науки", rating=4.8, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Web-технологии"),
            Course(id=30, description="Математика и компьютерные науки", rating=4.8, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Java-технологии"),
           
            # ЗАПОЛНЕНО
            Course(id=31, description="Программирование и информационные технологии", rating=4.8, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Основы программирования"),
            Course(id=32, description="Программирование и информационные технологии", rating=4.8, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Методы оптимизации"),
            Course(id=33, description="Веб-технологии и прикладное программирование", rating=4.8, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Разработка WEB-приложений"),
            Course(id=34, description="Веб-технологии и прикладное программирование", rating=4.8, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Объектно-ориентированное программирование"),
            Course(id=35, description="Квантовые коммуникации и наноэлектроника", rating=4.8, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Электроника и схемотехника;"),
            Course(id=36, description="Квантовые коммуникации и наноэлектроника", rating=4.8, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Квантовая оптика"),
            
            #ЗАПОЛНЕНО
            Course(id=37, description="Юриспруденция", rating=4.8, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Теория государства и права"),
            Course(id=38, description="Юриспруденция", rating=4.8, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Международное право"),
            Course(id=39, description="Юриспруденция", rating=4.8, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Конституционное право"),
            Course(id=40, description="Юриспруденция", rating=4.8, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Административное право"),
            Course(id=41, description="Юриспруденция", rating=4.8, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Уголовное право"),
            Course(id=42, description="Юриспруденция", rating=4.8, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Криминалистика")
        ]
        db.session.add_all(courses)

        # Добавляем преподавателей
        teachers = [      
            Teacher(id=1, description="Александров Иван Петрович", rating=4.7, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Моделирование технологических процессов"),
            Teacher(id=2, description="Алексеев Сергей Владимирович", rating=4.9, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Моделирование технологических процессов"),
            Teacher(id=3, description="Антонов Михаил Игоревич", rating=4.7, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Управление движением космических аппаратов"),
            Teacher(id=4, description="Андреев Павел Сергеевич", rating=4.9, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Управление движением космических аппаратов"),
            Teacher(id=5, description="Артемьев Дмитрий Олегович", rating=4.7, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Теория оптимального управления"),
            Teacher(id=6, description="Беляев Николай Викторович", rating=4.9, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Теория оптимального управления"),
            Teacher(id=7, description="Борисов Алексей Михайлович", rating=4.7, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Моделирование технологических процессов"),
            Teacher(id=8, description="Васильев Олег Николаевич", rating=4.9, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Моделирование технологических процессов"),
            Teacher(id=9, description="Виноградов Аркадий Степанович", rating=4.7, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="VR технологии в проектировании"),
            Teacher(id=10, description="Волков Виктор Евгеньевич", rating=4.9, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="VR технологии в проектировании"),
            Teacher(id=11, description="Воронцов Станислав Павлович", rating=4.7, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Работа в PDM системах"),
            Teacher(id=12, description="Гаврилов Петр Анатольевич", rating=4.9, year=1, institutes="ИНСТИТУТ АВИАЦИОННОЙ И РАКЕТНО-КОСМИЧЕСКОЙ ТЕХНИКИ", directions="Работа в PDM системах"),

            Teacher(id=13, description="Голубев Денис Артемович", rating=4.7, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Агрегаты и системы управления"),
            Teacher(id=14, description="Григорьев Андрей Владиславович", rating=4.9, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Агрегаты и системы управления"),
            Teacher(id=15, description="Гордеев Константин Петрович", rating=4.7, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Основы программирования ПЛК"),
            Teacher(id=16, description="Давыдов Максим Александрович", rating=4.9, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Основы программирования ПЛК"),
            Teacher(id=17, description="Дмитриев Артем Владимирович", rating=4.7, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Основы робототехники"),
            Teacher(id=18, description="Дроздов Юрий Сергеевич", rating=4.9, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Гидропривод и средства автоматики"),
            Teacher(id=19, description="Егорова Светлана Ивановна", rating=4.7, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Гидропривод и средства автоматики"),
            Teacher(id=20, description="Жданов Роман Николаевич", rating=4.9, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Виртуальная разработка изделий"),
            Teacher(id=21, description="Захаров Олег Дмитриевич", rating=4.7, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Виртуальная разработка изделий"),
            Teacher(id=22, description="Зимин Геннадий Михайлович", rating=4.9, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Основы робототехники"),
            Teacher(id=23, description="Игнатов Алексей Васильевич", rating=4.7, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Метрология"),
            Teacher(id=24, description="Иванов Виктор Станиславович", rating=4.9, year=1, institutes="ИНСТИТУТ ДВИГАТЕЛЕЙ И ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК", directions="Метрология"),
             
            Teacher(id=25, description="Казаков Степан Олегович", rating=4.7, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Профиль «Банки, финансы и инвестиции"),
            Teacher(id=26, description="Калинин Николай Евгеньевич", rating=4.9, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Профиль «Банки, финансы и инвестиции"),
            Teacher(id=27, description="Карпов Артур Петрович", rating=4.7, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Организация деятельности коммерческого банка"),
            Teacher(id=28, description="Киселев Юрий Аркадьевич", rating=4.9, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Организация деятельности коммерческого банка"),
            Teacher(id=29, description="Ковалев Александр Вячеславович", rating=4.7, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Профиль «Цифровой маркетинг и рыночная аналитика»"),
            Teacher(id=30, description="Козлов Вадим Сергеевич", rating=4.9, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Профиль «Цифровой маркетинг и рыночная аналитика»"),
            Teacher(id=31, description="Крылов Игорь Викторович", rating=4.7, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Эконометрические методы анализа и прогнозирования продаж"),
            Teacher(id=32, description="Кузнецов Дмитрий Петрович", rating=4.9, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="Эконометрические методы анализа и прогнозирования продаж"),
            Teacher(id=33, description="Лазарев Артем Павлович", rating=4.7, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="HR-проектирование"),
            Teacher(id=34, description="Лебедев Николай Васильевич", rating=4.9, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="HR-проектирование"),
            Teacher(id=35, description="Логинов Олег Александрович", rating=4.7, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="HR-аналитика"),
            Teacher(id=36, description="Лукьянов Степан Евгеньевич", rating=4.9, year=1, institutes="ИНСТИТУТ ЭКОНОМИКИ И УПРАВЛЕНИЯ", directions="HR-аналитика"),
 
            Teacher(id=37, description="Лукьянов Степан Евгеньевич", rating=4.7, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Общая психология"),
            Teacher(id=38, description="Макаров Станислав Юрьевич", rating=4.9, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Общая психология"),
            Teacher(id=39, description="Матвеев Артем Викторович", rating=4.7, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Экспериментальная психология"),
            Teacher(id=40, description="Миронов Василий Александрович", rating=4.9, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Экспериментальная психология"),
            Teacher(id=41, description="Михайлов Евгений Петрович", rating=4.7, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="История социологии"),
            Teacher(id=42, description="Морозов Павел Сергеевич", rating=4.9, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="История социологии"),
            Teacher(id=43, description="Назаров Дмитрий Анатольевич", rating=4.7, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Общая социология"),
            Teacher(id=44, description="Некрасов Виктор Олегович", rating=4.9, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Общая социология"),
            Teacher(id=45, description="Никитин Андрей Владимирович", rating=4.7, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Социальная безопасность"),
            Teacher(id=46, description="Новиков Сергей Михайлович", rating=4.9, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Социальная безопасность"),
            Teacher(id=47, description="Орлов Виталий Артемович", rating=4.7, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Философия прав человека"),
            Teacher(id=48, description="Осипов Станислав Владимирович", rating=4.9, year=1, institutes="СОЦИАЛЬНО-ГУМАНИТАРНЫЙ ИНСТИТУТ", directions="Философия прав человека"),

            Teacher(id=49, description="Павлов Максим Алексеевич", rating=4.7, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Моделирование систем"),
            Teacher(id=50, description="Панфилов Аркадий Петрович", rating=4.9, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Моделирование систем"),
            Teacher(id=51, description="Петров Виктор Станиславович", rating=4.7, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Методы вычислений и пакеты прикладных программ"),
            Teacher(id=52, description="Платонов Александр Дмитриевич", rating=4.9, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Методы вычислений и пакеты прикладных программ"),
            Teacher(id=53, description="Погодин Олег Васильевич", rating=4.7, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Метод конечных элементов и МКЭ-пакеты (SIMULIAAbaqus, ANSYS, Логос, CAE-Fidesys)"),
            Teacher(id=54, description="Поляков Николай Юрьевич", rating=4.9, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Метод конечных элементов и МКЭ-пакеты (SIMULIAAbaqus, ANSYS, Логос, CAE-Fidesys)"),
            Teacher(id=55, description="Прохоров Вадим Артемович", rating=4.7, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Устойчивость и управление движением"),
            Teacher(id=56, description="Разумов Михаил Викторович", rating=4.9, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Устойчивость и управление движением"),
            Teacher(id=57, description="Рогов Алексей Николаевич", rating=4.7, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Web-технологии"),
            Teacher(id=58, description="Родионов Павел Александрович", rating=4.9, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Web-технологии"),
            Teacher(id=59, description="Румянцев Дмитрий Евгеньевич", rating=4.7, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Java-технологии"),
            Teacher(id=60, description="Савельев Олег Викторович", rating=4.9, year=1, institutes="ИНСТИТУТ ЕСТЕСТВЕННЫХ И МАТЕМАТИЧЕСКИХ НАУК", directions="Java-технологии"),

            Teacher(id=61, description="Шестаков Виктор Петрович", rating=4.7, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Основы программирования"),
            Teacher(id=62, description="Чистяков Дмитрий Артемович", rating=4.9, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Основы программирования"),
            Teacher(id=63, description="Самойлов Артем Васильевич", rating=4.7, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Методы оптимизации"),
            Teacher(id=64, description="Сафонов Николай Петрович", rating=4.7, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Методы оптимизации"),
            Teacher(id=65, description="Соловьев Николай Евгеньевич", rating=4.7, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Разработка WEB-приложений"),
            Teacher(id=66, description="Соколов Артур Васильевич", rating=4.9, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Разработка WEB-приложений"),
            Teacher(id=67, description="Селезнев Виктор Дмитриевич", rating=4.7, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Объектно-ориентированное программирование"),
            Teacher(id=68, description="Семенов Степан Александрович", rating=4.9, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Объектно-ориентированное программирование"),
            Teacher(id=69, description="Сорокин Павел Викторович", rating=4.7, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Электроника и схемотехника"),
            Teacher(id=70, description="Степанов Андрей Петрович", rating=4.9, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Электроника и схемотехника"),
            Teacher(id=71, description="Тарасов Виктор Артемович", rating=4.7, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Квантовая оптика"),
            Teacher(id=72, description="Тимофеев Михаил Николаевич", rating=4.9, year=1, institutes="ИНСТИТУТ ИНФОРМАТИКИ И КИБЕРНЕТИКИ", directions="Квантовая оптика"),

            Teacher(id=73, description="РАЯН ГОСЛИНГ Ниолаевич", rating=4.7, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Теория государства и права"),
            Teacher(id=74, description="АААААААААААА АААААААА АААААААА", rating=4.9, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Теория государства и права"),
            Teacher(id=75, description="Картина На Стене", rating=4.7, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Международное право"),
            Teacher(id=76, description="Табуретка Рядовой", rating=4.9, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Международное право"),
            Teacher(id=77, description="Сол Гудман Викторович", rating=4.7, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Конституционное право"),
            Teacher(id=78, description="Брекинг Бед Йоу", rating=4.9, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Конституционное право"),
            Teacher(id=79, description="Величайший Папзан Артасович", rating=4.7, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Административное право"),
            Teacher(id=80, description="Шадоу Харт Жрицовна", rating=4.9, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Административное право"),
            Teacher(id=81, description="Пудж Раджер Бучкович", rating=4.7, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Уголовное право"),
            Teacher(id=82, description="Евил Артас МинниПекка", rating=4.9, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Уголовное право"),
            Teacher(id=83, description="Абаюндович Иииигооооооорь Фиолетовый", rating=4.7, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Криминалистика"),
            Teacher(id=84, description="Маньякин Рассказович Бипкин", rating=4.9, year=1, institutes="ЮРИДИЧЕСКИЙ ИНСТИТУТ", directions="Криминалистика")
        ]
        db.session.add_all(teachers)
        #ДимаГпт0.6
        # Добавляем отзывы
        reviews = [
            Review(text="Эщкерее!", rating=5, created_at=datetime.now(), teacher_name="Шестаков Виктор Петрович", direction="Основы программирования", login="user"),
            Review(text="Хороший, но сложный", rating=4, created_at=datetime.now(),  teacher_name="Чистяков Дмитрий Артемович", direction="Основы программирования", login="user"),
            Review(text="Очень классный препод!", rating=5, created_at=datetime.now(),  teacher_name="Самойлов Артем Васильевич",  direction="Методы оптимизации",login="moderator"),
            Review(text="Лайк за то, что поставил автомат!", rating=4, created_at=datetime.now(), teacher_name="Сафонов Николай Петрович",  direction="Методы оптимизации",login="moderator"),
            Review(text="Отличный курс!", rating=5, created_at=datetime.now(), teacher_name="Соловьев Николай Евгеньевич",  direction="Разработка WEB-приложений",login="administrator"),
            Review(text="Тяжелый :((( Сложно...", rating=3, created_at=datetime.now(), teacher_name="Соколов Артур Васильевич",  direction="Разработка WEB-приложений",login="administrator"),
        ]
        db.session.add_all(reviews)

        # Сохраняем изменения
        db.session.commit()
        print("База данных заполнена!")

if __name__ == "__main__":
    seed_database()
