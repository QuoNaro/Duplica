from sqlalchemy import create_engine, text


DATABASE_URL = "mssql+pyodbc://sa:Password!23@localhost:1433/master?driver=ODBC+Driver+17+for+SQL+Server"

# Подключение к базе данных
engine = create_engine(DATABASE_URL)




# Путь, куда будет сохраняться бэкап
backup_file_path = '/backup.bak'

# SQL-запрос для создания бэкапа
backup_query = text(f"BACKUP DATABASE [master] TO DISK = '{backup_file_path}'")

# Подключение и выполнение бэкапа
with engine.connect() as connection:
    connection.execute(backup_query)

print(f"Backup successfully created at: {backup_file_path}")


