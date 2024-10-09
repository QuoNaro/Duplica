from peewee import Model, SqliteDatabase, BooleanField, CharField

# Создаем подключение к базе данных
db = SqliteDatabase('db.sqlite')

# Определяем модель
class ActionsHistory(Model):
    class Meta: 
        database = db  # Указываем базу данных
    action = CharField(max_length=255)  # max_length можно указать явно
    status = BooleanField(default=True)   # Используем default для значения по умолчанию



# Создаем таблицы
try:
    db.connect()  # Подключаемся к базе данных
    db.create_tables([ActionsHistory])  # Создаем таблицы
except Exception as e:
    print(f"An error occurred: {e}")  # Обрабатываем исключения
finally:
    db.close()  # Закрываем соединение