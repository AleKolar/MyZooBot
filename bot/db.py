import sqlite3

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from handlers.try_choosing_handlers import amount

amount = 14
class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.amount = amount


    def user_exist(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(res))

    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
            return self.connection.commit()

    def add_pic(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS photos(amount_photo INTEGER PRIMARY KEY, photo BLOB)')
        i = self.amount
        #for i in range(13, 22):
        with open(f'{i}.jpeg', 'rb') as photo:
            h = photo.read()
            #self.cursor.execute('INSERT INTO photos(photo) VALUES(?)', [h])
            self.cursor.execute("INSERT INTO photos (photo, amount_photo) VALUES (?, ?)", (h, i))
        return self.connection.commit()

    def close(self):
        self.connection.close()


a = Database('DB1')
a.add_pic()

'''

# Открываем соединение с базой данных
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Фотография и идентификационный номер
photo_data = b'your_photo_data'
photo_id = 'photo1'

# Выполняем запрос SQL для добавления фотографии в таблицу photos
cursor.execute("INSERT INTO photos (photo, amount_photo) VALUES (?, ?)", (photo_data, photo_id))

# Сохраняем изменения и закрываем соединение с базой данных
conn.commit()
conn.close()
'''